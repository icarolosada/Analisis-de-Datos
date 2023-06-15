# Preparación de Datos

Los datos utilizados en este proyecto fueron recopilados de varias fuentes en línea, incluyendo:

- NOAA (National Oceanic and Atmospheric Administration): [https://www.noaa.gov/]
- Embalses.net: [https://www.embalses.net/]
- DatosClima.es: [https://datosclima.es/index.htm]

Debido a la gran cantidad de archivos y la ineficiencia de la importación directa a MySQL, se optó por utilizar Python para realizar la carga de los datos. A continuación, se presenta el código utilizado:

A continuación, el código:
```
import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine

host = 'localhost'
user = 'root'
password = 'xxxxxxx'
database = 'pluviometria_espana100anos'

# Establecer conexión
connection = pymysql.connect(host=host, user=user, password=password, database=database)
print("Conexión establecida correctamente.")
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Lista de archivos CSV
folder_path = 'C:\\Users\\Icaro.DESKTOP-8VQB1F3\\Desktop\\Data Analyst\\Histórico del Clima\\Pluviometría\\EUROPA2023-04-15\\sp'
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
print(f"Número de archivos CSV encontrados: {csv_files}")

# Recorrer la lista de archivos CSV y realizar la carga
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path, header=None, delimiter=';')  # Lee el archivo CSV sin cabeceras
    df.columns = ['Id_estacion', 'fecha', 'temp_max', 'temp_min', 'lluvia', 'nieve', 'profundi_nieve']  # Asigna los nombres de columna
    df.to_sql('historico', con=engine, if_exists='append', index=False)   # Carga los datos en la tabla
    print(f"Archivo '{file}' cargado correctamente.")

# Cerrar la conexión
connection.close()
```

Una vez terminada la carga de datos con Python, se procede a la carga estándar desde consola y la limpieza de datos


### Inspeccion inicial de la tabla

```sql

DESCRIBE pluviometria_espana100anos.historico;
SELECT * FROM pluviometria_espana100anos.historico LIMIT 0, 10

```

### Tenemos dos columnas que no interesan para nuestro análisis

```sql
ALTER TABLE pluviometria_espana100anos.historico
DROP COLUMN nieve, DROP COLUMN profundi_nieve;
```

### El formato de varias columnas se modifican para que acepten decimales antes de la conversión a centrígrados

```sql
ALTER TABLE pluviometria_espana100anos.historico MODIFY temp_max DECIMAL(10, 1), MODIFY temp_min DECIMAL(10, 1);
```
### El formato de la temperatura están en decimas de grado, hay que hacer la conversión
```sql
UPDATE pluviometria_espana100anos.historico SET temp_max = temp_max / 10, temp_min = temp_min / 10;
```
### EL formato de la fecha no es consistente en todas las tablas, se modifica
```sql
UPDATE embalses SET FECHA = STR_TO_DATE(FECHA, '%Y-%m-%d');
```
### Continua la limpieza y se sustituye null por 0
```sql
UPDATE historico
SET temp_max = IFNULL(temp_max, 0),
    temp_min = IFNULL(temp_min, 0),
    lluvia = IFNULL(lluvia, 0),
    nieve = IFNULL(nieve, 0),
    profundi_nieve = IFNULL(profundi_nieve, 0)
WHERE fecha IS NULL
   OR temp_max IS NULL
   OR temp_min IS NULL
   OR lluvia IS NULL
   OR nieve IS NULL
   OR profundi_nieve IS NULL;
```
## Se comienza a sacar tablas para su posterior análisis 

### Agrupar cada estación por año y calcular la cantidad total de lluvia por año
```sql
SELECT Id_estacion, YEAR(fecha) AS total_año, SUM(lluvia) AS total_lluvia
FROM pluviometria_espana100anos.historico
GROUP BY Id_estacion, YEAR(fecha)
ORDER BY Id_estacion, YEAR(fecha);
```

### Obtener el total de lluvia por año sumando la lluvia de todas las estaciones
```sql
SELECT YEAR(fecha) AS total_año, SUM(lluvia) AS total_lluvia
FROM pluviometria_espana100anos.historico
GROUP BY YEAR(fecha)
ORDER BY YEAR(fecha);
```
### Sacar el nombre y la identificación de dos tablas usando join:
```sql
SELECT historico.Id_estacion, GROUP_CONCAT(DISTINCT estaciones.NOMBRE_ESTACION) AS nombres_estaciones
FROM historico
JOIN estaciones ON historico.Id_estacion = estaciones.ID
GROUP BY historico.Id_estacion
LIMIT 0, 1000;
```
### Debido a la gran cantidad de datos, hay que agrupar el total por 2 décadas para evitar el colapso del servidor
```sql
SELECT historico.Id_estacion, estaciones.NOMBRE_ESTACION, 
  CONCAT(FLOOR(YEAR(historico.fecha) / 20) * 20, 's') AS decada,
  SUM(historico.lluvia) AS total_lluvia
FROM historico
JOIN estaciones ON historico.Id_estacion = estaciones.ID
GROUP BY historico.Id_estacion, estaciones.NOMBRE_ESTACION, decada;
```
### Sacar tabla con cada estacion y su ubicacion en latitud y longitud
```sql
SELECT historico.Id_estacion, 
       estaciones.NOMBRE_ESTACION, 
       estaciones.LATITUD,
       estaciones.LONGITUD
FROM historico
JOIN estaciones ON historico.Id_estacion = estaciones.ID
GROUP BY historico.Id_estacion, estaciones.NOMBRE_ESTACION, estaciones.LATITUD, estaciones.LONGITUD
LIMIT 0, 1000;
```
### Sacar total de lluvia por año y por estación
```sql
SELECT historico.Id_estacion, estaciones.NOMBRE_ESTACION, YEAR(historico.fecha) AS año, SUM(historico.lluvia) AS total_lluvia
FROM historico
JOIN estaciones ON historico.Id_estacion = estaciones.ID
GROUP BY historico.Id_estacion, estaciones.NOMBRE_ESTACION, YEAR(historico.fecha);
```
### Media de lluvia por años
```sql
SELECT YEAR(fecha) AS años, AVG(lluvia) AS media_lluvia
FROM pluviometria_espana100anos.historico
GROUP BY YEAR(fecha);
```
   
