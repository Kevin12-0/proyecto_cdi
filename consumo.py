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


allowSelfSignedHttps(
    True
)  # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
    "Inputs": {
        "data": [
            {
                "Nombre": "example_value",
                "null": 0,
                "almost_null": 0,
                "basic": 0,
                "intermediate": 0,
                "advanced": 0,
                "native": 1,
                "HTML": 1,
                "CSS": 1,
                "SaSS": 1,
                "JS": 1,
                "PHP": 1,
                "JAVA": 0,
                "TS": 1,
                "OtraHerramienta": 0,
                "NingunaHerramientaWeb": 0,
                "React": 1,
                "Vue": 1,
                "Angular": 0,
                "Ember": 0,
                "Backbone": 0,
                "Mercury": 0,
                "OtroFramework": 0,
                "NingunFramework": 0,
                "GitHub": 1,
                "GitLab": 1,
                "Google Cloud Sorse Repositories": 0,
                "GitKraken": 1,
                "OtroControldeVerciones": 0,
                "NingunControldeVerciones": 0,
                "Windows": 1,
                "MacOS": 1,
                "GNULinux": 1,
                "Otro": 0,
                "NingunOS": 0,
                "Azure": 1,
                "AWS": 0,
                "Heroku": 1,
                "GoogleCloud": 0,
                "Digital Ocean": 0,
                "Oracle Cloud": 0,
                "OtraComputoNube": 0,
                "NingunaComputoNube": 0,
                "SaaS": 1,
                "PaaS": 1,
                "IaaS/HaaS": 1,
                "BaaS": 0,
                "DaaS": 0,
                "OtroTipoDeSoftware": 0,
                "NingunSoftware": 0,
                "VSCode": 1,
                "IntelliJ Idea": 1,
                "PyCharm": 1,
                "Xcode": 1,
                "Eclipse": 1,
                "Sublime Text": 1,
                "VIM": 1,
                "OtroIDE": 0,
                "NingunIDE": 0,
                "FastAPI": 1,
                "Falcon": 0,
                "Eve": 0,
                "Hug": 0,
                "Web.py": 1,
                "Flask": 1,
                "OtraAPI": 0,
                "NigunaAPI": 0,
                "JavaScript": 1,
                "Python": 1,
                "PHPConsumo": 1,
                "JavaConsumo": 0,
                "Ruby": 0,
                "C#": 1,
                "OtraConsumo": 0,
                "NingunaConsumo": 0,
                "JSON": 1,
                "XML": 1,
                "HTMLInfo": 1,
                "CSV": 1,
                "RSS": 0,
                "OtroFormato": 0,
                "Ningun Formto": 0,
                "VariablesEntorno": 1,
                "Scrum": 1,
                "Kanban": 1,
                "XP": 0,
                "Agile Inseption": 1,
                "Desing Spring": 1,
                "OtraMAgil": 0,
                "NingunaMAgil": 0,
                "Cascada": 1,
                "Prototipado": 1,
                "Espiral": 1,
                "Incremental": 0,
                "Diseño Rapido": 0,
                "OtraMTradicional": 0,
                "NingunaMTradicional": 0,
            }
        ]
    },
    "GlobalParameters": 1.0,
}

body = str.encode(json.dumps(data))

url = (
    "https://machile-leatning-studio-iosuk.southcentralus.inference.ml.azure.com/score"
)
# Replace this with the primary/secondary key or AMLToken for the endpoint
api_key = "w8UFfl5TS4DlbrOKYweXc2sz83iINuYe"
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {
    "Content-Type": "application/json",
    "Authorization": ("Bearer " + api_key),
    "azureml-model-deployment": "automl8ca357b353-1",
}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", "ignore"))
