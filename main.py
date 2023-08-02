# Librerias
import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI, version
import os
import fastparquet

app = FastAPI(title="Bienvenido a Mi API")
dir_actual = os.getcwd()+'/Dataset/'

# Ruta raíz para obtener el logotipo
@app.get("/logo1.png")
async def get_logo():
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "logo1.png")
    return {"file": open(logo_path, "rb")}

# Definir la versión de la API
app_version = "1.0.0"
app = VersionedFastAPI(app, version=app_version)

# Endpoint de ejemplo con versión
@version(1)
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma_v1(idioma: str):
    # Tu código aquí para la versión 1
    df = pd.read_parquet(dir_actual + 'df_idioma_agrupado')
    cantidad_peliculas = df[df['original_language'] == idioma]['cantidad_peliculas'].sum()
    return {'mensaje': f"Versión 1 - La cantidad de peliculas estrenadas en idioma {idioma} es de {cantidad_peliculas}"}

@version(2)
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma_v2(idioma: str):
    # Tu código aquí para la versión 2
    df = pd.read_parquet(dir_actual + 'df_idioma_agrupado')
    cantidad_peliculas = df[df['original_language'] == idioma]['cantidad_peliculas'].sum()
    return {'mensaje': f"Versión 2 - La cantidad de peliculas estrenadas en idioma {idioma} es de {cantidad_peliculas}"}