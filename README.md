# Análisis Histórico del Clima: Tendencias y Variabilidad en España

## 1. Introducción
El clima desempeña un papel fundamental en nuestra sociedad, influyendo en una amplia gama de aspectos que afectan nuestra vida diaria. Desde la seguridad alimentaria y la planificación urbana hasta la gestión de recursos hídricos, comprender las tendencias y la variabilidad del clima es esencial para tomar decisiones informadas y desarrollar estrategias efectivas en respuesta al cambio climático.

En este proyecto, me he enfocado en analizar el histórico del clima en España, un país con una diversidad geográfica notable. Para llevar a cabo este análisis, he recurrido a una combinación de datos recopilados de fuentes confiables y reconocidas, como: 
- [National Oceanic and Atmospheric Administration (NOAA)](https://www.noaa.gov/), 
- [Embalses.net](https://www.embalses.net/) y 
- [DatosClima.es](https://datosclima.es/index.htm), 

Se pretende investigar las tendencias y la variabilidad de variables climáticas clave, como la temperatura y la precipitación, a lo largo del tiempo.  
Para llevar a cabo este análisis, he utilizado técnicas de procesamiento de datos y visualización para explorar y comprender los patrones climáticos en diferentes regiones de España. También he examinado la relación entre las variables climáticas y otros fenómenos, como la disponibilidad de agua en embalses y estaciones hidrológicas.

## 2. Objetivo
El objetivo central de este proyecto radica en adquirir información valiosa sobre las tendencias climáticas en España y su influencia en el entorno natural y las actividades humanas. Este conocimiento nos brindará una comprensión más profunda de los desafíos que enfrentamos en la gestión del agua, permitiéndonos desarrollar estrategias efectivas para mitigar períodos de escasez.

Para realizar este análisis utilizaremos distintas visualizaciones generadas mediante la librería “matplotlib” del lenguaje de programación “Python” 

Se han utilizado datos de 207 estaciones meteorológicas españolas repartidas por cada provincia Española, se buscarán patrones y tendencias en los distintos registros entre los años 1990 y 2020 con la finalizad de entender la evolución meteorológica sufrida en este periodo de tiempo. 

Una vez analizados los datos, podremos contestar a preguntas como las que se muestran a continuación: 
- ¿Cuál es la tendencia en la evolución de las temperaturas en los últimos años? 
- ¿Cuál es la tendencia en la evolución de las precipitaciones en los últimos años?  
- ¿Qué grado de correlación hay entre las distintas variables climatológicas registradas? 

Existen diversas interrogantes, incluyendo las mencionadas anteriormente, que pueden encontrar respuesta a través del empleo de herramientas que facilitan la interpretación de datos mediante visualizaciones interactivas.

## 3. Recursos
### 3.1 Conjunto de datos
Los conjuntos de datos recopilan información meteorológica relevante y están organizados por año. Para acceder a ellos, podemos utilizar el centro de descargas de la "National Oceanic and Atmospheric Administration (NOAA)", disponible en la sección de descargas. Además, la información histórica de los embalses se encuentra disponible en embalses.net, mientras que el resto de los datos pueden consultarse en DatosClima.es.


### 3.2 Herramientas
Para la realización de las tareas de preprocesado de los datos, realizar consultas, modificaciones y gestión de datos se ha utilizado el lenguaje de SQL en MySQL Workbench, todo  descrito en un archivo Markdown alojado en la seccion de código alojado en esta misma carpeta, para revisarlo simplemente pinca en el siguente enlace [Códico](https://github.com/icarolosada/Analisis-de-Datos/blob/main/Codigo.md).

Para la visualizacion de gráficas se ha utilizado el lenguaje de programación Python el cual se ejecuta sobre un Notebook de Jupyter, utilizando la libreria [Matplotlib](https://matplotlib.org/) se puede ver todo el codigo y gráficas en la carpeta de Visualizaciones accede pinchando en [visualizaciones](https://github.com/icarolosada/Analisis-de-Datos/tree/master/Visualizaciones/Visualizaciones)  

Jupyter Notebook es una herramienta poderosa y versátil que permite programar, ejecutar y compartir código de manera interactiva. Es un entorno de desarrollo basado en web que facilita la creación y edición de documentos en los que se pueden combinar código, visualizaciones, texto explicativo y otros elementos.

## 4. Tratamiento o preparación de los datos
Los procesos que describo a continuación los encontrarás comentados en un [Notebook de Jupyter ]([https://xxxxxx](https://jupyter.org/)) que también podrás ejecutar desde este [Notebook2](https://github.com/icarolosada/Analisis-de-Datos/blob/master/Codigo/Codigo/Notebook2.ipynb) alojado este mismo post de Github en la carpeta de código. 

Antes de lanzarnos a construir una visualización efectiva, debemos realizar un tratamiento previo de los datos, prestando especial atención a la obtención de los mismos y validando su contenido, asegurando que se encuentran en el formato adecuado y consistente para su procesamiento y que no contienen errores. Todo se ha realizado mediante consultas en MySQL descritas el archivo [SQL_Query](https://github.com/icarolosada/Analisis-de-Datos/blob/master/Codigo/Codigo/SQL_Query.md) 

Como primer paso del proceso, una vez que se han importado los datos necesarios en formato .csv y se han cargado en la base de datos, es crucial llevar a cabo un análisis exploratorio de los datos (EDA). Este análisis tiene como objetivo interpretar adecuadamente los datos de partida, identificar posibles anomalías, datos faltantes o errores que puedan afectar la calidad de los procesos y los resultados posteriores. Para obtener más detalles sobre el análisis realizado, se puede consultar el archivo [SQL_Query](https://github.com/icarolosada/Analisis-de-Datos/blob/master/Codigo/Codigo/SQL_Query.md)que describe dicho proceso.


El siguiente paso consiste en generar las tablas de datos preprocesados que utilizaremos para nuestras visualizaciones. Para lograr esto, filtraremos los conjuntos de datos iniciales y calcularemos los valores relevantes y necesarios para el análisis llevado a cabo en este ejercicio. Puedes encontrar más detalles sobre este proceso en el apartado [datos_procesados](https://github.com/icarolosada/Analisis-de-Datos/tree/master/Datos_procesados)

Una vez terminado el preprocesamiento, obtendremos las tablas de datos “media_lluvia_anos.xlsx” , “Media_temperaturas_anos.xlsx” y  "Capacida_embalses.xlsx" las cuales utilizaremos en el siguiente apartado del Notebook para generar las visualizaciones.  

La estructura del Notebook en la que se realizan los pasos previamente descritos junto a comentarios explicativos de cada uno de ellos, es la siguiente: 

1. Instalación y carga de librerías
2. Carga de los conjuntos de datos
3. Análisis exploratorio de datos (EDA)
4. Preparación de las tablas de datos
5. Visualizaciones
6. Guardado de gráficos

Podrás reproducir este análisis, ya que el código fuente está disponible en nuestra la de GitHub. La forma de proporcionar el código es a través de un documento realizado sobre un Jupyter Notebook que una vez cargado en el entorno de desarrollo podrás ejecutar o modificar de manera sencilla. EL carácter de este post es totalmente informativo y quiere favorecer el entendimiento de los lectores no especializados, el código no pretende ser el más eficiente, sino facilitar su comprensión por lo que posiblemente se te ocurrirán muchas formas de optimizar el código propuesto para lograr fines similares. ¡Te animo a que lo hagas! 


## 5. Visualizaciones
Se han creado diversas visualizaciones y gráficos utilizando la biblioteca de visualización de datos matplotlib en Python, con el objetivo de extraer información de las tablas de datos preprocesadas y responder a las preguntas iniciales planteadas en este ejercicio.

Matplotlib es una biblioteca de visualización ampliamente utilizada en el lenguaje de programación Python. Permite generar una amplia variedad de gráficos, como gráficos de líneas, de barras, de dispersión, de torta, entre otros. Con matplotlib, es posible personalizar cada aspecto de las visualizaciones, incluyendo los ejes, etiquetas, colores y estilos.

En la siguiente [carpeta](https://github.com/icarolosada/Analisis-de-Datos/tree/master/Visualizaciones/Visualizaciones), encontrarás todas las visualizaciones generadas utilizando matplotlib, que se describen en los siguientes apartados.

## 5.1 Gráficos
Los gráficos son representaciones visuales de datos que nos permiten comunicar información de manera efectiva. Hay una amplia variedad de tipos de gráficos disponibles, como gráficos de barras, gráficos de líneas, gráficos de dispersión y gráficos circulares, entre otros. Los gráficos de barras son útiles para comparar la magnitud de diferentes categorías y para visualizar diferencias entre ellas. 

# 6. Conclusiones del ejercicio
xxxxxx
xxxxxx

