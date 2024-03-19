##########################################################
#
# Copyright (C) 2023-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

import grpc


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

        self.channel = None


    def is_server_ready(self, timeout: int = 1) -> bool:
        """
            Returns whether server is connected and ready.

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
