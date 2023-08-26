from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import urllib.request
import json
import os
import ssl


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if (
        allowed
        and not os.environ.get("PYTHONHTTPSVERIFY", "")
        and getattr(ssl, "_create_unverified_context", None)
    ):
        ssl._create_default_https_context = ssl._create_unverified_context


 

allowSelfSignedHttps(True)
app = FastAPI()
origins = ["*"]


class features(BaseModel):
    Nombre: str
    null: int
    almost_null: int
    basic: int
    intermediate: int
    advanced: int
    native: int
    HTML: int
    CSS: int
    SaSS: int
    JS: int
    PHP: int
    JAVA: int
    TS: int
    OtraHerramienta: int
    NingunaHerramientaWeb: int
    React: int
    Vue: int
    Angular: int
    Ember: int
    Backbone: int
    Mercury: int
    OtroFramework: int
    NingunFramework: int
    GitHub: int
    GitLab: int
    GoogleRepositories: int
    GitKraken: int
    OtroControldeVersiones: int
    NingunControldeVersiones: int
    Windows: int
    MacOS: int
    GNULinux: int
    OtroOS: int
    NingunOS: int
    Azure: int
    AWS: int
    Heroku: int
    GoogleCloud: int
    DigitalOcean: int
    OracleCloud: int
    OtraComputoNube: int
    NingunaComputoNube: int
    SaaS: int
    PaaS: int
    IaaSHaaS: int
    BaaS: int
    DaaS: int
    OtroTipoDeSoftware: int
    NingunSoftware: int
    VSCode: int
    IntelliJ: int
    PyCharm: int
    Xcode: int
    Eclipse: int
    SublimeText: int
    VIM: int
    OtroIDE: int
    NingunIDE: int
    fastapi: int
    Falcon: int
    Eve: int
    Hug: int
    Webpy: int
    Flask: int
    OtraAPI: int
    NigunaAPI: int
    JavaScript: int
    Python: int
    PHPConsumo: int
    JavaConsumo: int
    Ruby: int
    C: int
    OtraConsumo: int
    NingunaConsumo: int
    JSON: int
    XML: int
    HTMLInfo: int
    CSV: int
    RSS: int
    OtroFormato: int
    NingunFormto: int
    VariablesEntorno: int
    Scrum: int
    Kanban: int
    XP: int
    Agile: int
    Desing: int
    OtraMAgil: int
    NingunaMAgil: int
    Cascada: int
    Prototipado: int
    Espiral: int
    Incremental: int
    DiseñoRapido: int
    OtraMTradicional: int
    NingunaMTradicional: int


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello():
    return "Hola mundo"


@app.post("/prediction/")
async def predictValue(features: features):
    try:
        values = [
            {
                "Nombre": features.Nombre,
                "null": features.null,
                "almost_null": features.almost_null,
                "intermediate": features.intermediate,
                "basic": features.basic,
                "advanced": features.advanced,
                "native": features.native,
                "HTML": features.HTML,
                "CSS": features.CSS,
                "SaSS": features.SaSS,
                "JS": features.JS,
                "PHP": features.PHP,
                "JAVA": features.JAVA,
                "TS": features.TS,
                "OtraHerramienta": features.OtraHerramienta,
                "NingunaHerramientaWeb": features.NingunaHerramientaWeb,
                "React": features.React,
                "Vue": features.Vue,
                "Angular": features.Angular,
                "Ember": features.Ember,
                "Backbone": features.Backbone,
                "Mercury": features.Mercury,
                "OtroFramework": features.OtroFramework,
                "NingunFramework": features.NingunFramework,
                "GitHub": features.GitHub,
                "GitLab": features.GitLab,
                "Google Cloud Sorse Repositories": features.GoogleRepositories,
                "GitKraken": features.GitKraken,
                "OtroControldeVerciones": features.OtroControldeVersiones,
                "NingunControldeVerciones": features.NingunControldeVersiones,
                "Windows": features.Windows,
                "MacOS": features.MacOS,
                "GNULinux": features.GNULinux,
                "Otro": features.OtroOS,
                "NingunOS": features.NingunOS,
                "Azure": features.Azure,
                "AWS": features.AWS,
                "Heroku": features.Heroku,
                "GoogleCloud": features.GoogleCloud,
                "Digital Ocean": features.DigitalOcean,
                "Oracle Cloud": features.OracleCloud,
                "OtraComputoNube": features.OtraComputoNube,
                "NingunaComputoNube": features.NingunaComputoNube,
                "SaaS": features.SaaS,
                "PaaS": features.PaaS,
                "IaaS/HaaS": features.IaaSHaaS,
                "BaaS": features.BaaS,
                "DaaS": features.DaaS,
                "OtroTipoDeSoftware": features.OtroTipoDeSoftware,
                "NingunSoftware": features.NingunSoftware,
                "VSCode": features.VSCode,
                "IntelliJ Idea": features.IntelliJ,
                "PyCharm": features.PyCharm,
                "Xcode": features.Xcode,
                "Eclipse": features.Eclipse,
                "Sublime Text": features.SublimeText,
                "VIM": features.VIM,
                "OtroIDE": features.OtroIDE,
                "NingunIDE": features.NingunIDE,
                "FastAPI": features.fastapi,
                "Falcon": features.Falcon,
                "Eve": features.Eve,
                "Hug": features.Hug,
                "Web.py": features.Webpy,
                "Flask": features.Flask,
                "OtraAPI": features.OtraAPI,
                "NigunaAPI": features.NigunaAPI,
                "JavaScript": features.JavaScript,
                "Python": features.Python,
                "PHPConsumo": features.PHPConsumo,
                "JavaConsumo": features.JavaConsumo,
                "Ruby": features.Ruby,
                "C#": features.C,
                "OtraConsumo": features.OtraConsumo,
                "NingunaConsumo": features.NingunaConsumo,
                "JSON": features.JSON,
                "XML": features.XML,
                "HTMLInfo": features.HTMLInfo,
                "CSV": features.CSV,
                "RSS": features.RSS,
                "OtroFormato": features.OtroFormato,
                "Ningun Formto": features.NingunFormto,
                "VariablesEntorno": features.VariablesEntorno,
                "Scrum": features.Scrum,
                "Kanban": features.Kanban,
                "XP": features.XP,
                "Agile Inseption": features.Agile,
                "Desing Spring": features.Desing,
                "OtraMAgil": features.OtraMAgil,
                "NingunaMAgil": features.NingunaMAgil,
                "Cascada": features.Cascada,
                "Prototipado": features.Prototipado,
                "Espiral": features.Espiral,
                "Incremental": features.Incremental,
                "Diseño Rapido": features.DiseñoRapido,
                "OtraMTradicional": features.OtraMTradicional,
                "NingunaMTradicional": features.NingunaMTradicional,
            }
        ]

        data = {
            "Inputs": {"data": values},
            "GlobalParameters": 1.0,
        }
        body = str.encode(json.dumps(data))
        url = "https://machile-leatning-studio-iosuk.southcentralus.inference.ml.azure.com/score"
        # Replace this with the primary/secondary key or AMLToken for the endpoint
        api_key = "w8UFfl5TS4DlbrOKYweXc2sz83iINuYe"
        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")
        headers = {
            "Content-Type": "application/json",
            "Authorization": ("Bearer " + api_key),
            "azureml-model-deployment": "automl8ca357b353-1",
        }
        req = urllib.request.Request(url, body, headers)
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result)
        result = result["Results"]
        result = result[0]
        return result
    except Exception as e:
        print(e)
