from os import name

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.sql.functions import user

from backend.auth import authentication
from backend.db import models
from backend.db.database import engine
from backend.routers import comment, post, user

description = """
Backend API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).

## Posts

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).

## Comments

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""


api = FastAPI(
    title="Backend API - Starter",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


api.include_router(user.router)
api.include_router(post.router)
api.include_router(comment.router)
api.include_router(authentication.router)


@api.get("/")
async def read_root():
    return {"Hello": "ok"}


origins = ["http://localhost:3000", "http://localhost:3001", "http://localhost:3002"]

api.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(engine)

api.mount("/images", StaticFiles(directory="./backend/images"), name="images")
