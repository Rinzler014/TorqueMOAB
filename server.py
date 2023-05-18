import socket
import json

# Datos del servidor
host = 'localhost'
port = 65432

#Lista de Espera

queue = {}

counter = 0

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al puerto y dirección del servidor
sock.bind((host, port))

# Escuchar conexiones entrantes (máximo 1)
sock.listen(1)

# Esperar por una conexión
print("Esperando conexión...")
conn, addr = sock.accept()
print("Conexión establecida desde:", addr)

# Ciclo para recibir y enviar mensajes continuamente
while True:
    
    # Recibir el mensaje del cliente
    operation = conn.recv(1024).decode()
    operation = json.loads(operation)
    
    queue[operation["execution_time"]] = operation
    
    print("Mensaje Agregado a la Lista de Espera:", operation)

    if operation["command"] == 'exit':
        
        operation = json.dumps(operation)
        
        # Enviar el mensaje al tercer archivo a través de sockets
        archivo_host = 'localhost'
        archivo_port = 65433

        # Crear un nuevo socket TCP/IP para el archivo de impresión
        archivo_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectar el socket al archivo de impresión
        archivo_sock.connect((archivo_host, archivo_port))

        # Enviar el mensaje al archivo de impresión
        archivo_sock.sendall(operation.encode())

        # Cerrar la conexión con el archivo de impresión
        archivo_sock.close()
        
        break
    
    if len(queue) == 3:
        
        while len(queue) > 0:
        
            operation = queue[min(queue)]
            operation = json.dumps(operation)
            queue.pop(min(queue))
            
            # Enviar el mensaje al tercer archivo a través de sockets
            archivo_host = 'localhost'
            archivo_port = 65433

            # Crear un nuevo socket TCP/IP para el archivo de impresión
            archivo_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Conectar el socket al archivo de impresión
            archivo_sock.connect((archivo_host, archivo_port))

            # Enviar el mensaje al archivo de impresión
            archivo_sock.sendall(operation.encode())

            # Cerrar la conexión con el archivo de impresión
            archivo_sock.close()

# Cerrar la conexión con el cliente
conn.close()
