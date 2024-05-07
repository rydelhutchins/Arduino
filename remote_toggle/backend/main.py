from fastapi import FastAPI
from database import database
from contextlib import asynccontextmanager

@asynccontextmanager
async def app_lifespan(app):
    await database.connect()
    print("Database connected.")
    try:
        yield 
    finally:
        await database.disconnect()
        print("Database disconnected.")

app = FastAPI(lifespan=app_lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}