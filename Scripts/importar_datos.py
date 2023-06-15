import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine

host = 'localhost'
user = 'root'
password = 'xxxxxxx'
database = 'pluviometria'

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
    df.to_sql('historico', con=engine, if_exists='append', index=False)  # Carga los datos en la tabla
    print(f"Archivo '{file}' cargado correctamente.")

# Cerrar la conexión
connection.close()



