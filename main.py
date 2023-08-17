from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
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


class Config:
    data = [
        {
            "Nombre": "example_value",
            "null": 0,
            "almost_null": 0,
            "basic": 0,
            "intermediate": 0,
            "advanced": 0,
            "native": 0,
            "HTML": 0,
            "CSS": 0,
            "SaSS": 0,
            "JS": 0,
            "PHP": 0,
            "JAVA": 0,
            "TS": 0,
            "OtraHerramienta": 0,
            "NingunaHerramientaWeb": 0,
            "React": 0,
            "Vue": 0,
            "Angular": 0,
            "Ember": 0,
            "Backbone": 0,
            "Mercury": 0,
            "OtroFramework": 0,
            "NingunFramework": 0,
            "GitHub": 0,
            "GitLab": 0,
            "Google Cloud Sorse Repositories": 0,
            "GitKraken": 0,
            "OtroControldeVerciones": 0,
            "NingunControldeVerciones": 0,
            "Windows": 0,
            "MacOS": 0,
            "GNULinux": 0,
            "Otro": 0,
            "NingunOS": 0,
            "Azure": 0,
            "AWS": 0,
            "Heroku": 0,
            "GoogleCloud": 0,
            "Digital Ocean": 0,
            "Oracle Cloud": 0,
            "OtraComputoNube": 0,
            "NingunaComputoNube": 0,
            "SaaS": 0,
            "PaaS": 0,
            "IaaS/HaaS": 0,
            "BaaS": 0,
            "DaaS": 0,
            "OtroTipoDeSoftware": 0,
            "NingunSoftware": 0,
            "VSCode": 0,
            "IntelliJ Idea": 0,
            "PyCharm": 0,
            "Xcode": 0,
            "Eclipse": 0,
            "Sublime Text": 0,
            "VIM": 0,
            "OtroIDE": 0,
            "NingunIDE": 0,
            "FastAPI": 0,
            "Falcon": 0,
            "Eve": 0,
            "Hug": 0,
            "Web.py": 0,
            "Flask": 0,
            "OtraAPI": 0,
            "NigunaAPI": 0,
            "JavaScript": 0,
            "Python": 0,
            "PHPConsumo": 0,
            "JavaConsumo": 0,
            "Ruby": 0,
            "C#": 0,
            "OtraConsumo": 0,
            "NingunaConsumo": 0,
            "JSON": 0,
            "XML": 0,
            "HTMLInfo": 0,
            "CSV": 0,
            "RSS": 0,
            "OtroFormato": 0,
            "Ningun Formto": 0,
            "VariablesEntorno": 0,
            "Scrum": 0,
            "Kanban": 0,
            "XP": 0,
            "Agile Inseption": 0,
            "Desing Spring": 0,
            "OtraMAgil": 0,
            "NingunaMAgil": 0,
            "Cascada": 0,
            "Prototipado": 0,
            "Espiral": 0,
            "Incremental": 0,
            "Diseño Rapido": 0,
            "OtraMTradicional": 0,
            "NingunaMTradicional": 0,
        }
    ]


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
async def predictValue():
    values = [
            features.null,
            features.almost_null,
            features.basic,
            features.intermediate,
            features.advanced,
            features.native,
            features.HTML,
            features.CSS,
            features.SaSS,
            features.JS,
            features.PHP,
            features.JAVA,
            features.TS,
            features.OtraHerramienta,
            features.NingunaHerramientaWeb,
            features.React,
            features.Vue,
            features.Angular,
            features.Ember,
            features.Backbone,
            features.Mercury,
            features.OtroFramework,
            features.NingunFramework,
            features.GitHub,
            features.GitLab,
            features.GoogleRepositories,
            features.GitKraken,
            features.OtroControldeVersiones,	
            features.NingunControldeVersiones,	
            features.Windows,	
            features.MacOS,	
            features.GNULinux,	
            features.OtroOS,	
            features.NingunOS,
            features.Azure,	
            features.AWS,	
            features.Heroku,	
            features.GoogleCloud,	
            features.DigitalOcean,	
            features.OracleCloud,	
            features.OtraComputoNube,	
            features.NingunaComputoNube,
            features.SaaS,	
            features.PaaS,	
            features.IaaSHaaS,	
            features.BaaS,	
            features.DaaS,	
            features.OtroTipoDeSoftware,	
            features.NingunSoftware,
            features.VSCode,	
            features.IntelliJ, 
            features.PyCharm,	
            features.Xcode,	
            features.Eclipse,	
            features.SublimeText,	
            features.VIM,	
            features.OtroIDE,	
            features.NingunIDE,	
            features.fastapi,
            features.Falcon,	
            features.Eve,	
            features.Hug,	
            features.Webpy,	
            features.Flask	,
            features.OtraAPI,	
            features.NigunaAPI,	
            features.JavaScript,	
            features.Python,	
            features.PHPConsumo,	
            features.JavaConsumo,	
            features.Ruby,	
            features.C	,
            features.OtraConsumo,	
            features.NingunaConsumo,	
            features.JSON,	
            features.XML,	
            features.HTMLInfo,	
            features.CSV,	
            features.RSS,	
            features.OtroFormato,	
            features.NingunFormto,	
            features.VariablesEntorno,	
            features.Scrum	,
            features.Kanban,	
            features.XP,	
            features.Agile, 
            features.Desing ,
            features.OtraMAgil	,
            features.NingunaMAgil,	
            features.Cascada	,
            features.Prototipado,	
            features.Espiral,	
            features.Incremental,	
            features.DiseñoRapido,
            features.OtraMTradicional,	
            features.NingunaMTradicional
        ]
    data = {
        "Inputs": {values},
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
    return result
