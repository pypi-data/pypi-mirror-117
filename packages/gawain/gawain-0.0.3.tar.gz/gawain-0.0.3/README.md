# Gawain
Booru armor wrapper

```py
import asyncio
import gawain

async def gel():
    data = gawain.Load()
    print(data.search(tags="milf", limit=25, pid=1, block="shota"))


async def main():
    get = [ gel()]
    await asyncio.gather(*get)

asyncio.run(main())
```