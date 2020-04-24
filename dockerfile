FROM python:3

# Exponemos el puerto 8080
EXPOSE 8080 8080

# Instalamos las dependencias de necesarias apra el ocr
# RUN apt-get update \
#     && apt-get install poppler-utils -y \
#     && apt-get clean \
#     && apt-get autoremove
RUN ["/bin/bash", "apt-get", "update", \
    "apt-get","install","poppler-utils", "-y", \
    "apt-get", "clean" \
    "apt-get", "autoremove"

# Copiamos el proyecto al contenedor
# RUN make /app
COPY . /app

# Instalamos las dependencias
# RUN pip install -r /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Ejecutamos la app
CMD python /app/app.py
