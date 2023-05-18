import socket

# Datos del servidor
host = 'localhost'
port = 65432

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
sock.connect((host, port))

# Ciclo para enviar mensajes al servidor
while True:
    
    mensaje = input("Enter the operation ('exit' para terminar): ")

    if mensaje == 'exit':
        # Enviar el mensaje al servidor
        sock.sendall(mensaje.encode())
        break

    # Enviar el mensaje al servidor
    sock.sendall(mensaje.encode())

# Cerrar la conexión
sock.close()
