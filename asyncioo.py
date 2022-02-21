import asyncio
from asyncio import tasks
import httpx
import time
import json

start_time = time.time()
all_data = []


async def get_users(client, url):
    resp = await client.get(url)
    users = resp.json()
    return users

async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for id_number in range(1, 2):
            url = f'https://jsonplaceholder.typicode.com/users/{id_number}/posts'
            tasks.append(asyncio.ensure_future(get_users(client, url)))
            url = f'https://jsonplaceholder.typicode.com/users/{id_number}/todos'
            tasks.append(asyncio.ensure_future(get_users(client, url)))
            url = f'https://jsonplaceholder.typicode.com/users/{id_number}/albums'
            tasks.append(asyncio.ensure_future(get_users(client, url)))
            url = f'https://jsonplaceholder.typicode.com/posts/{id_number}/comments'
            tasks.append(asyncio.ensure_future(get_users(client, url)))
            url = f'https://jsonplaceholder.typicode.com/albums/{id_number}/photos'
            tasks.append(asyncio.ensure_future(get_users(client, url)))
        users = await asyncio.gather(*tasks)
        for user in users:
            print(user)


if __name__ == '__main__':
    asyncio.run(main())

end_time = time.time() - start_time
print(f'\n Execution time: {end_time} seconds')