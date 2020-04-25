# Rotate images

## Instalación

Para instalar el entorno es necesario ejecutar los siguientes pasos, los cuales generarn un entorno virtual e instala las dependencias necesarias para su correcto funcionamiento

```sh
# Ruta que contiene los entornos virtuales
cd /Users/borjasanchez/code/python/virtualenv

export VENV=rotate-image # Nombre del entorno virtual

# Instalar virtual env en macOS con Homebrew de los entornos virtuales
pip install virtualenv

# Creación de un nuevo entorno virtual
virtualenv $VENV --python=python3

# Activación del entorno virtual
source ./$VENV/bin/activate

# Descarga de las dependencias desde el path del proyecto
pip install -r requirements.txt

```

## Test

Para probar el servicio, se puede ejecutar el siguiente comando

```sh
curl --location --request POST 'http://0.0.0.0:8080/v1/ns/borja/image/rotate' \
    --form 'file=@/Users/borja.sanchez/Code/python/workspace/rotate-image/resources/IMG_3536.jpg' \
    --output ./descarga.jpg
```

# Referencias Externas

Para el desarrollo del proyecto se ha seguido la [siguiente guia](https://medium.com/analytics-vidhya/ocr-on-region-of-interest-roi-in-image-using-opencv-and-tesseract-a7cab6ff18b3)

Para la creación del pipeline en github con publicación [docker](https://www.prestonlamb.com/blog/creating-a-docker-image-with-github-actions)
## Docker


Para generar la imagen docker ejecutamos `docker build --rm -f "dockerfile" -t jichu20/rotate-image:latest "."`

Para correr un contenedor docker de esta imagen `docker run -p 8080:8080 jichu20/rotate-image:latest`
