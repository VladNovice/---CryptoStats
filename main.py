from fastapi import FastAPI
from services import get_crypto_price

app = FastAPI()

@app.get("/price/{currency}")
async def get_crypto(currency: str):
    price = await get_crypto_price(currency)
    return {"currency": currency, "price": price}
