import socket
import sys

def servidor():
    if len(sys.argv) != 2:
        print("Uso: python servidor.py <ip_esperada>")
        sys.exit(1)
    
    ip_esperada = sys.argv[1]
    host = '0.0.0.0'  # Escucha en todas las interfaces
    port = 5000       # Puerto específico
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f"Servidor escuchando en {host}:{port}")
        print(f"IP esperada del cliente: {ip_esperada}")
        
        s.listen(1)
        print("Esperando conexión...")
        
        # Aceptar una sola conexión
        conn, addr = s.accept()
        with conn:
            print(f"Conexión establecida desde {addr[0]}:{addr[1]}")
            
            if addr[0] != ip_esperada:
                print(f"Advertencia: Conexión de IP no esperada ({addr[0]})")
            
            # Recibir hasta 3 mensajes (puedes ajustar este número)
            for _ in range(3):
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Mensaje de {addr[0]}: {data.decode('utf-8')}")
            
            print("Fin de la comunicación")

if __name__ == "__main__":
    servidor()