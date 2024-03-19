##########################################################
#
# Copyright (C) 2023-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

import grpc
from grpc import _channel
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc


class BaseClient(object):

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 50051,
    ) -> 'BaseClient':
        """
            BaseClient Constructor.

            Parameters:
                - host (str): Server hostname. Defaults to `localhost`.
                - port (int): Server port number. Defaults to `50051`.
        """
        self.host = host
        self.port = port
        self.target = f'{host}:{port}'

        self.service: str = None
        self.sub = None
        self.channel: _channel   = None
        self.health_stub: health_pb2_grpc.HealthStub = None


    def is_server_serving(self, timeout: int = 1) -> bool:
        """
            Returns whether server is up and serving.

            Parameters:
                - timeout (int): Timeout for future request. Defaults to `1`.

            Returns:
                - (bool): Server readiness status.
        """
        try:
            grpc.channel_ready_future(self.channel).result(timeout)
            return True
        except grpc.FutureTimeoutError:
            return False
        except Exception as ex:
            raise ex


    def is_service_serving(self, rpc: str) -> bool:
        """
            This method sends a HealthCheckRequest to the health check service
            to determine the health status of the specified service. It returns
            True if the service is serving requests, and False if it's not serving.

            Parameters:
                - rpc (str): RPC name of the service.

            Returns:
                - bool: True if the service is healthy (serving requests), False otherwise.
        """
        service_rpc = f'{self.service}.{rpc}'
        request = health_pb2.HealthCheckRequest(service=service_rpc)
        response = self.health_stub.Check(request)

        return {
            health_pb2.HealthCheckResponse.SERVING: True,       # Healthy
            health_pb2.HealthCheckResponse.NOT_SERVING: False   # Not healthy
        }[response.status]
