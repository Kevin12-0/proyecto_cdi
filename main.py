from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
import os

modelPredictive = os.path.join("files/model.joblib")

app = FastAPI()

origins = ["*"]
class PredictionInput(BaseModel):
    null: int,
    almost_null: int,
    basic: int,
    intermediate: int,
    advanced: int,
    native: int,
    HTML: int,
    CSS: int,
    SaSS: int,
    JS: int,
    PHP: int,
    JAVA: int,
    TS: int,
    OtraHerramienta: int,
    NingunaHerramientaWeb: int,
    React: int,
    Vue: int,
    Angular: int,
    Ember: int,
    Backbone: int,
    Mercury: int,
    OtroFramework: int,
    NingunFramework: int,
    GitHub: int
    GitLab: int
    GoogleCloudSorseRepositories: int
    GitKraken: int
    OtroControldeVerciones: int
    NingunControldeVerciones: int
    Windows: int
    MacOS: int
    GNULinux: int
    Otro: int
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
    IaaS: int
    BaaS: int
    DaaS: int
    OtroTipoDeSoftware: int
    NingunSoftware: int
    VSCode: int
    IntelliJIdea: int
    PyCharm: int
    Xcode: int
    Eclipse: int
    SublimeText: int
    VIM: int
    OtroIDE: int
    NingunIDE: int
    FastAPI: int
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
    Inseption: int
    DesingSpring: int
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
async def get_hello_world():
    return {"hello": "world"}


@app.post(
    "/prediction/{null}/{almost_null}/{basic}/{intermediate}/{advanced}/{native}/{HTML}/{CSS}/{SaSS}/{JS}/{PHP}/{JAVA}/{TS}/{OtraHerramienta}/{NingunaHerramientaWeb}/{React}/{Vue}/{Angular}/{Ember}/{Backbone}/{Mercury}/{OtroFramework}/{NingunFramework}/{GitHub}/{GitLab}/{GoogleCloudSorseRepositories}/{GitKraken}/{OtroControldeVerciones}/{NingunControldeVerciones}/{Windows}/{MacOS}/{GNULinux}/{Otro}/{NingunOS}/{Azure}/{AWS}/{Heroku}/{GoogleCloud}/{DigitalOcean}/{OracleCloud}/{OtraComputoNube}/{NingunaComputoNube}/{SaaS}/{PaaS}/{IaaS}/{BaaS}/{DaaS}/{OtroTipoDeSoftware}/{NingunSoftware}/{VSCode}/{IntelliJIdea}/{PyCharm}/{Xcode}/{Eclipse}/{SublimeText}/{VIM}/{OtroIDE}/{NingunIDE}{FastAPI}/{Falcon}/{Eve}{Hug}/{Webpy}/{Flask}/{OtraAPI}/{NigunaAPI}/{JavaScript}/{Python}/{PHPConsumo}/{JavaConsumo}/{Ruby}/{C}/{OtraConsumo}/{NingunaConsumo}/{JSON}/{XML}/{HTMLInfo}/{CSV}/{RSS}/{OtroFormato}/{NingunFormto}/{VariablesEntorno}/{Scrum}/{Kanban}/{XP}/{Agile}/{Inseption}/{DesingSpring}/{OtraMAgil}/{NingunaMAgil}/{Cascada}/{Prototipado}/{Espiral}/{Incremental}/{DiseñoRapido}/{OtraMTradicional}/{NingunaMTradicional}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Get a user",
    description="Get a user",
    tags=["auth"],
)
async def postPrediction():
    data = [
        null,
        almost_null,
        basic,
        intermediate,
        advanced,
        native,
        HTML,
        CSS,
        SaSS,
        JS,
        PHP,
        JAVA,
        TS,
        OtraHerramienta,
        NingunaHerramientaWeb,
        React,
        Vue,
        Angular,
        Ember,
        Backbone,
        Mercury,
        OtroFramework,
        NingunFramework,
        GitHub,
        GitLab,
        GoogleCloudSorseRepositories,
        GitKraken,
        OtroControldeVerciones,
        NingunControldeVerciones,
        Windows,
        MacOS,
        GNULinux,
        Otro,
        NingunOS,
        Azure,
        AWS,
        Heroku,
        GoogleCloud,
        DigitalOcean,
        OracleCloud,
        OtraComputoNube,
        NingunaComputoNube,
        SaaS,
        PaaS,
        IaaS,
        BaaS,
        DaaS,
        OtroTipoDeSoftware,
        NingunSoftware,
        VSCode,
        IntelliJIdea,
        PyCharm,
        Xcode,
        Eclipse,
        SublimeText,
        VIM,
        OtroIDE,
        NingunIDE,
        FastAPI,
        Falcon,
        Eve,
        Hug,
        Webpy,
        Flask,
        OtraAPI,
        NigunaAPI,
        JavaScript,
        Python,
        PHPConsumo,
        JavaConsumo,
        Ruby,
        C,
        OtraConsumo,
        NingunaConsumo,
        JSON,
        XML,
        HTMLInfo,
        CSV,
        RSS,
        OtroFormato,
        NingunFormto,
        VariablesEntorno,
        Scrum,
        Kanban,
        XP,
        Agile,
        Inseption,
        DesingSpring,
        OtraMAgil,
        NingunaMAgil,
        Cascada,
        Prototipado,
        Espiral,
        Incremental,
        DiseñoRapido,
        OtraMTradicional,
        NingunaMTradicional,
    ]
    model = load("model.joblib")
    prediction = model.predict([data])
    response = {"Probabilidad de ser contratado": prediction[0]}
    print(data)
    return response
