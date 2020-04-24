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

# Referencias Externas


## Docker

Para generar la imagen docker ejecutamos `docker build --rm -f "dockerfile" -t jichu20/rotate-image:latest "."`

Para correr un contenedor docker de esta imagen `docker run -p 8080:8080 jichu20/rotate-image:latest`
