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
    pass