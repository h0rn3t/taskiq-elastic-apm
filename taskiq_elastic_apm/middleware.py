from logging import getLogger
from typing import Any

import elasticapm
from taskiq.abc.middleware import TaskiqMiddleware
from taskiq.message import TaskiqMessage
from taskiq.result import TaskiqResult

logger = getLogger("taskiq.elastic_apm")


class ElasticApmMiddleware(TaskiqMiddleware):
    """
    Middleware that integrates Elastic APM monitoring for workers.

    This middleware sets up an Elastic APM client and captures performance
    and error data for tasks being executed.

    :param server_url: The URL of the Elastic APM server.
    :param service_name: The name of your service as registered in Elastic APM.
    :param environment: The deployment environment ('production', 'development', etc.).
    :param config: Additional configuration options for Elastic APM client.
    """

    def __init__(
        self,
        client: elasticapm.Client,
    ) -> None:
        super().__init__()
        self.client = client
        elasticapm.instrument()
        logger.debug("Elastic APM client initialized")

    def startup(self) -> None:
        """
        Elastic APM startup.

        This function initializes any required resources for Elastic APM.
        """
        ...

    def pre_execute(
        self,
        message: "TaskiqMessage",
    ) -> "TaskiqMessage":
        """
        Function to begin capturing performance data.

        This function begins a transaction in Elastic APM before task execution.

        :param message: current message.
        :return: message
        """
        try:
            self.client.begin_transaction(transaction_type="taskiq")
        except Exception as e:
            logger.error(f"Failed to begin transaction with APM server: {e}")
        return message

    def post_execute(
        self,
        message: TaskiqMessage,
        result: TaskiqResult[Any],
    ) -> None:
        """
        Function to capture task execution details.

        This function sends performance data and error details (if any) to Elastic APM.

        :param message: received message.
        :param result: result of the execution.
        """
        try:
            if result.is_err:
                self.client.capture_exception()
                self.client.end_transaction(name=message.task_name, result="error")
            else:
                self.client.end_transaction(name=message.task_name, result="success")
        except Exception as e:
            logger.error(f"Failed to send data to APM server: {e}")

    def post_save(
        self,
        message: "TaskiqMessage",
        result: "TaskiqResult[Any]",
    ) -> None:
        """
        Method to run after saving task result.

        This can be used to perform any clean-up or additional data capture after task result is saved.

        :param message: received message.
        :param result: result of execution.
        """
        # Implement any post-save logic if necessary

