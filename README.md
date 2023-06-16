# Análisis Histórico del Clima: Tendencias y Variabilidad en España

## 1. Introducción
El clima es un factor fundamental que influye en diversos aspectos de nuestra vida, desde la agricultura y la seguridad alimentaria hasta la planificación urbana y la gestión de recursos hídricos. Comprender las tendencias y la variabilidad del clima es crucial para tomar decisiones informadas y desarrollar estrategias efectivas en respuesta al cambio climático.En este proyecto, nos centraremos en analizar el histórico del clima en España.Utilizando una combinación de datos recopilados de diversas fuentes confiables, como: 
- [National Oceanic and Atmospheric Administration (NOAA)](https://www.noaa.gov/), 
- [Embalses.net](https://www.embalses.net/) y 
- [DatosClima.es](https://datosclima.es/index.htm), 

Se pretende investigar las tendencias y la variabilidad de variables climáticas clave, como la temperatura y la precipitación, a lo largo del tiempo.  

Para llevar a cabo este análisis, utilizaremos técnicas de procesamiento de datos y visualización para explorar y comprender los patrones climáticos en diferentes regiones de España. También examinaremos la relación entre las variables climáticas y otros fenómenos, como la disponibilidad de agua en embalses y estaciones hidrológicas.

## 2. Objetivo
El objetivo principal de este proyecto es obtener información valiosa sobre las tendencias climáticas en España y su impacto en el entorno natural y las actividades humanas. Este conocimiento nos ayudará a comprender mejor los desafíos que enfrentamos en la gestión del agua y a desarrollar estrategias para mitigar peridos de escased.

Para realizar este análisis utilizaremos distintas visualizaciones generadas mediante la librería “xxxx” del lenguaje de programación “Python” 

Se han utilizado datos de todas las estaciones meteorológicas españolas, se buscarán patrones y tendencias en los distintos registros entre los años 1990 y 2020 con la finalizad de entender la evolución meteorológica sufrida en este periodo de tiempo. 

Una vez analizados los datos, podremos contestar a preguntas como las que se muestran a continuación: 
- ¿Cuál es la tendencia en la evolución de las temperaturas en los últimos años? 
- ¿Cuál es la tendencia en la evolución de las precipitaciones en los últimos años?  
- ¿Qué grado de correlación hay entre las distintas variables climatológicas registradas? 

Estas, y muchas otras preguntas pueden ser resueltas mediante el uso de herramientas que facilitan la interpretación de los datos mediante visualizaciones interactivas.

## 3. Recursos
### 3.1 Conjunto de datos
Los conjuntos de datos contienen distinta información meteorológica de interés para la cuestión estan desglosados por año. Dentro del centro de descargas de "National Oceanic and Atmospheric Administration (NOAA)", podremos descárgalos, en el apartado de descargas. Igualmente en la iformación historica de los embalses es pulbica en embalses.net y el resto en DatosClima.es


### 3.2 Herramientas
Para la realización de las tareas de preprocesado de los datos, realizar consultas, modificaciones y gestión de datos se ha utilizado el lenguaje de SQL en MySQL Workbench, todo  descrito en un archivo Markdown alojado en la seccion de código alojado en esta misma carpeta, para revisarlo simplemente pinca en el siguente enlace [Códico](https://github.com/icarolosada/Analisis-de-Datos/blob/main/Codigo.md).

Para la visualizacion de gráficas se ha utilizado el lenguaje de programación Python el cual se ejecuta sobre un Notebook de Jupyter, utilizando la libreria [Matplotlib](https://matplotlib.org/) se puede ver todo el codigo y gráficas en la carpeta de Visualizaciones accede pinchando [aki](http://xxx.xxx)  

Jupyter Notebook es una herramienta poderosa y versátil que permite programar, ejecutar y compartir código de manera interactiva. Es un entorno de desarrollo basado en web que facilita la creación y edición de documentos en los que se pueden combinar código, visualizaciones, texto explicativo y otros elementos.

## 4. Tratamiento o preparación de los datos
Los procesos que te describimos a continuación los encontrarás comentados en [Jupyter Notebook](https://xxxxxx) que también podrás ejecutar desde xxxxxx. 

Antes de lanzarnos a construir una visualización efectiva, debemos realizar un tratamiento previo de los datos, prestando especial atención a la obtención de los mismos y validando su contenido, asegurando que se encuentran en el formato adecuado y consistente para su procesamiento y que no contienen errores. Todo se ha realizado mediante consultas en MySQL descritas el archivo [SQL_Query](https://github.com/icarolosada/Analisis-de-Datos/blob/master/Codigo/SQL_Query.md) 

Como primer paso del proceso, una vez importados las datos en formato .csv necesarios y cargados a la base de datos, es necesario realizar un análisis exploratorio de los datos (EDA) con el fin de interpretar adecuadamente los datos de partida, detectar anomalías, datos ausentes o errores que pudieran afectar a la calidad de los procesos posteriores y resultados. Todo descrito en el archivo[SQL_Query](https://github.com/icarolosada/Analisis-de-Datos/blob/master/Codigo/SQL_Query.md) 

El siguiente paso a dar es generar las tablas de datos preprocesadas que usaremos en las visualizaciones. Para ello, filtraremos los conjuntos de datos iniciales y calcularemos los valores que sean necesarios y de interés para el análisis realizado en este ejercicio, lo pouedes encontrar en el apartado [datos_procesados](https://github.com/icarolosada/Analisis-de-Datos/tree/master/Datos_procesados)

Una vez terminado el preprocesamiento, obtendremos las tablas de datos “media_lluvia_anos.xlsx” , “Media_temperaturas_anos.xlsx” y  "Capacida_embalses.xlsx" las cuales utilizaremos en el siguiente apartado del Notebook para generar las visualizaciones.  

La estructura del Notebook en la que se realizan los pasos previamente descritos junto a comentarios explicativos de cada uno de ellos, es la siguiente: 

1. Instalación y carga de librerías
2. Carga de los conjuntos de datos
3. Análisis exploratorio de datos (EDA)
4. Preparación de las tablas de datos
5. Visualizaciones
6. xxxxxxxx

Podrás reproducir este análisis, ya que el código fuente está disponible en nuestra la de GitHub. La forma de proporcionar el código es a través de un documento realizado sobre un Jupyter Notebook que una vez cargado en el entorno de desarrollo podrás ejecutar o modificar de manera sencilla. EL carácter de este post es totalmente informativo y quiere favorecer el entendimiento de los lectores no especializados, el código no pretende ser el más eficiente, sino facilitar su comprensión por lo que posiblemente se te ocurrirán muchas formas de optimizar el código propuesto para lograr fines similares. ¡Te animo a que lo hagas! 


* * *
- - -
_ _ _


## 5. Visualizaciones
xxxxxxxxx
xxxxxxxxxx

## 5.1 Gráficos de líneas
xxxxxxx
xxxxxx

## 5.2 Gráficos de barras
xxxxxxx
xxxxxx

## 5.3 Histogramas
xxxxxxx
## 5.4 Diagramas de cajas y bigotes
xxxxxxx
xxxxxx
## 5.5 Gráficos de sectores
xxxxxx
xxxxxx

## 5.6 Gráficos de sectores
xxxxxx
xxxxxxxx
## 5.7 Matriz de correlación
xxxxx
xxxxxx
# 6. Conclusiones del ejercicio
xxxxxx
xxxxxx

