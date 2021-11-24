from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo

from flask_opentracing import FlaskTracing
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
import logging

from random import randint
from time import sleep

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

metrics = GunicornInternalPrometheusMetrics(app)

logging.getLogger("").handlers = []
logging.basicConfig(format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

def init_tracer(service):

    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
        },
        service_name=service,
        validate=True,
        metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer("backend")
flask_tracer = FlaskTracing(tracer, True, app)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)


# generates delays from 60 to 130 ms, as if the real work performed (eg.request remote API-site)
def delay_generator():
    delay = randint(6, 13) / 100
    return delay


@app.route("/")
def homepage():
    message = "Hello World"
    with tracer.start_span("homepage") as span:
        span.set_tag("message", message)
        sleep(delay_generator())
    return message


@app.route("/api")
def my_api():
    delay = delay_generator()
    answer = f'I did something in {delay*1000} ms'
    with tracer.start_span("my_api_worker") as span:
        span.set_tag("job_name", "some_data_handler")
        sleep(delay)
    return jsonify(response=answer)


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
