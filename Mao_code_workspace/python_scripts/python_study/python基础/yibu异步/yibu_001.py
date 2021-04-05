import asyncio

async def hello():
    print('begin...')
    r=await asyncio.sleep(1)
    print('end...')

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
