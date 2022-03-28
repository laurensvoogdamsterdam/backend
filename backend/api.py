from fastapi import FastAPI

api = FastAPI(title="Dev")


@api.get("/")
async def read_root():
    return {"Hello": "ok"}
