import threading
import time
import json
import os
import logging

# Configuración del logging
logging.basicConfig(filename="sistema.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

IMAGENES_JSON = "imagenes_pendientes.json"

def guardar_imagen(imagen):
    """Guarda la imagen en el archivo JSON."""
    try:
        if os.path.exists(IMAGENES_JSON):
            with open(IMAGENES_JSON, "r") as file:
                imagenes = json.load(file)
        else:
            imagenes = []

        imagenes.append(imagen)
        with open(IMAGENES_JSON, "w") as file:
            json.dump(imagenes, file, indent=4)

        logging.info(f"Imagen guardada: {imagen}")
        print(f"Imagen guardada: {imagen}")
    except Exception as e:
        logging.error(f"Error guardando imagen: {e}")
        print(f"Error guardando imagen: {e}")

class SateliteThread(threading.Thread):
    def __init__(self, nombre, cantidad):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.cantidad = cantidad

    def run(self):
        print(f"{self.nombre} iniciando generación de imágenes...")
        for i in range(self.cantidad):
            time.sleep(5)  # Simula la generación de una imagen cada 5 segundos
            imagen = {"satellite": self.nombre, "imagen_id": i + 1, "timestamp": time.time()}
            guardar_imagen(imagen)
        print(f"{self.nombre} ha terminado la generación de imágenes.")

if __name__ == "__main__":
    sat1 = SateliteThread("Satélite_A", 5)
    sat2 = SateliteThread("Satélite_B", 5)

    sat1.start()
    sat2.start()

    sat1.join()
    sat2.join()

    print("Todos los satélites han terminado.")
