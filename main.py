# Librerias
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request
from fastapi_versioning import VersionedFastAPI, version
from fastapi.templating import Jinja2Templates
import os
import fastparquet

app = FastAPI(title="Bienvenido a Mi API")

# Ruta raíz para obtener el logotipo
@app.get("/logo1.png")
async def get_logo():
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "logo1.png")
    return {"file": open(logo_path, "rb")}

# Definir la versión de la API
app_version = "1.0.0"
app = VersionedFastAPI(app, version=app_version)

# Ruta para mostrar el formulario con la lista desplegable
templates = Jinja2Templates(directory="templates")

@version(1)
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma_v1(request: Request, idioma: str):
    idiomas_completos = [
        'Abkhazian', 'Afrikaans', 'Amharic', 'Arabic', 'Aymara', 'Bulgarian', 'Bambara', 'Bengali', 'Tibetan', 'Bosnian',
        'Catalan', 'Chinese', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian',
        'Basque', 'Persian', 'Finnish', 'French', 'Frisian', 'Galician', 'Hebrew', 'Hindi', 'Croatian', 'Hungarian',
        'Armenian', 'Indonesian', 'Icelandic', 'Italian', 'Inuktitut', 'Japanese', 'Javanese', 'Georgian', 'Kazakh',
        'Kannada', 'Korean', 'Kurdish', 'Kyrgyz', 'Latin', 'Luxembourgish', 'Lao', 'Lithuanian', 'Latvian', 'Macedonian',
        'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Norwegian Bokmål', 'Nepali', 'Dutch', 'Norwegian',
        'Punjabi', 'Polish', 'Pashto', 'Portuguese', 'Quechua', 'Romanian', 'Russian', 'Kinyarwanda', 'Serbo-Croatian',
        'Sinhala', 'Slovak', 'Slovenian', 'Samoan', 'Albanian', 'Serbian', 'Swedish', 'Tamil', 'Telugu', 'Tajik', 'Thai',
        'Tagalog', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Wolof', 'Unknown', 'Chinese', 'Zulu'
    ]

    return templates.TemplateResponse(
        "peliculas_idioma.html",
        {"request": request, "idioma": idioma, "idiomas_completos": idiomas_completos}
    )
