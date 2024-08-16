import asyncio
import time
from definitely import asyncily


# You can use this as a decorator like so:
@asyncily
def buy_stuff(item: str):
    print("dad is going out!")
    time.sleep(2)
    print("came back with the %s!" % item)


async def main():
    await buy_stuff("milk")


asyncio.run(main())
