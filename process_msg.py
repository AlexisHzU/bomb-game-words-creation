import threading
import itertools
import time

finalizar = threading.Event()

def animacion():
    for c in itertools.cycle("|/-\\"):
        if finalizar.is_set():
            break
        print(f"\rProcesando... {c}", end="", flush=True)
        time.sleep(0.1)

def start():
    # Iniciar la animación
    hilo = threading.Thread(target=animacion)
    hilo.start()
    while finalizar.is_set():
        time.sleep(0.5)  # Simula trabajo