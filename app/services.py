import httpx 


async def func_get_price(currency: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={currency}&vs_currencies=usd"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            return data[currency]['usd']
        except (httpx.HTTPStatusError, KeyError):
            return None