# Librerias 
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import numpy as np
import pandas as pd
import fastparquet
import json

app = FastAPI()

dir_actual = os.getcwd()+'/Dataset/'


# Monto la carpeta "static" en la ruta "/static"
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root():
    titulo = "Bienvenido a Mi App de Películas"
    logo1 = "/static/logo1.png"
    logo2 = "/static/logo2.png"

    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{titulo}</title>
        </head>
        <body>
            <div style="text-align: center; margin-top: 20px;">
                <h1>{titulo}</h1>
                <img src="{logo1}" alt="Logo 1" width="200" height="200">
                <img src="{logo2}" alt="Logo 2" width="200" height="200">
                <br>
                <br>
                <h2>Funciones disponibles:</h2>
                <ul>
            </div>
        </body>
        </html>
    """
dir_actual = os.getcwd()+'/Dataset/'

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    df = pd.read_parquet(dir_actual+'df_idioma_agrupado')
    
    '''
    Se ingresa un idioma, debe devolver la cantidad de películas producidas en ese idioma.
    Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma.
    '''
    cantidad_peliculas = df[df['original_language'] == idioma]['cantidad_peliculas'].sum()
    return {'mensaje': f"La cantidad de peliculas estrenadas en idioma {idioma} es de {cantidad_peliculas}"}

@app.get('/peliculas_duracion/{peliculas_duracion}')
def peliculas_duracion(titulo_de_la_filmacion: str):
    df = pd.read_parquet(dir_actual + 'df_movies_final')
    '''
    Se ingresa una película. Debe devolver la duración y el año.
    Ejemplo de retorno: X. Duración: X minutos. Año: XXXX.
    '''
    # Espacios en blanco
    titulo_de_la_filmacion = titulo_de_la_filmacion.replace("%20", " ")
    
    df_filtro = df[df['title'] == titulo_de_la_filmacion]

    if len(df_filtro) == 0:
        return {'mensaje': 'No se encontró la película con el título especificado'}
    
    # Obtengo los valores de duración y año de estreno
    runtime = df_filtro['runtime'].values[0]
    ano_estreno = df_filtro['release_year'].values[0]
    
    return {"mensaje": f"La película '{titulo_de_la_filmacion}' fue estrenada en el año {ano_estreno} con una duración de {runtime} minutos."}

from fastapi import FastAPI, Query

app = FastAPI()

# Resto del código...

@app.get('/franquicia/')
def franquicia(franquicia: str = Query(..., description="Nombre de la franquicia")):
    df = pd.read_parquet(dir_actual + 'df_movies_final')
    
    '''
    Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx
    '''
    # Filtro las películas que pertenecen a la franquicia
    franquicia_df = df[df['belongs_to_collection'] == franquicia]

    if franquicia_df.empty:
        return {'mensaje': f'No se encontró la franquicia "{franquicia}" en la base de datos.'}

    # Calculo la cantidad de películas, ganancia total y promedio
    cantidad_peliculas = len(franquicia_df)
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = franquicia_df['revenue'].mean()

    return {
        'mensaje': f'La franquicia "{franquicia}" posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}.'
    }


'''
@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    df = pd.read_parquet(dir_actual + 'df_movies_final')
    
    
    #Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    #Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx

    # Filtro las películas que pertenecen a la franquicia
    franquicia_df = df[df['belongs_to_collection'] == franquicia]

    if franquicia_df.empty:
        return {'mensaje': f'No se encontró la franquicia "{franquicia}" en la base de datos.'}

    # Calculo la cantidad de películas, ganancia total y promedio
    cantidad_peliculas = len(franquicia_df)
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = franquicia_df['revenue'].mean()

    return {
        'mensaje': f'La franquicia "{franquicia}" posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}.'
    }
    
'''
@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    df = pd.read_parquet(dir_actual + 'df_movies_final')
    
    '''
    Se ingresa un país, retornando la cantidad de peliculas producidas en el mismo.
    Ejemplo de retorno: Se produjeron X películas en el país X

    '''
    # Filtro las películas producidas en el país especificado
    peliculas_pais_df = df[df['production_countries'].str.contains(pais)]

    if peliculas_pais_df.empty:
        return {'mensaje': f'No se encontraron películas producidas en el país "{pais}" en la base de datos.'}

    # Calculo la cantidad de películas producidas en el país
    cantidad_peliculas = len(peliculas_pais_df)

    return {
        'mensaje': f'Se produjeron {cantidad_peliculas} películas en el país "{pais}".'
    }

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    df = pd.read_parquet(dir_actual+'df_mes')
       
    '''
    Se ingresa el mes en español y la función retorna la cantidad de películas que se 
    estrenaron ese mes históricamente
    '''
    
    # Convierto el mes consultado a minúsculas y en español, y aplica capitalize que nos devuelve la primer letra en mayúscula, el resto de la palabra en minúscula como la tenemos en el df.
    mes = mes.lower().capitalize()
    
    # Filtro por el día de lanzamiento en el dataset
    df1 = df[df['release_month'] == mes]

    # Obtengo la cantidad de películas para ese día
    respuesta = len(df1)
    return {'mes': mes, 'cantidad': respuesta}
    
@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str):
    df = pd.read_parquet(dir_actual+'df_dia')
    
    '''
    Se ingresa el dia y la funcion retorna la cantidad de peliculas que se 
    estrenaron ese dia historicamente
    '''
    # Converto el día consultado a minúsculas y en español, y aplicar capitalize para obtener la primera letra en mayúscula
    dia = dia.lower().capitalize()
    
    # Asigno un valor predeterminado a df_day
    df_day = None
    
    # Filtro por día en el dataset
    if dia in df['release_day'].unique():
        df_day = df[df['release_day'] == dia]

    # Verific0 si se encontraron datos para el día consultado
    if df_day is not None:
        # Obtengo la cantidad de películas para ese día
        respuesta = len(df_day)
        return {'dia': dia, 'cantidad': respuesta}
    else:
        return {'dia': dia, 'cantidad': 0}

@app.get('/score_titulo/{titulo_de_la_filmacion}')
def score_titulo(titulo_de_la_filmacion):
    df = pd.read_parquet(dir_actual + 'df_movies_score')
    '''
    Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score/popularidad.
    '''
    # Espacios en blanco
    titulo_de_la_filmacion = titulo_de_la_filmacion.replace("%20", " ")
    
    df_filtro = df[df['title'] == titulo_de_la_filmacion]

    if len(df_filtro) == 0:
        return {'mensaje': 'No se encontró la película con el título'}
    
    score = df_filtro['popularity'].values[0]
    ano_estreno = df_filtro['release_year'].values[0]
    
    return {"mensaje": f"La película '{titulo_de_la_filmacion}' fue estrenada en el año {ano_estreno} con un score/popularidad de {score}"}


@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:str):
    df = pd.read_parquet(dir_actual + 'df_movies_titulo')
    '''
    Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor 
    promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
    '''
    # Espacios en blanco 
    titulo = titulo.replace("%20", " ")
    
    df_filtro = df[df['title'] == titulo]

    if len(df_filtro) == 0:
        return {'mensaje': 'No se encontró la película con el título'}

    votos = df_filtro['vote_count'].values[0]
    promedio = df_filtro['vote_average'].values[0]

    if votos < 2000:
        return {'mensaje': 'La película no cumple con la condición de tener al menos 2000 valoraciones.'}

    ano_estreno = df_filtro['release_year'].values[0]
    return {'titulo': titulo, 'anio': str(ano_estreno), 'voto_total': str(votos), 'voto_promedio': str(promedio)}

@app.get('/nombre_actor/{nombre_actor}')
def nombre_actor(nombre_actor:str):
    df = pd.read_parquet(dir_actual+'df_actores')
    
    '''
    Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver 
    el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno
    '''
     # Convertir el nombre del director a minúsculas
    nombre_actor = nombre_actor.lower()

    # Filtro el DataFrame por el nombre del actor en minúsculas
    actor_films = df[df['actores'].apply(lambda actores: nombre_actor in [a.lower() for a in actores])]

    # Calculo la cantidad de películas en las que ha participado el actor
    cantidad_peliculas = len(actor_films)

    # Calculo el retorno total del actor sumando los retornos de todas las películas
    retorno_total = actor_films['return'].sum()

    # Calculo el promedio de retorno por película
    promedio_retorno = retorno_total / cantidad_peliculas
   
    return {
        "Exito_actor": f"El actor {nombre_actor} ha participado de {cantidad_peliculas} cantidad de filmaciones, el mismo ha conseguido un retorno de {retorno_total} con un promedio de {promedio_retorno} por filmación."
        }


@app.get('/nombre_director/{nombre_director}')
def nombre_director(nombre_director: str):
    df = pd.read_parquet(dir_actual + 'df_director')
    
    '''
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del 
    mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
    '''
    # Convertir el nombre del director a minúsculas
    nombre_director = nombre_director.lower()

    # Filtrar el DataFrame por el nombre del director
    director_films = df[df['director'].str.lower().str.contains(nombre_director)]

    # Calculo el éxito del director como el promedio de retorno de todas las películas dirigidas por él
    promedio_retorno = director_films['return'].mean()

    # Crear la lista de películas dirigidas por el director con su información correspondiente
    peliculas = []
    for index, row in director_films.iterrows():
        pelicula = {
            "nombre": row['title'],
            "fecha_lanzamiento": str(row['release_date']),
            "retorno": row['return'],
            "costo": row['budget'],
            "ganancia": row['revenue']
        }
        peliculas.append(pelicula)

    return {
        "exito_director": f"El director {nombre_director} ha tenido éxito con un promedio de retorno de {promedio_retorno}",
        "peliculas": peliculas
    }

    
# ML
@app.get('/recomendacion/{recomendacion}')
def recomendacion(titulo:str):
    df = pd.read_parquet(dir_actual+'df_final_con_modelo')
    
    '''
    Ingresas un nombre de pelicula y te recomienda las similares en una lista
    '''
    # Obtengo el índice de la película buscada
    idx = df[df['title'] == titulo].index[0]

    # Obtengo el cluster asignado a la película buscada
    cluster_label = df.loc[idx, 'cluster_label']

    # Filtro las películas que pertenecen al mismo cluster
    cluster_movies = df[df['cluster_label'] == cluster_label]

    # Saco la película de referencia de la lista
    cluster_movies = cluster_movies[cluster_movies['title'] != titulo]

    # Ordeno las películas del cluster por popularidad de forma descendente
    cluster_movies = cluster_movies.sort_values(by='popularity', ascending=False)

    # Obtengo los títulos de las películas más populares dentro del cluster (excluyendo la película de referencia)
    recommended_movies = cluster_movies['title'].tolist()[:5]

    # Retorna la lista de los 5 títulos más populares dentro del cluster (excluyendo la película de referencia)
    return recommended_movies
