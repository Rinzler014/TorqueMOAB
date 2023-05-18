import socket

# Datos del servidor
host = 'localhost'
port = 65432

# Mensaje a enviar
mensaje = "¡Hola, servidor!"

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
sock.connect((host, port))

# Enviar el mensaje al servidor
sock.sendall(mensaje.encode())

# Cerrar la conexión
sock.close()
