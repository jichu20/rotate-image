# Importing necessary libraries
import cv2
import io
import os
import numpy as np
from flask_restful import Api, Resource
from flask_api import status
from flask import Flask, request, send_file
from core import utils, image
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
api = Api(app)

metrics = PrometheusMetrics(app)

# Métrica con información estatica, nos vale como healtcheck
metrics.info("service", "Name and version of service", version="0.1.0", service="rotate-image")


class Image(Resource):
    def post(self):
        if "file" not in request.files:
            return {"_error": "No file selected"}, status.HTTP_400_BAD_REQUEST

        file = request.files["file"]

        if file and not utils.allowed_file(file.filename):
            return (
                {"_error": f"Selected file is not valid, only {utils.ALLOWED_EXTENSIONS} is allowed"},
                status.HTTP_400_BAD_REQUEST,
            )

        nparr = np.fromstring(file.read(), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR in OpenCV 3.1

        img_rotated = image.orientation_correction(img_np)

        cv2.imwrite(file.filename, img_rotated)

        with open(file.filename, "rb") as bites:
            bytes_image = io.BytesIO(bites.read())

        os.remove(file.filename)
        return send_file(bytes_image, attachment_filename=file.filename, mimetype="image/jpg")


api.add_resource(Image, "/image/rotate", endpoint="image")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
