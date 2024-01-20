from fastapi import FastAPI, status, Query
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

import aioredis

from shemas import UserData

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)


async def redis_connection():
    redis = await aioredis.from_url('redis://redis:6379/0')
    return redis


@app.post('/write_data')
async def write_data(user_data: UserData):
    phone = user_data.phone
    address = user_data.address
    redis = await redis_connection()
    await redis.set(phone, address)
    return status.HTTP_200_OK


@app.get('/check_data')
async def check_data(phone: str = Query(..., title="Phone number",
                                        regex=r"^(?:'\+?\d{11}'|\+?\d{11})$")):
    redis = await redis_connection()
    # тесткейс использует ковычки для обрамления строки
    phone = phone.strip("'\"")
    # приравнивание номеров для форматов "8..." и "+7..."
    phone = '+7' + phone[1:] if phone.startswith('8') else phone
    address = await redis.get(phone)
    return {'address': address}

