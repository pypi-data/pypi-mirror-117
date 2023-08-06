import asyncio
import sys
import os

filepath = os.path.split(__file__)[0]
sys.path.append(".")


from l0n0lutils.async_runner import async_runner


async def task_test():
    await asyncio.sleep(3)
    print("closed")

def on_close():
    print("xxxxxx")

loop = asyncio.get_event_loop()
r = async_runner(loop)
r.on_close_function(on_close)
loop.create_task(task_test())
r.run_forever()

