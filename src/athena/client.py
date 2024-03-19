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
from base_clienty import BaseClient
from protos.athena import athena_pb2_grpc


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
        
        self.channel = grpc.insecure_channel(self.target)
        self.stub = athena_pb2_grpc.AthenaStub(self.channel)
