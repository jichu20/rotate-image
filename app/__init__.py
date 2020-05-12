from flask import Flask
from flask_restful import Api
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
api = Api(app)

METRICS = PrometheusMetrics(app)
