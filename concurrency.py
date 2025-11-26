import asyncio
import time
async def toast_bagel(type, delay):
    print(f'Started toasting bagel {type}')
    await asyncio.sleep(delay)
    print('Bagel is toasted')

async def brew_coffee(type, delay):
    print(f'Started brewing {type} coffee')
    await asyncio.sleep(delay)
    print('Coffee is brewed')


async def runner():
    start = time.time()
    tasks = await asyncio.gather(toast_bagel("cream cheeese", 5), brew_coffee("cortado", 2))
    end = time.time()
    print(f'Total time it took was : {end-start}s')

if __name__=="__main__":
    asyncio.run(runner())
