import asyncio
import aiohttp

async def api_call(url):
    response = await aiohttp.get(url)
    print('finished {}'.format(url))
    result = await response.text()
    print(result)

async def main(urls):
    await asyncio.wait([api_call(url) for url in urls])

if __name__ == '__main__':
    urls = [
        'https://httpbin.org/delay/3',  # long request
        'https://httpbin.org/delay/1',  # short request
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
