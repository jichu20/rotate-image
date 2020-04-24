# Listado de extensiones pemritidas
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


# Función para validar las extensiones
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
