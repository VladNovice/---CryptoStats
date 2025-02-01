import httpx

# URL API CoinGecko для получения цен
BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

async def get_crypto_price(currency: str) -> float:
    """
    Получение текущей цены криптовалюты.
    
    :param currency: Название криптовалюты (например, 'bitcoin', 'ethereum')
    :return: Текущая цена криптовалюты
    
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params={"ids": currency, "vs_currencies": "usd"})
        
        if response.status_code == 200:
            data = response.json()
            return data[currency]['usd']  # возвращаем цену в USD
        else:
            raise ValueError("Ошибка получения данных: " + response.text)
