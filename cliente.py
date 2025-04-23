import socket
import sys

def cliente():
    if len(sys.argv) != 3:
        print("Uso: python cliente.py <ip_servidor> <mensaje>")
        sys.exit(1)
    
    host = sys.argv[1]
    mensaje = sys.argv[2]
    port = 5000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Conectado al servidor {host}:{port}")
            s.sendall(mensaje.encode('utf-8'))
            print("Mensaje enviado correctamente")
        except ConnectionRefusedError:
            print("Error: No se pudo conectar al servidor")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    cliente()