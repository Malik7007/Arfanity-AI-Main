# Stage 1: Build the Frontend
FROM node:20-alpine AS build-frontend
WORKDIR /app/frontend
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Build the Backend
FROM python:3.11-slim AS build-backend
WORKDIR /app/backend

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    ffmpeg \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./

# Stage 3: Final Production Image
FROM python:3.11-slim
WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy built backend
COPY --from=build-backend /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build-backend /usr/local/bin /usr/local/bin
COPY --from=build-backend /app/backend /app/backend

# Copy built frontend to the backend's static directory
COPY --from=build-frontend /app/frontend/build /app/build

# Set environment variables
ENV ENV=prod
ENV FRONTEND_BUILD_DIR=/app/build
ENV DATA_DIR=/app/data
ENV PORT=8080

EXPOSE 8080

WORKDIR /app/backend
CMD ["uvicorn", "arfanity_ai.main:app", "--host", "0.0.0.0", "--port", "8080"]
