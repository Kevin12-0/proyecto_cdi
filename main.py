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


class Features(BaseModel):
    nombre: str
    correo: str
    number: int

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
        schema_extra = {
            "example": {
                "nombre": "ApellidoPaterno ApellidoMaterno Nombres",
                "correo": "example@email.com",
                "number": 0,
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
                "GoogleRepositories": 0,
                "GitKraken": 0,
                "OtroControldeVersiones": 0,
                "NingunControldeVersiones": 0,
                "Windows": 0,
                "MacOS": 0,
                "GNULinux": 0,
                "OtroOS": 0,
                "NingunOS": 0,
                "Azure": 0,
                "AWS": 0,
                "Heroku": 0,
                "GoogleCloud": 0,
                "DigitalOcean": 0,
                "OracleCloud": 0,
                "OtraComputoNube": 0,
                "NingunaComputoNube": 0,
                "SaaS": 0,
                "PaaS": 0,
                "IaaSHaaS": 0,
                "BaaS": 0,
                "DaaS": 0,
                "OtroTipoDeSoftware": 0,
                "NingunSoftware": 0,
                "VSCode": 0,
                "IntelliJ": 0,
                "PyCharm": 0,
                "Xcode": 0,
                "Eclipse": 0,
                "SublimeText": 0,
                "VIM": 0,
                "OtroIDE": 0,
                "NingunIDE": 0,
                "fastapi": 0,
                "Falcon": 0,
                "Eve": 0,
                "Hug": 0,
                "Webpy": 0,
                "Flask": 0,
                "OtraAPI": 0,
                "NigunaAPI": 0,
                "JavaScript": 0,
                "Python": 0,
                "PHPConsumo": 0,
                "JavaConsumo": 0,
                "Ruby": 0,
                "C": 0,
                "OtraConsumo": 0,
                "NingunaConsumo": 0,
                "JSON": 0,
                "XML": 0,
                "HTMLInfo": 0,
                "CSV": 0,
                "RSS": 0,
                "OtroFormato": 0,
                "NingunFormto": 0,
                "VariablesEntorno": 0,
                "Scrum": 0,
                "Kanban": 0,
                "XP": 0,
                "Agile": 0,
                "Desing": 0,
                "OtraMAgil": 0,
                "NingunaMAgil": 0,
                "Cascada": 0,
                "Prototipado": 0,
                "Espiral": 0,
                "Incremental": 0,
                "DiseñoRapido": 0,
                "OtraMTradicional": 0,
                "NingunaMTradicional": 0,
            }
        }


class Label(BaseModel):
    hiring: float


class message(BaseModel):
    message: float


app = FastAPI()


@app.post(
    "/hiring/",
    response_model=Label,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Predecir la probabilidad de ser contratado",
    description="Predecir la probabilidad de ser contratado",
    tags={"Predictive hiring model"},
)
async def get_hiring(features: Features):
    try:
        model = load("model.joblib")
        data = [
            features.nombre,
            features.correo,
            features.number,
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
            features.Flask,
            features.OtraAPI,
            features.NigunaAPI,
            features.JavaScript,
            features.Python,
            features.PHPConsumo,
            features.JavaConsumo,
            features.Ruby,
            features.C,
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
            features.Scrum,
            features.Kanban,
            features.XP,
            features.Agile,
            features.Desing,
            features.OtraMAgil,
            features.NingunaMAgil,
            features.Cascada,
            features.Prototipado,
            features.Espiral,
            features.Incremental,
            features.DiseñoRapido,
            features.OtraMTradicional,
            features.NingunaMTradicional,
        ]
        predictions = model.predict([data])
        # conexionBaseDatos(data,predictions[0])
        response = {"hiring": predictions[0]}
        return response
    except Exception as e:
        response = JSONResponse(
            status_code=400,
            content={"message": f"{e.args}"},
        )
        return response


hiring_model = pd.read_csv("works_oferts.csv")
# print(hiring_model)
X = hiring_model[
    [
        "null",
        "almost_null",
        "basic",
        "intermediate",
        "advanced",
        "native",
        "HTML",
        "CSS",
        "SaSS",
        "JS",
        "PHP",
        "JAVA",
        "TS",
        "OtraHerramienta",
        "NingunaHerramientaWeb",
        "React",
        "Vue",
        "Angular",
        "Ember",
        "Backbone",
        "Mercury",
        "OtroFramework",
        "NingunFramework",
        "GitHub",
        "GitLab",
        "GoogleRepositories",
        "GitKraken",
        "OtroControldeVersiones",
        "NingunControldeVersiones",
        "Windows",
        "MacOS",
        "GNULinux",
        "OtroOS",
        "NingunOS",
        "Azure",
        "AWS",
        "Heroku",
        "GoogleCloud",
        "DigitalOcean",
        "OracleCloud",
        "OtraComputoNube",
        "NingunaComputoNube",
        "SaaS",
        "PaaS",
        "IaaSHaaS",
        "BaaS",
        "DaaS",
        "OtroTipoDeSoftware",
        "NingunSoftware",
        "VSCode",
        "IntelliJ",
        "PyCharm",
        "Xcode",
        "Eclipse",
        "SublimeText",
        "VIM",
        "OtroIDE",
        "NingunIDE",
        "fastapi",
        "Falcon",
        "Eve",
        "Hug",
        "Webpy",
        "Flask",
        "OtraAPI",
        "NigunaAPI",
        "JavaScript",
        "Python",
        "PHPConsumo",
        "JavaConsumo",
        "Ruby",
        "C",
        "OtraConsumo",
        "NingunaConsumo",
        "JSON",
        "XML",
        "HTMLInfo",
        "CSV",
        "RSS",
        "OtroFormato",
        "NingunFormto",
        "VariablesEntorno",
        "Scrum",
        "Kanban",
        "XP",
        "Agile",
        "Desing",
        "OtraMAgil",
        "NingunaMAgil",
        "Cascada",
        "Prototipado",
        "Espiral",
        "Incremental",
        "DiseñoRapido",
        "OtraMTradicional",
        "NingunaMTradicional",
    ]
].values
y = hiring_model["probabilidad"].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0
)


model_load = load("model.joblib")
predictions = model_load.predict(X_test)
