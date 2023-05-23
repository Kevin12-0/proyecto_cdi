from fastapi.middleware.cors import CORSMiddleware
from fastapi import *
from typing import List
from typing import Union

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/children")
async def get_children():
    return {"Esto es": "una prueba"}
