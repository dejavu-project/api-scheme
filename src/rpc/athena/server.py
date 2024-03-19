##########################################################
#
# Copyright (C) 2023-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

import grpc

# Third-party imports
from src.rpc.base_server import BaseServer
from protos.athena import athena_pb2
from protos.athena import athena_pb2_grpc


class GetBacktestService(athena_pb2_grpc.AthenaServicer):

    def GetBacktest(
        self,
        request: athena_pb2.GetBacktestRequest,
        context: grpc.ServicerContext,
    ) -> athena_pb2.GetBacktestResponse:
        """
            Executes a backtest based on the provided request.

            Parameters:
                - request (athena_pb2.GetBacktestRequest): The backtest request.
                - context (grpc.ServicerContext): The gRPC context.

            Returns:
                - (athena_pb2.GetBacktestResponse): The backtest response.
        """
        response = athena_pb2.GetBacktestResponse()
        return response


class AthenaServer(BaseServer):

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 50051,
        n_workers: int = 1,
    ) -> 'AthenaServer':
        """
            AthenaServer Constructor.

            Parameters:
                - host (str): Server hostname. Defaults to `localhost`.
                - port (int): Server port number. Defaults to `50051`.
                - n_workers (int): Number of threads. Defaults to `1`.
        """
        super().__init__(host, port, n_workers)

        # Register servicers
        athena_pb2_grpc.add_AthenaServicer_to_server(GetBacktestService(), self.server)
