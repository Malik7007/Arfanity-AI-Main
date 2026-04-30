import asyncio
import os
import sys
import json

# Add the current directory to sys.path to import arfanity_ai
sys.path.append(os.getcwd())

from arfanity_ai.internal.db import get_async_db_context
from arfanity_ai.config import Config
from sqlalchemy import select

async def main():
    async with get_async_db_context() as db:
        res = await db.execute(select(Config).order_by(Config.id.desc()).limit(1))
        config = res.scalars().first()
        if config:
            print("DB_CONFIG_FOUND:TRUE")
            print(json.dumps(config.data, indent=2))
        else:
            print("DB_CONFIG_FOUND:FALSE")

if __name__ == "__main__":
    asyncio.run(main())
