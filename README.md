<p align="center">
<img src="src/logo proyecto.png"  height=300>
</p>

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

<p align="left">
<img src="src/Distribicion de peliculas por dias de estreno.png"  height=300>
</p>

<p align="center">
<img src="src/Matriz de correlacion.png"  height=300>
</p>

<p align="center">
<img src="src/Peliculas mas populares.png"  height=300>
</p>

<p align="right">
<img src="src/Relacion de presupuesto y cantidad de votos.png"  height=300>
</p>

# <h2 align=center> Modelo Machine Learning </h2>


Al terminar la etapa del EDA, me propuse generar el modelo. Para ello, investigué y encontré que el enfoque basado en TF-IDF era el más fácil de implementar. Sin embargo, decidí desestimar este enfoque ya que no utilizaría un modelo de machine learning.

En su lugar, decidí implementar el modelo SVD utilizando la biblioteca Surprise. Sin embargo, me encontré con varios errores de compatibilidad con otras bibliotecas que estaba utilizando y no pude realizar la instalación adecuada de Surprise.

Dado el tiempo limitado que tenía para completar el proyecto y las posibles dificultades que podría enfrentar al implementar la API, opté por elegir un modelo de K-means.

Generé el modelo de K-means y busqué los clústeres óptimos para su implementación. En cuanto a las variables utilizadas para la generación del modelo, me limité a las variables numéricas. Intentar transformar las variables categóricas a un formato que el modelo pudiera utilizar resultaba en un costo computacional muy elevado. Por lo tanto, opté por utilizar únicamente las variables numéricas y generar una nueva columna que identificara a qué clúster pertenecía cada película.

<p align="center">
<img src="src/codo K-mean.png" 

# <h2 align=center> API y funcionalidades </h2>


La API se implementó en ***'render.com'*** utilizando la biblioteca ***'FASTAPI'*** para la generación del archivo **'main.py'** 

Las funcionalidades generadas fueron las siguientes:

+ def **peliculas_idioma( *`Idioma`* )**: 
  Se ingresa un idioma, debe devolver la cantidad de películas producidas en ese idioma. Para esta funcion se saco las abrebiaturas y se coloco el idioma entero, se deja la siguiente lista de referencia de idiomas
   
   *`idiomas_completos`* = ['Abkhazian', 'Afrikaans', 'Amharic', 'Arabic', 'Aymara', 'Bulgarian', 'Bambara', 'Bengali', 'Tibetan', 'Bosnian', 'Catalan', 'Chinese', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Basque', 'Persian', 'Finnish', 'French', 'Frisian', 'Galician', 'Hebrew', 'Hindi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian', 'Inuktitut', 'Japanese', 'Javanese', 'Georgian', 'Kazakh', 'Kannada', 'Korean', 'Kurdish', 'Kyrgyz', 'Latin', 'Luxembourgish', 'Lao', 'Lithuanian', 'Latvian', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Norwegian Bokmål', 'Nepali', 'Dutch', 'Norwegian', 'Punjabi', 'Polish', 'Pashto', 'Portuguese', 'Quechua', 'Romanian', 'Russian', 'Kinyarwanda', 'Serbo-Croatian', 'Sinhala', 'Slovak', 'Slovenian', 'Samoan', 'Albanian', 'Serbian', 'Swedish', 'Tamil', 'Telugu', 'Tajik', 'Thai', 'Tagalog', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Wolof', 'Unknown', 'Chinese', 'Zulu']

  
+ def **peliculas_duracion( *`Pelicula`* )** : 
  Se ingresa una pelicula. Debe devolver la duracion y el año.

+ def **franquicia( *`Franquicia`* )**: 
  Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio

+ def **peliculas_pais( *`Pais`* )**: 
  Se ingresa un país, retornando la cantidad de peliculas producidas en el mismo.

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


En el sistema de recomendación, la función filtra el título de la película para identificar a qué clúster pertenece. A continuación, se realiza un cálculo de popularidad y se muestra un top 5 de películas en función de esa popularidad. No se tiene en cuenta el título de la película proporcionada en el proceso de recomendación.

El objetivo es proporcionar al usuario una lista de películas similares y populares que puedan ser de su interés, basándose en el clúster al que pertenece la película consultada. Esto ayuda a ofrecer recomendaciones relevantes y diversificar las opciones para el usuario.

<p align="center">
<img src="src/render deploy.png" 

<p align="center">
<img src="src/Render API.png" 

# <h2 align=center> Consideraciones finales </h2>

Haciendo una recapitulación interna, se pudo mejorar varios procesos durante el desarrollo del proyecto y llegar a mejores resultados. Con la experiencia adquirida, se reconoce que existen varios aspectos que se podrían mejorar en el proyecto. Sin embargo, dadas las limitaciones de tiempo y la falta de experiencia en algunos aspectos, se considera que la implementación de la API y el sistema de recomendaciones es exitosa.

Es importante destacar el aprendizaje obtenido a lo largo del proyecto y reconocer las áreas en las que se pueden realizar mejoras en futuros proyectos. A medida que se adquiere más experiencia, se podrá perfeccionar aún más el desarrollo y optimización de sistemas similares.

En general, considero que el proyecto es una implementación sólida de una API y un sistema de recomendaciones, dadas las circunstancias y los recursos disponibles en ese momento.

# <h3 align=center> Link </h3>

+ Render:
    https://proyecto-recomendacion-peliculas-api.onrender.com/docs

+ Youtube
    https://youtu.be/O7jY7Lz4fxM