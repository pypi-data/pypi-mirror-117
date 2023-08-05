# Intro

Monitoring template is a Python library for easy start of microservice with Loki Logger, Tracer and Prometheus metrics inside

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install monitoring_template
```

## Settings (Environment Variables)
| Environment Name | Decription | Default Value |
| :---: | :---: | :---: |
| SERVICE_NAME | Name of your service | monitoring_template |
| LOG_LEVEL | Logging level to Loki | DEBUG |
| LOKI_SERVER | IP Address of Loki to push logs | 127.0.0.1 |
| LOKI_PORT | Loki Port | 3100 |
| JAEGER_SERVER | IP Address of Jaeger to push traces | 127.0.0.1 |
| JAEGER_PORT | Jaeger Port | 6831 |

## Usage

### Loki Logging

```python
from monitoring_template.tools.logger import get_logger

logger = get_logger()

logger.info(
    msg=f"Some Message in case of success",
    extra={"tags": {"label_1": "value_1"}}
)

logger.error(
    msg=f"Some Message in case of error",
    extra={"tags": {"label_1": "value_1"}}
)

```

### Prometheus metrics

```python
# How to describe metrics inside your service. 
# More details - https://github.com/prometheus/client_python

from prometheus_client import Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)
```

```python
# How to run Prom Metrics with Flask
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import os


def start_flask():
    new_app = Flask(__name__)

    metrics = PrometheusMetrics(new_app)
    new_app.wsgi_app = DispatcherMiddleware(new_app.wsgi_app, {'/metrics': make_wsgi_app()})
    new_app.secret_key = os.urandom(12)
    new_app.run(
        debug=False,
        port=8080,
        host="127.0.0.1",
        threaded=False
    )


def main():
    start_flask()


if __name__ == "__main__":
    main()
```
### Traces

```python
from monitoring_template.tools.tracer import get_tracer
import time

tracer = get_tracer()


def process_request(t):
    """A dummy function that takes some time."""
    with tracer.start_as_current_span("core-endpoint-health-get"):
        time.sleep(t)
```
