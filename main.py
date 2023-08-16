from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load
from fastapi.middleware.cors import CORSMiddleware

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
async def get_hello_world():
    return {"hello": "world"}


@app.post(
    "/prediction/"
    + "{name}/{email}/{null}/{almost_null}/{basic}/{intermediate}/{advanced}/{native}"
)
async def postPrediction():
    pass
