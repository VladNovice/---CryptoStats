from fastapi import FastAPI

from services import func_get_price
#8922eb27-5656-4e9d-89ea-6a74c1234f2f

app = FastAPI()

@app.get("/price/{currency}")
async def func_get_crypto(currency: str):
    price = await func_get_price(currency)
    return {"currency": currency, "price": price}