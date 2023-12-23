import asyncio
import time

import aiohttp
import requests

resources = [
    {
        "resource": "user profile",
        "url": 'http://3.208.12.242:8012/users/1/profile'
    },
    {
        "resource": "discussions",
        "url": 'http://44.211.253.211:8013/discussions/liutianshu0307@gmail.com'
    }
]

async def fetch(session, resource):
    url = resource["url"]
    print("Calling URL = ", url)
    async with session.get(url) as response:
        t = await response.text()
        print("Responsed URL = ", url, "    Content: ", t[0:15])
        result = {
            "resource": resource["resource"]
        }
    return result

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch(session, res)) for res in resources]
        await asyncio.gather(*tasks)
def synch_main():
    for r in resources:
        print("Calling URL = ", r["url"])
        t = requests.get(r["url"])
        print("Responded URL = ", r["url"])


if __name__ == '__main__':
    for i in range(10):
        print("************************************", i+1, "************************************")
        time1 = time.time()
        print("* begin asynchronous call")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        time2 = time.time()
        print("* begin synchronous call")
        synch_main()
        time3 = time.time()
        print("asynchronous call time : ", time2 - time1)
        print("synchronous call time : ", time3 - time2)