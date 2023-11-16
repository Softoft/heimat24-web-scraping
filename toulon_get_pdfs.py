import asyncio
import os
import re

import aiohttp

BASE_URL = "https://www.univ-tln.fr"


def fix_url(url):
    if is_relative_url(url):
        return convert_relative_url(url)
    else:
        return url


def is_relative_url(url):
    return "http" not in url


def convert_relative_url(relative_url):
    if relative_url[0] == "/":
        return BASE_URL + relative_url
    else:
        return BASE_URL + "/" + relative_url


def find_pdf_links(file_path):
    pattern_full_url = re.compile(r"https?://[^ ,\n]+\.pdf")
    pattern_relative_url = re.compile(r"\n([^ ,\n]*.pdf)")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        return pattern_full_url.findall(content) + pattern_relative_url.findall(content)


async def download_pdf(session, url, folder_path, retries=5, delay=1):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            file_name = url.split("/")[-1]
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, "wb") as file:
                file.write(await response.content.read())
            print(f"Downloaded: {url}")
    except Exception as e:
        if retries > 0:
            print(f"Retry {url}, attempts remaining: {retries}")
            await asyncio.sleep(delay)
            await download_pdf(session, url, folder_path, retries - 1, delay * 2)
        else:
            print(f"Failed to download {url} after several attempts: {e}")


async def main():
    file_path = "data/toulon_urls_unique.txt"
    folder_path = "data/toulon_pdf"

    pdf_links = find_pdf_links(file_path)
    fixed_links = [fix_url(url) for url in pdf_links]
    unique_urls = list(set(fixed_links))

    async with aiohttp.ClientSession(headers={"User-Agent": "Mozilla/5.0"}) as session:
        tasks = [download_pdf(session, url, folder_path) for url in unique_urls]
        for counter, task in enumerate(asyncio.as_completed(tasks), 1):
            await task
            print(f"{counter}/{len(unique_urls)}")


if __name__ == "__main__":
    asyncio.run(main())
