from . import app  # noqa - Importando por el archivo wsgi.py
from . import api
from . import METRICS as g_metrics

from .services.image import Image
from .services.metrics import Metrics

# Métrica con información estatica, nos vale como healtcheck
g_metrics.info("service", "Name and version of service", version="0.2.0", service="rotate-image")

api.add_resource(Image, "/v1/ns/<string:ns>/image/rotate", endpoint="image")
api.add_resource(Metrics, "/_service/metrics", endpoint="metrics")
