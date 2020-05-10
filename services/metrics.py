
import prometheus_client
from commons.mime_types import CONTENT_TYPE_TEST_PLAIN
from flask_restful import Resource
from flask.wrappers import Response
# from commons.app_metrics import METRICS as g_metrics


class Metrics(Resource):

    # @g_metrics.do_not_track()
    def get(self):
        return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_TEST_PLAIN)
