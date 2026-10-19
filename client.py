import socket

IP_ANDROID = "192.168.1.130"
PUERTO = 5000

def enviar_senal(senal):
    with socket.create_connection(
        (IP_ANDROID, PUERTO),
        timeout=5
    ) as cliente:
        cliente.sendall((senal + "\n").encode("utf-8"))

    print("Señal enviada:", senal)


enviar_senal("SENAL_C")