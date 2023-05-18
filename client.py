import socket
import json

# Datos del servidor
host = 'localhost'
port = 65432

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
sock.connect((host, port))

# Ciclo para enviar mensajes al servidor
while True:
    
    execution_time = int(input("Enter the execution time (in seconds): "))
    max_memory = input("Enter the maximum memory (in MB): ")
    cores = input("Enter the number of cores: ")
    mensaje = input("Enter the operation ('exit' para terminar): ")
    
    operation = json.dumps({
        "execution_time": execution_time,
        "max_memory": max_memory,
        "cores": cores,
        "command": mensaje
    })
    
    if mensaje == 'exit':
        # Enviar el mensaje al servidor
        sock.sendall(operation.encode())
        break

    # Enviar el mensaje al servidor
    sock.sendall(operation.encode())


# Cerrar la conexión
sock.close()
