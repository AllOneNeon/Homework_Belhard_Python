import asyncio
import aiohttp
from asyncio import tasks
from pip import main
import httpx
import time

tasks = []


##########
async def main(url_list):    
    for n in url_list:
        tasks.append(asyncio.create_task((n)))
    print (tasks)
    return await asyncio.gather(*tasks)
urls = ['https://jsonplaceholder.typicode.com/users/{id}/posts', 
        'https://jsonplaceholder.typicode.com/users/{id}/todos',
        'https://jsonplaceholder.typicode.com/users/{id}/albums',
        'https://jsonplaceholder.typicode.com/posts/{id}/comments',
        'https://jsonplaceholder.typicode.com/albums/{id}/photos']
loop = asyncio.get_event_loop()
results = loop.run_until_complete(main(urls))
print (results)