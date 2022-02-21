import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/')
        print(response)
    await asyncio.gather(*response)

asyncio.run(main())




#https://jsonplaceholder.typicode.com/