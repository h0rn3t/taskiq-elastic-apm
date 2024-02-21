[![ci](https://img.shields.io/badge/Support-Ukraine-FFD500?style=flat&labelColor=005BBB)](https://img.shields.io/badge/Support-Ukraine-FFD500?style=flat&labelColor=005BBB)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pip](https://img.shields.io/pypi/v/taskiq-elastic-apm?color=blue)](https://pypi.org/project/taskiq-elastic-apm/)
[![Downloads](https://static.pepy.tech/badge/taskiq-elastic-apm)](https://pepy.tech/project/taskiq-elastic-apm)

# TaskIQ Elastic APM Middleware

TaskIQ Elastic APM Middleware is a Python library providing easy integration of Elastic APM monitoring into TaskIQ task processing. This middleware enables efficient tracking and analysis of task performance and errors, leveraging the capabilities of Elastic APM.

## Features

- Easy integration with TaskIQ workers.
- Automatic performance and error tracking for tasks.
- Customizable to fit various Elastic APM configurations.

## Installation

You can install the TaskIQ Elastic APM Middleware directly from PyPI:

```bash
pip install taskiq-elastic-apm
```

Usage
To use the middleware in your TaskIQ project, simply import and add it to your TaskIQ application:

python
Copy code
from taskiq import Taskiq
from taskiq_elastic_apm_middleware import ElasticApmMiddleware

# Create your Taskiq instance
``` python


broker = AioPikaBroker(
    url=settings.CELERY_BROKER_URL,
    queue_name=settings.CELERY_DEFAULT_QUEUE,
    exchange_name=settings.CELERY_DEFAULT_QUEUE,
).with_middlewares(
    ElasticApmMiddleware(
        client=apm,
    )
)


```

# Define your tasks and start your application as usual
### Configuration

You can configure the middleware by passing parameters to ElasticApmMiddleware.

The main parameters are:

**client**: elasticapm.Client - The Elastic APM client instance to use. If not provided, a new client will be created using the following parameters:
``` python
from elasticapm.contrib.starlette import make_apm_client

apm_settings = {
    "ENABLED": settings.APM_ENABLE,
    "ENVIRONMENT": settings.ENVIRONMENT,
    "SERVER_URL": settings.APM_SERVER_URL,
    "SERVICE_NAME": settings.SERVICE_NAME,
    "SECRET_TOKEN": settings.APM_SECRET_TOKEN,
    "CAPTURE_BODY": settings.APM_CAPTURE_BODY,
    "CAPTURE_HEADERS": settings.APM_CAPTURE_HEADERS,
    "COLLECT_LOCAL_VARIABLES": settings.APM_COLLECT_LOCAL_VARIABLES,
    "AUTO_LOG_STACKS": settings.APM_AUTO_LOG_STACKS,
}

apm = make_apm_client(apm_settings)
```
