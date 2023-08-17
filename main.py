from joblib import dump, load
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
async def hello ():
    return "Hola mundo"

