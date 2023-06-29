# Librerias 
import os
from fastapi import FastAPI
import numpy as np
import pandas as pd
import fastparquet
import json

app = FastAPI()

dir_actual = os.getcwd()+'/Dataset/'

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
    return {'dia': mes, 'cantidad': respuesta}
    
@app.get('/cantidad_filmaciones_dia{dia}')
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
    df = pd.read_parquet(dir_actual+'df_movies_score')
    
    filtro = input("Ingrese el titulo de la pelicula que quiere saber los votos: ")
    df_filtro = df[df['title'] == filtro]   
    
    if len(df_filtro) == 0:
        print('No se encontró la pelicula con el título')
        return

    scort = df_filtro['popularity'].values[0]
    ano_estreno = df_filtro['release_year'].values[0]
    
    return {"La película", filtro, "fue estrenada en el año", ano_estreno, 'con un score/popularidad de',scort}



@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:str):
    df = pd.read_parquet(dir_actual+'df_movies_titulo')
    
    '''
    Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor 
    promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
    '''
    filtro = input("Ingrese el titulo de la pelicula que quiere saber los votos: ")
    df_filtro = df[df['title'] == filtro]  
    
    if len(df_filtro) == 0:
        print('No se encontró la pelicula con el título')
        return
    
    votos = df_filtro['vote_count'].values[0]
    promedio = df_filtro['vote_average'].values[0]
    
    if votos < 2000:
        print({'La pelicula no cumple con la condicion de tener al menos 2000 valoraciones.'})
        return
    
    ano_estreno = df_filtro['release_year'].values[0]    
    
    return {'titulo':str(filtro), 'anio':str(ano_estreno), 'voto_total': str(votos), 'voto_promedio': str(promedio)}

@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:str):
    df = pd.read_parquet(dir_actual+'df_final_con_modelo')
    
    '''
    Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver 
    el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno
    '''
    # Solicito el nombre del actor por teclado
    nombre_actor = input("Ingrese el nombre del actor: ").lower()

    # Filtro el DataFrame por el nombre del actor en minúsculas
    actor_films = df[df['actores'].apply(lambda actores: nombre_actor in [a.lower() for a in actores])]

    # Calculo la cantidad de películas en las que ha participado el actor
    cantidad_peliculas = len(actor_films)

    # Calculo el retorno total del actor sumando los retornos de todas las películas
    retorno_total = actor_films['return'].sum()

    # Calculo el promedio de retorno por película
    promedio_retorno = retorno_total / cantidad_peliculas
   
    
    return {
        "exito_actor": f"El actor {nombre_actor} ha participado de {cantidad_peliculas} cantidad de filmaciones, el mismo ha conseguido un retorno de {retorno_total} con un promedio de {promedio_retorno} por filmación",
        "cantidad_peliculas": cantidad_peliculas,
        "promedio_retorno": promedio_retorno
    }


@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    df = pd.read_parquet(dir_actual+'df_final_con_modelo')
    
    ''' 
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del 
    mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
    '''
    # Filtroel DataFrame por el nombre del director
    director_films = df[df['director'] == nombre_director]

    # Calculo el éxito del director como el promedio de retorno de todas las películas dirigidas por él
    promedio_retorno = director_films['return'].mean()

    # Creo la lista de películas dirigidas por el director con su información correspondiente
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
@app.get('/recomendacion/{titulo}')
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
