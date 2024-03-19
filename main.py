# Copyright (C) 2023-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

# Third-party imports
from src.athena.server import AthenaServer


if __name__ == '__main__':

    server = AthenaServer(
        host = 'localhost',
        port = 50051,
        n_workers = 1
    )
    server.start()
