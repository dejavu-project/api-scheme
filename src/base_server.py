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


class BaseServer(object):

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 50051,
        n_workers: int = 1,
    ) -> 'BaseServer':
        """
            BaseServer Constructor.

            Parameters:
                - host (str): Server hostname. Defaults to `localhost`.
                - port (int): Server port number. Defaults to `50051`.
                - n_workers (int): Number of threads. Defaults to `1`.
        """
        self.host = host
        self.port = port
        self.n_workers = n_workers
        self.target = f'{host}:{port}'

        self.thread_pool = futures.ThreadPoolExecutor(n_workers)
        self.server = grpc.server(self.thread_pool)
        self.server.add_insecure_port(self.target)


    def start(self) -> None:
        """
            Starts the server in blocking mode.
        """
        self.server.start()
        self.server.wait_for_termination()
