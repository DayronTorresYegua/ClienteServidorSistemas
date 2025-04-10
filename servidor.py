import socket

def iniciar_servidor(host='0.0.0.0', port=12345):
    """Servidor que maneja una única conexión y un único mensaje"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)  # Solo permite una conexión en cola
        print(f"Servidor listo en {host}:{port}")
        
        print("Esperando conexión...")
        conn, addr = s.accept()
        
        with conn:
            print(f"Conexión aceptada de {addr}")
            data = conn.recv(1024)  # Recibe el mensaje
            
            if data:
                mensaje = data.decode('utf-8')
                print(f"Mensaje recibido: {mensaje}")
                
                # Procesamiento según el protocolo
                respuesta = "hola " + mensaje.split()[1] + "2" if mensaje.startswith("hola ") else "Mensaje no reconocido"
                
                conn.sendall(respuesta.encode('utf-8'))
                print("Respuesta enviada, cerrando conexión")

if __name__ == "__main__":
    iniciar_servidor()