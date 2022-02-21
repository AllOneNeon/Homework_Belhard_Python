import asyncio
from pip import main
import time
import httpx

httpx_url = 'https://jsonplaceholder.typicode.com/'



async def get_users(url):
    print(f's{url}')
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        print(resp.status_code)
    print(f'end {url}')

async def main(): # coroutine
    print('start main')
    #await wait(belhard_url)
    #await wait(httpx_url)
    await asyncio.gather(
            get_users(httpx_url)
        )
    print('finish main')

if __name__=='__main__':
    start = time.time()
    asyncio.run(main())
    print('Timing', time.time() - start)



