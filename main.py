import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from joblib import dump, load
from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load
from fastapi.middleware.cors import CORSMiddleware


class Features(BaseModel):
    null: float
    almost_null: float
    basic: float
    intermediate: float
    advanced: float
    native: float
    HTML: float
    CSS: float
    SaSS: float
    JS: float
    PHP: float
    JAVA: float
    TS: float
    OtraHerramienta: float
    NingunaHerramientaWeb: float
    React: float
    Vue: float
    Angular: float
    Ember: float
    Backbone: float
    Mercury: float
    OtroFramework: float
    NingunFramework: float
    GitHub: float
    GitLab: float
    GoogleRepositories: float
    GitKraken: float
    OtroControldeVersiones: float
    NingunControldeVersiones: float
    Windows: float
    MacOS: float
    GNULinux: float
    OtroOS: float
    NingunOS: float
    Azure: float
    AWS: float
    Heroku: float
    GoogleCloud: float
    DigitalOcean: float
    OracleCloud: float
    OtraComputoNube: float
    NingunaComputoNube: float
    SaaS: float
    PaaS: float
    IaaSHaaS: float
    BaaS: float
    DaaS: float
    OtroTipoDeSoftware: float
    NingunSoftware: float
    VSCode: float
    IntelliJ: float
    PyCharm: float
    Xcode: float
    Eclipse: float
    SublimeText: float
    VIM: float
    OtroIDE: float
    NingunIDE: float
    fastapi: float
    Falcon: float
    Eve: float
    Hug: float
    Webpy: float
    Flask: float
    OtraAPI: float
    NigunaAPI: float
    JavaScript: float
    Python: float
    PHPConsumo: float
    JavaConsumo: float
    Ruby: float
    C: float
    OtraConsumo: float
    NingunaConsumo: float
    JSON: float
    XML: float
    HTMLInfo: float
    CSV: float
    RSS: float
    OtroFormato: float
    NingunFormto: float
    VariablesEntorno: float
    Scrum: float
    Kanban: float
    XP: float
    Agile: float
    Desing: float
    OtraMAgil: float
    NingunaMAgil: float
    Cascada: float
    Prototipado: float
    Espiral: float
    Incremental: float
    DiseñoRapido: float
    OtraMTradicional: float
    NingunaMTradicional: float

    class Config:
        schema_extra = {
            "example": {
                "null": 0.0,
                "almost_null": 0.0,
                "basic": 0.0,
                "intermediate": 0.0,
                "advanced": 0.0,
                "native": 0.0,
                "HTML": 0.0,
                "CSS": 0.0,
                "SaSS": 0.0,
                "JS": 0.0,
                "PHP": 0.0,
                "JAVA": 0.0,
                "TS": 0.0,
                "OtraHerramienta": 0.0,
                "NingunaHerramientaWeb": 0.0,
                "React": 0.0,
                "Vue": 0.0,
                "Angular": 0.0,
                "Ember": 0.0,
                "Backbone": 0.0,
                "Mercury": 0.0,
                "OtroFramework": 0.0,
                "NingunFramework": 0.0,
                "GitHub": 0.0,
                "GitLab": 0.0,
                "GoogleRepositories": 0.0,
                "GitKraken": 0.0,
                "OtroControldeVersiones": 0.0,
                "NingunControldeVersiones": 0.0,
                "Windows": 0.0,
                "MacOS": 0.0,
                "GNULinux": 0.0,
                "OtroOS": 0.0,
                "NingunOS": 0.0,
                "Azure": 0.0,
                "AWS": 0.0,
                "Heroku": 0.0,
                "GoogleCloud": 0.0,
                "DigitalOcean": 0.0,
                "OracleCloud": 0.0,
                "OtraComputoNube": 1.0,
                "NingunaComputoNube": 0.0,
                "SaaS": 0.0,
                "PaaS": 1.0,
                "IaaSHaaS": 0.0,
                "BaaS": 0.0,
                "DaaS": 0.0,
                "OtroTipoDeSoftware": 0.0,
                "NingunSoftware": 0.0,
                "VSCode": 1.0,
                "IntelliJ": 0.0,
                "PyCharm": 0.0,
                "Xcode": 0.0,
                "Eclipse": 0.0,
                "SublimeText": 0.0,
                "VIM": 0.0,
                "OtroIDE": 0.0,
                "NingunIDE": 0.0,
                "fastapi": 0.0,
                "Falcon": 0.0,
                "Eve": 0.0,
                "Hug": 1,
                "Webpy": 0.0,
                "Flask": 0.0,
                "OtraAPI": 0.0,
                "NigunaAPI": 0.0,
                "JavaScript": 0.0,
                "Python": 0.0,
                "PHPConsumo": 0.0,
                "JavaConsumo": 0.0,
                "Ruby": 0.0,
                "C": 0.0,
                "OtraConsumo": 0.0,
                "NingunaConsumo": 0.0,
                "JSON": 1.0,
                "XML": 0.0,
                "HTMLInfo": 0.0,
                "CSV": 0.0,
                "RSS": 0.0,
                "OtroFormato": 0.0,
                "NingunFormto": 0.0,
                "VariablesEntorno": 0.0,
                "Scrum": 0.0,
                "Kanban": 0.0,
                "XP": 0.0,
                "Agile": 0.0,
                "Desing": 0.0,
                "OtraMAgil": 0.0,
                "NingunaMAgil": 0.0,
                "Cascada": 0.0,
                "Prototipado": 0.0,
                "Espiral": 0.0,
                "Incremental": 0.0,
                "DiseñoRapido": 0.0,
                "OtraMTradicional": 0.0,
                "NingunaMTradicional": 0.0,
            }
        }


class Label(BaseModel):
    hiring: float


class message(BaseModel):
    message: float


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


