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

**client**: elasticapm.Client - The Elastic APM client instance to use. If not provided, a new client will be created using the following parameters.
