import socket
import pandas as pd
import numpy as np
import datetime
import time
import json

data = pd.read_csv('data.csv')

def state_with_the_most_accidents():
    
    states = data["State"].values
    states = pd.DataFrame(states, columns=["State"])
    return states["State"].value_counts()

def hours_with_most_accidents():
    
    dates = data["Start_Time"].values

    hours = []

    for date in dates:
        date = date.split(" ")
        date = date[1].split(":")
        date = date[0]
        
        hours.append(date + ":00")
    
    hours = pd.DataFrame(hours, columns=["Start_Time"])
    hours = hours["Start_Time"].value_counts().head(5)
    times = []
    
    for hour in hours.index:
        hour = hour.split(":")
        hour = hour[0]
        times.append("Day" if int(hour) < 17 else "Night")
        
    return pd.DataFrame({
        "Hour": hours.index,
        "Accidents": hours.values,
        "Time": times
    })
    
def day_with_most_accidents():
    
    dates = data["Start_Time"].values    
    days = []

    for date in dates:
        date = date.split(" ")
        date = date[0]
        
        day = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
        
        days.append(day)
            
    days = pd.DataFrame(days, columns=["Start_Time"])
    return days["Start_Time"].value_counts().head(1)

def time_with_most_cases():

    day = 0
    night = 0
    
    for index, time in enumerate(hours_with_most_accidents()["Time"]):
        if time == "Day": day += int(hours_with_most_accidents()["Accidents"][index])
        else: night += int(hours_with_most_accidents()["Accidents"][index])

    return day, night



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
    
    match operation["command"]:
        
        case "state_with_the_most_accidents":
            print(state_with_the_most_accidents())
        
        case "hours_with_most_accidents":
            print(hours_with_most_accidents())
            
        case "day_with_most_accidents":
            print(day_with_most_accidents())
        
        case "time_with_most_cases":
            print(time_with_most_cases())
            
        case "exit":
            break
            
        case _:
            print("Command not found")
    

conn.close()