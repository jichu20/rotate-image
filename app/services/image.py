import cv2
import io
import os
import numpy as np
from flask_restful import Resource
from flask_api import status
from flask import request, send_file

from ..commons.mime_types import CONTENT_TYPE_IMAGE_JPG
from ..core import utils, image


class Image(Resource):
    def post(self, ns):
        if "file" not in request.files:
            return {"_error": "No file selected"}, status.HTTP_400_BAD_REQUEST

        file = request.files["file"]

        if file and not utils.allowed_file(file.filename):
            return (
                # {"_error": f"Selected file is not valid, only {utils.ALLOWED_EXTENSIONS} is allowed"},
                {
                    "_error": "Selected file is not valid, only %s is allowed"
                    % {utils.listToString(utils.ALLOWED_EXTENSIONS)}
                },
                status.HTTP_400_BAD_REQUEST,
            )

        nparr = np.fromstring(file.read(), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR in OpenCV 3.1

        img_rotated = image.orientation_correction(img_np)

        cv2.imwrite(file.filename, img_rotated)

        with open(file.filename, "rb") as bites:
            bytes_image = io.BytesIO(bites.read())

        os.remove(file.filename)
        return send_file(bytes_image, attachment_filename=file.filename, mimetype=CONTENT_TYPE_IMAGE_JPG)
