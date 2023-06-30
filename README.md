<h1 align="center">Proyecto Recomendación Películas + API</h1>

El siguiente proyecto se generó con la intención de mostrar un Producto Mínimo Viable (MVP). Aborda la problemática de un sistema de recomendaciones que abarca desde la recolección y tratamiento de datos hasta la generación del modelo y las funcionalidades de la aplicación, incluyendo la implementación de una API en línea funcional.

Datasets
El proyecto utiliza dos conjuntos de datos:

1. movies_dataset.csv: contiene las siguientes características:
     * budget: El presupuesto con el que se realizó la película.
     * genre: El género de la película (acción, comedia, thriller, etc.).
     * homepage: Un enlace a la página principal de la película.
     * id: El movie_id tal como está en el primer conjunto de datos.
     * keywords: Las palabras clave o etiquetas relacionadas con la película.
     * original_language: El idioma en el que se realizó la película.
     * original_title: El título de la película antes de la traducción o adaptación.
     * overview: Una breve descripción de la película.
     * popularity: Una cantidad numérica que especifica la popularidad de la película.
     * production_companies: La productora de la película.
     * production_countries: El país en el que se produjo.
     * release_date: La fecha en la que se estrenó.
     * revenue: Los ingresos generados por la película en todo el mundo.
     * runtime: La duración de la película en minutos.
     * status: "Estrenada" o "Rumor".
     * tagline: Eslogan de la película.
     * title: Título de la película.
     * vote_average: Calificación promedio que recibió la película.
     * vote_count: La cantidad de votos recibidos.

2. Credits.csv: contiene las siguientes características:
     * movie_id: Un identificador único para cada película.
     * cast: El nombre de los actores principales y de reparto.
     * crew: El nombre del director, editor, compositor, escritor, etc.

Los dos conjuntos de datos se unieron en la columna 'id' utilizando el método merge para su posterior limpieza y adecuación de los datos.

El proyecto me presento varios retos a nivel de datos, ya que varias columna tenian datos anidados y las formas de tratarlos fue especifica para cada columna, lo que me genero una perdida de tiempo importante en la investigacion de su realizacion y metodologias.

# <h2 align=center> EDA </h2>

El EDA se dividió en análisis de variables categóricas y numéricas para un mejor análisis. A continuación, se muestran algunas imágenes de los análisis realizados:


### Adjuntar imagenes ### 

# <h2 align=center> Modelo Machine Learning </h2>

Al terminar la etapa del EDA me propuse generar el modelo, para lo cual investigue y lo mejor era realizarlo por un enfoque Enfoque basado en TF-IDF que es una medida estadística que evalúa la importancia de una palabra en un documento en un corpus.

Si bien el mismo era el mas facil de realizar, no estaria utilizando un modelo de machine learning con lo cual se desestimo este enfoque.

Con lo cual me prepuse implementar el modelo SVD con la libreria surprise, debo reconocer que no pude realizar la instalacion de la misma ya que presentaba varios errores de compatibilidad con otras librerias que venia usando.

Considerando el tiempo que me quedaba para la realizacion del proyecto y las dificultades que prodia presentar el desploy de la API, opte por elegir un modelo de K-means.

El mismo fue generado y se busco los cluster optimos para la realizacion. 

En cuanto a las variables que se usaron para la generacion del modelo, me limite a las numericas ya que al querer transformar variables categoriacas a un formato que el modelo pudiera utilizar el costo computacional de la tarea era muy elevado. Con lo cual opte por usar la variables numericas y generar una nueva columna donde se identifica a que cluster pertenece la pelicula.

### adjuntar imagen de los cluster

# <h2 align=center> API y funcionalidades </h2>

La API se implato en ***'render.com'*** utilizando la libreria ***'FASTAPI'*** para la generacion del archivo **'main.py'** 

Las funcionalidades generaras fueron las siguientes:

+ def **cantidad_filmaciones_mes( *`Mes`* )**:
    Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.

+ def **cantidad_filmaciones_dia( *`Dia`* )**:
    Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.

+ def **score_titulo( *`titulo_de_la_filmación`* )**:
    Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.

+ def **votos_titulo( *`titulo_de_la_filmación`* )**:
    Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.

+ def **get_actor( *`nombre_actor`* )**:
    Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. **La definición no deberá considerar directores.**

+ def **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

+ def **recomendacion( *`titulo`* )**:
    Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

En el sistema de recomendacion la funcion filtra el titulo de la pelicula identificando al cluster que pertenece y se procede a hacer un top 5 por la columna popularidad donde no se tiene en cuenta el titulo de la pelicula proporcionada.

### Agregar imagen de la api

# <h2 align=center> Consideraciones finales </h2>

Haciendo una recapacitacion interna, se pudo mejor varios procesos del desarrollo del proyecto y llegar a mejores resultados. Hoy contando con mayor experiencia considero que tengo varios aspectos a mejorar en el proyecto pero para el tiempo que se contaba para la realizacion del mismo y la inexperiencia que poseia en varios aspectos considero que es una buena implantacion de una api y un sistema de recomendaciones.


# <h3 align=center> Link </h3>

+ Render:
    https://proyecto-recomendacion-peliculas-api.onrender.com/docs

+ Youtube
    https://youtu.be/O7jY7Lz4fxM