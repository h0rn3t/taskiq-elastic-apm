# TaskIQ Elastic APM Middleware

TaskIQ Elastic APM Middleware is a Python library providing easy integration of Elastic APM monitoring into TaskIQ task processing. This middleware enables efficient tracking and analysis of task performance and errors, leveraging the capabilities of Elastic APM.

## Features

- Easy integration with TaskIQ workers.
- Automatic performance and error tracking for tasks.
- Customizable to fit various Elastic APM configurations.

## Installation

You can install the TaskIQ Elastic APM Middleware directly from PyPI:

```bash
pip install taskiq-elastic-apm-middleware
```

Usage
To use the middleware in your TaskIQ project, simply import and add it to your TaskIQ application:

python
Copy code
from taskiq import Taskiq
from taskiq_elastic_apm_middleware import ElasticApmMiddleware

# Create your Taskiq instance
``` python

middleware = ElasticApmMiddleware(server_url="http://apm-server:8200", service_name="your_service")
middleware.set_broker(broker)

```

# Define your tasks and start your application as usual
Configuration

You can configure the middleware by passing parameters to ElasticApmMiddleware.
The main parameters are:

**server_url**: The URL of your Elastic APM server.

**service_name**: The name of your service as registered in Elastic APM.

**environment**: (Optional) The deployment environment, e.g., 'production', 'development'.

**config**: (Optional) A dictionary with additional configuration options for the Elastic APM client.