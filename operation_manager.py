import socket
import pandas as pd
import numpy as np
import datetime
import time
import json
import zipfile
import matplotlib.pyplot

data = pd.read_csv('data.csv')

block = pd.DataFrame(data,columns=['Zipcode','Start_Lat', 'Start_Lng','Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway',
       'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal',
       'Turning_Loop'])

block["Zipcode"].value_counts()

def zipDF(zipcode,df):
  DataF=df.loc[block['Zipcode'] == zipcode]
  return(DataF)

def start_co(df):
  lat=df['Start_Lat'].head(1)
  lng=df['Start_Lng'].head(1)
  return(lat.values,lng.values)

def max_acci(df):
  df2=pd.DataFrame(df,columns=['Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway',
       'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal',
       'Turning_Loop'])
  S=df2.sum()
  s_value=S.max()
  s_maxx = S.astype("int").idxmax()
  print(s_maxx, "", s_value)

# Datos del servidor
host = 'localhost'
port = 65433

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al puerto y dirección del servidor de archivo de impresión
sock.bind((host, port))

while True:

    # Escuchar conexiones entrantes (máximo 1)
    sock.listen(1)

    # Esperar por una conexión
    print("Esperando conexión...")
    conn, addr = sock.accept()
    print("Conexión establecida desde:", addr)

    # Recibir el mensaje del servidor
    operation = conn.recv(1024).decode('utf-8')
    operation = json.loads(operation)
    
    # Mostrar el mensaje en pantalla
    
    print("Mensaje recibido:", operation)
    
    if operation["zipcode"] == 'exit':
        break
    
    df=zipDF(operation["zipcode"],block)
    la,ln=start_co(df)
    print(" la latitud es: ", la.item(0))
    print(" la longitud es: ",ln.item(0))

    print("-"*30,"\n")
    max_acci(df)
    

conn.close()