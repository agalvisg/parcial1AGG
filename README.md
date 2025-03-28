# parcial1AGG
## Sistema de Procesamiento de Imágenes Satelitales.

Este proyecto simula un sistema de procesamiento de imágenes satelitales utilizando programación paralela con hilos (threading) y procesos (multiprocessing).

### Estructura del Proyecto

- satelite.py: Simula satélites que generan imágenes y las almacenan en imagenes_pendientes.json.

- servidor.py: Procesa las imágenes pendientes y las guarda en imagenes_procesadas.json utilizando múltiples procesos.

- imagenes_pendientes.json: Archivo donde se almacenan las imágenes generadas que aún no han sido procesadas. Este archivo se creará en caso de no existir.

- imagenes_procesadas.json: Archivo donde se almacenan las imágenes ya procesadas. Este archivo se creará en caso de no existir.

- sistema.log: Archivo de registro donde se documentan los eventos y errores. Este archivo se creará en caso de no existir


### Ejecución

1. Ejecutar los satélites

Abre una terminal y ejecuta:

python satelite.py

Esto iniciará la generación de imágenes, las cuales se guardarán en imagenes_pendientes.json.

2. Ejecutar el servidor

Abre otra terminal y ejecuta:

python servidor.py

Esto iniciará los procesos encargados de procesar las imágenes pendientes y guardarlas en imagenes_procesadas.json.

### Funcionamiento

Los satélites generan imágenes cada 5 segundos y las almacenan en un JSON.

El servidor ejecuta múltiples procesos trabajadores que:

Revisan si hay imágenes pendientes.

Procesan cada imagen con un retraso simulado de 15 segundos.

Guardan las imágenes procesadas en otro JSON.

Si no hay imágenes pendientes, esperan 10 segundos antes de revisar nuevamente.

El sistema imprime el progreso en la consola y guarda logs de eventos y errores en sistema.log.

### Consideraciones

Si imagenes_pendientes.json no existe, se crea automáticamente.

Se manejan excepciones para evitar fallos en la ejecución.

Se implementa logging para monitorear el comportamiento del sistema.

En caso de que no se hayan generado más imágenes hay qeu finalizar el proceso del servidor manualmente con crtl+c.