import asyncio
import os
import sys
import json

# Add the current directory to sys.path to import arfanity_ai
sys.path.append(os.getcwd())

from arfanity_ai.models.users import Users
from arfanity_ai.internal.db import get_async_db_context
from sqlalchemy import select, text

async def main():
    async with get_async_db_context() as db:
        count = await Users.get_num_users(db=db)
        print(f"USER_COUNT:{count}")
        res = await Users.get_users(db=db)
        for u in res['users']:
            print(f"USER: {u.email} | ROLE: {u.role} | NAME: {u.name}")

if __name__ == "__main__":
    asyncio.run(main())
