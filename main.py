import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import APIKey
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_versioning import VersionedFastAPI, version
import os
import fastparquet
import json

app = FastAPI(title="Bienvenido a Mi API", version="1.0.0")
templates = Jinja2Templates(directory="templates")
dir_actual = os.getcwd()+'/Dataset/'

# Ruta raíz para obtener el logotipo
@app.get("/logo1.png", response_class=HTMLResponse)
async def get_logo():
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "logo1.png")
    return {"file": open(logo_path, "rb")}


@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    df = pd.read_parquet(dir_actual+'df_idioma_agrupado')
    
    '''
    Se ingresa un idioma, debe devolver la cantidad de películas producidas en ese idioma.
    Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma.
    '''
    
    cantidad_peliculas = df[df['original_language'] == idioma]['cantidad_peliculas'].sum()
    return {'mensaje': f"La cantidad de peliculas estrenadas en idioma {idioma} es de {cantidad_peliculas}"}

idiomas_completos = ['Abkhazian', 'Afrikaans', 'Amharic', 'Arabic', 'Aymara', 'Bulgarian', 'Bambara', 'Bengali', 'Tibetan', 'Bosnian', 'Catalan', 'Chinese', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Basque', 'Persian', 'Finnish', 'French', 'Frisian', 'Galician', 'Hebrew', 'Hindi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian', 'Inuktitut', 'Japanese', 'Javanese', 'Georgian', 'Kazakh', 'Kannada', 'Korean', 'Kurdish', 'Kyrgyz', 'Latin', 'Luxembourgish', 'Lao', 'Lithuanian', 'Latvian', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Norwegian Bokmål', 'Nepali', 'Dutch', 'Norwegian', 'Punjabi', 'Polish', 'Pashto', 'Portuguese', 'Quechua', 'Romanian', 'Russian', 'Kinyarwanda', 'Serbo-Croatian', 'Sinhala', 'Slovak', 'Slovenian', 'Samoan', 'Albanian', 'Serbian', 'Swedish', 'Tamil', 'Telugu', 'Tajik', 'Thai', 'Tagalog', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Wolof', 'Unknown', 'Chinese', 'Zulu']

# Agregar la lista plegable de idiomas
@app.get("/docs", response_class=HTMLResponse)
@version(1)
async def custom_swagger_ui_html():
    openapi_url = "/openapi.json"
    title = "Documentación de Mi API"
    html_content = get_swagger_ui_html(openapi_url=openapi_url, title=title)
    html_with_list = html_content.replace(
        "<h2>Endpoints</h2>",
        "<h2>Endpoints</h2>\n<ul>" + "".join(f"<li>{idioma}</li>" for idioma in idiomas_completos) + "</ul>"
    )
    return HTMLResponse(content=html_with_list)

# Agregar más rutas aquí...

# Iniciar la aplicación utilizando VersionedFastAPI
app = VersionedFastAPI(app, version_format="{major}.{minor}")
