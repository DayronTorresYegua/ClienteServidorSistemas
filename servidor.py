import socket
import sys

def servidor():
    if len(sys.argv) != 2:
        print("Uso: python servidor.py <ip_cliente>")
        sys.exit(1)
    
    host = '0.0.0.0'  # Escucha en todas las interfaces
    port = 5000       # Puerto específico
    ip_cliente = sys.argv[1]
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f"Servidor escuchando en {host}:{port}")
        print(f"IP del cliente configurada: {ip_cliente}")
        
        s.listen(1)
        print("Esperando conexión...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Conexión establecida desde {addr[0]}:{addr[1]}")
            
            if addr[0] != ip_cliente:
                print(f"Advertencia: Conexión de IP no esperada ({addr[0]})")
            
            data = conn.recv(1024)
            if not data:
                print("No se recibió mensaje")
            else:
                print(f"Mensaje de {addr[0]}: {data.decode('utf-8')}")

if __name__ == "__main__":
    servidor()