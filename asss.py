import asyncio
import aiohttp
from asyncio import tasks
from pip import main
import httpx
import time





async def get_users():
    url = [f'https://jsonplaceholder.typicode.com/']
    tasks = []
    for id in url:
        task = get_users(*url)
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    results = asyncio.run(main())