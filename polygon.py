import pandas as pd
import requests
import polygon
import asyncio

async def main():
    api_key = "c1LVL_w5bcBEXIfWB_jEPqyDJGirPl3Q"

    stocks_client = polygon.StocksClient(api_key, True)

    previous_close = await stocks_client.get_previous_close("AMD")

    await stocks_client.close()

    print(previous_close)

if __name__ == '__main__':
    asyncio.run(main())