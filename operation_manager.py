import socket

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
    mensaje = conn.recv(1024).decode()
    
    if mensaje == 'exit':
        break

    # Mostrar el mensaje en pantalla
    print("Mensaje recibido:", mensaje)


conn.close()