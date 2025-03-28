import multiprocessing
import time
import json
import os
import logging

# Configuración del logging
logging.basicConfig(filename="sistema.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

IMAGENES_JSON = "imagenes_pendientes.json"
PROCESADAS_JSON = "imagenes_procesadas.json"

def procesar_imagen(imagen):
    """Simula el procesamiento de la imagen."""
    try:
        print(f"Procesando imagen {imagen}")
        time.sleep(15)  # Simula un procesamiento que tarda 15 segundos
        imagen["procesado"] = True
        guardar_imagen_procesada(imagen)
        logging.info(f"Imagen procesada: {imagen}")
        print(f"Imagen procesada y guardada: {imagen}")
    except Exception as e:
        logging.error(f"Error procesando imagen: {e}")
        print(f"Error procesando imagen: {e}")

def guardar_imagen_procesada(imagen):
    """Guarda la imagen procesada en un archivo JSON."""
    try:
        if os.path.exists(PROCESADAS_JSON):
            with open(PROCESADAS_JSON, "r") as file:
                imagenes = json.load(file)
        else:
            imagenes = []

        imagenes.append(imagen)
        with open(PROCESADAS_JSON, "w") as file:
            json.dump(imagenes, file, indent=4)
    except Exception as e:
        logging.error(f"Error guardando imagen procesada: {e}")
        print(f"Error guardando imagen procesada: {e}")

def cargar_imagenes_pendientes():
    """Carga las imágenes pendientes del JSON."""
    if not os.path.exists(IMAGENES_JSON):
        return []

    with open(IMAGENES_JSON, "r") as file:
        return json.load(file)

def limpiar_pendientes():
    """Limpia el archivo de imágenes pendientes después de procesarlas."""
    with open(IMAGENES_JSON, "w") as file:
        json.dump([], file)

def worker():
    """Proceso trabajador que se encarga de procesar las imágenes."""
    while True:
        imagenes = cargar_imagenes_pendientes()
        if imagenes:
            imagen = imagenes.pop(0)
            procesar_imagen(imagen)
            with open(IMAGENES_JSON, "w") as file:
                json.dump(imagenes, file)
        else:
            print("No hay imágenes pendientes. Esperando...")
            time.sleep(10)  # Espera 10 segundos antes de revisar nuevamente

if __name__ == "__main__":
    print("Iniciando servidor de procesamiento...")
    process1 = multiprocessing.Process(target=worker)
    process2 = multiprocessing.Process(target=worker)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
