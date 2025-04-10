import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("Uso: python client.py <ip_servidor> <mensaje>")
        sys.exit(1)
    
    host = sys.argv[1]
    mensaje = ' '.join(sys.argv[2:])  # Permite mensajes con espacios
    port = 12345
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Conectado a {host}:{port}")
            
            s.sendall(mensaje.encode('utf-8'))
            data = s.recv(1024)
            
            print(f"Respuesta del servidor: {data.decode('utf-8')}")
            
        except ConnectionRefusedError:
            print(f"No se pudo conectar al servidor {host}:{port}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()