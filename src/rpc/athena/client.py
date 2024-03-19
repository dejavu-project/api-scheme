##########################################################
#
# Copyright (C) 2023-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

import grpc
from grpc_health.v1 import health_pb2_grpc

# Third-party imports
from src.rpc.base_client import BaseClient
from protos.athena import athena_pb2
from protos.athena import athena_pb2_grpc
from google.protobuf.json_format import MessageToDict


class AthenaClient(BaseClient):

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 50051
    ) -> 'AthenaClient':
        """
            AthenaClient Constructor.

            Parameters:
                - host (str): Server hostname. Defaults to `localhost`.
                - port (int): Server port number. Defaults to `50051`.
        """
        super().__init__(host, port)

        self.service = 'Athena'
        self.channel = grpc.insecure_channel(self.target)

        # Stubs
        self.stub = athena_pb2_grpc.AthenaStub(self.channel)
        self.health_stub = health_pb2_grpc.HealthStub(self.channel) # Healthcheck


    def get_backtest(self) -> dict:
        request = athena_pb2.GetBacktestRequest()   # Create request
        response = self.stub.GetBacktest(request)   # Get response
        return MessageToDict(response)              # Return as dict
