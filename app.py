# -*- coding: utf-8 -*-
# Importing necessary libraries

from services.metrics import Metrics
from services.image import Image
from flask_restful import Api
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from commons.app_metrics import METRICS as g_metrics

app = Flask(__name__)
api = Api(app)
g_metrics = PrometheusMetrics(app)

# Métrica con información estatica, nos vale como healtcheck
g_metrics.info("service", "Name and version of service", version="0.2.0", service="rotate-image")

api.add_resource(Image, "/v1/ns/<string:ns>/image/rotate", endpoint="image")
api.add_resource(Metrics, "/_service/metrics", endpoint="metrics")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
