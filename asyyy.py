import httpx
import asyncio

async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)

urls = ["https://jsonplaceholder.typicode.com/users",
 "https://jsonplaceholder.typicode.com/users/posts",
 "https://jsonplaceholder.typicode.com/users/todos"]

async def launch():
    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp.text for resp in resps]
    
    for html in data:
        print(html)

asyncio.run(launch())