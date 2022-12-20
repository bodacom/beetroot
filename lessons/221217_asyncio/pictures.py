import requests
import threading
import datetime

# https://picsum.photos/

user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/89.0.4389.72 Safari/537.36'}

session = requests.Session()
session.headers.update(user_agent)


def picture_downloader(num_of_pictures: int) -> None:
    thread_name = threading.current_thread().getName()
    for i in range(num_of_pictures):
        response = session.get("https://picsum.photos/200", allow_redirects = True, stream = True)
        with open(f"downloaded_images/{thread_name}_image_{i}.jpg", "wb") as picture:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    picture.write(chunk)
        print(f"{thread_name}: Download {i + 1} pictures out of {num_of_pictures}")


thread_1 = threading.Thread(target = picture_downloader, args = (10,), name = "thread-1")
thread_2 = threading.Thread(target = picture_downloader, args = (10,), name = "thread-2")

time_s = datetime.datetime.now()

thread_1.start()
thread_2.start()

time_f = datetime.datetime.now()

thread_1.join()
thread_2.join()

print("Time execution", time_f - time_s)


import requests
import threading
import time
import asyncio
import aiohttp
import datetime
import random


def save_image(data):
    with open(f"image_{random.randint(1, 1000)}.jpg", "wb") as picture:
        for chunk in data.iter_content(chunk_size=1024):
            if chunk:
                picture.write(chunk)


async def get_picture(url: str, session) -> None:
    async with session.get(url, allow_redirects=True) as response:

        data = await response.read()
        save_image(data)


async def main():
    url = "https://picsum.photos/200"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(get_picture(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

s = time.perf_counter()
asyncio.run(main())
print(time.perf_counter() - s)
