# -*- coding: utf-8 -*-
# Listado de extensiones pemritidas
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


# Función para validar las extensiones
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ", " + ele

    # return string
    return str1
