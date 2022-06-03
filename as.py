import asyncio
from asyncio import tasks
import httpx
import time
import json

start_time = time.time()
all_data = []

async def users():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://jsonplaceholder.typicode.com/users')
        print(r.text)

async def post():
    async with httpx.AsyncClient() as client:

            url = await client.get('https://jsonplaceholder.typicode.com/users/{id}posts')
            users = post()
            asyncio.gather(*[post(users)])
            

asyncio.run(users())
asyncio.run(post())

end_time = time.time() - start_time
print(f'\n Execution time: {end_time} seconds')