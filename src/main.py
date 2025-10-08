# Testing Grounds
# Playing around with async to understand it  

import asyncio
import random
import time

async def fetch_data(site):
    print(f"Fetching data from {site}")
    await asyncio.sleep(random.randint(1,5))
    print(f"Finished fetching from {site}!")

async def main():
    sites = ["example.com", "google.com", "github.com", "wikipedia.org", "reddit.com"]
    start = time.time()
    await asyncio.gather(*(fetch_data(site) for site in sites))
    end = time.time()

    print(f"Total time taken: {round(end - start, 2)} seconds")

asyncio.run(main())
    