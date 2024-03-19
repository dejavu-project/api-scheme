##########################################################
#
# Copyright (C) 2023-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

import grpc
from concurrent import futures
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

# Third-party imports
from src.utils import logger


class BaseServer(object):

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 50051,
        n_workers: int = 1,
        healthcheck_n_workers: int = 1,
    ) -> 'BaseServer':
        """
            BaseServer Constructor.

            Parameters:
                - host (str): Server hostname. Defaults to `localhost`.
                - port (int): Server port number. Defaults to `50051`.
                - n_workers (int): Number of threads. Defaults to `1`.
                - healthcheck_n_workers (int): Number of threads for healthchec. Defaults to `1`.
        """
        self.n_workers = n_workers
        self.target = f'{host}:{port}'

        # Server
        self.thread_pool = futures.ThreadPoolExecutor(n_workers)
        self.server = grpc.server(self.thread_pool)
        self.server.add_insecure_port(self.target)

        # Healthcheck service
        self.health_servicer: health.HealthServicer
        self._configure_health_server(healthcheck_n_workers)


    def start(self) -> None:
        """
            Starts the server in blocking mode.
        """
        logger.debug(f"Listening on '{self.target}'")
        self.server.start()
        self.server.wait_for_termination()


    def stop(self) -> None:
        """
            Stops the server permanently.
        """
        self.health_servicer.enter_graceful_shutdown()  # Mark services as `NOT_SERVING`
        self.server.stop()


    def _configure_health_server(self, n_threads: int = 1):
        """
            Configures creates a HealthServicer instance with experimental non-blocking
            behavior and a thread pool executor with a maximum of 10 workers. It then adds
            the HealthServicer instance to the gRPC server. Additionally, it starts a daemon
            thread to toggle the health status of the service periodically.

            Parameters:
                - n_threads (int): Number of thread workers. Defaults to `1`.

            Returns:
                - None
        """
        self.health_servicer = health.HealthServicer(
            experimental_non_blocking = True,
            experimental_thread_pool = futures.ThreadPoolExecutor(max_workers=n_threads),
        )
        health_pb2_grpc.add_HealthServicer_to_server(self.health_servicer, self.server)


    def set_service_to_serving(self, service: str) -> None:
        """
            This method updates the health status of the specified service to `SERVING`.

            Parameters:
                - service (str): The name of the service whose health status will be set to SERVING.

            Returns:
                - None
        """
        self.health_servicer.set(service, health_pb2.HealthCheckResponse.SERVING)


    def set_service_to_not_serving(self, service: str) -> None:
        """
            This method updates the health status of the specified service to `NOT_SERVING`.

            Parameters:
                - service (str): The name of the service whose health status will be set to SERVING.

            Returns:
                - None
        """
        self.health_servicer.set(service, health_pb2.HealthCheckResponse.NOT_SERVING)
