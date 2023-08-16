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
    + "{name}/{email}/{null}/{almost_null}/{basic}/{intermediate}/{advanced}/{native}/"
    + "{HTML}/{CSS}/{SaSS}/{JS}/{PHP}/{JAVA}/{TS}/{OtraHerramienta}/{NingunaHerramientaWeb}/"
    + "{React}/{Vue}/{Angular}/{Ember}/{Backbone}/{Mercury}/{OtroFramework}/{NingunFramework}/"
    + "{GitHub}/{GitLab}/{Google Cloud Sorse Repositories}/{GitKraken}/{OtroControldeVerciones}/{NingunControldeVerciones}/"+"{Windows}/{MacOS}/{GNULinux}/{Otro}/{NingunOS}/"
    +"{Azure}/{AWS}/{Heroku}/{GoogleCloud}/{Digital Ocean}/{Oracle Cloud}/{OtraComputoNube}/{NingunaComputoNube}/"
    +"{SaaS}/{PaaS}/{IaaS}/{BaaS}/{DaaS}/{OtroTipoDeSoftware}/{NingunSoftware}/" 
    + "{VSCode}/{IntelliJ Idea}/{PyCharm}/{Xcode}/{Eclipse}/{Sublime Text}/{VIM}/{OtroIDE}/{NingunIDE}" 
    + "{FastAPI}/{Falcon}/{Eve}{Hug}/{Web.py}/{Flask}/{OtraAPI}/{NigunaAPI}/"
    + "{JavaScript}/{Python}/{PHPConsumo}/{JavaConsumo}/{Ruby}/{C#}/{OtraConsumo}/{NingunaConsumo}/"
    +"{JSON}/{XML}/{HTMLInfo}/{CSV}/{RSS}/{OtroFormato}/{Ningun Formto}/"
    +"{VariablesEntorno}/"
    +"{Scrum}/{Kanban}/{XP}/{Agile}/{Inseption}/{Desing Spring}/{OtraMAgil}/{NingunaMAgil}/"
    +"{Cascada}/{Prototipado]/{Espiral}/{Incremental}/{Diseño Rapido/{OtraMTradicional}/{NingunaMTradicional}"
)
async def postPrediction():
    return "hola"
