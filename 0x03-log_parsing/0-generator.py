#!/usr/bin/python3
from random import randint, random, choice
from sys import stdout
from time import sleep
from datetime import datetime

for i in range(10000):
    sleep(random())
    stdout.write(
        '{:d}.{:d}.{:d}.{:d} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'
        .format(
            randint(1, 255),
            randint(1, 255),
            randint(1, 255),
            randint(1, 255),
            datetime.now(),
            choice([200, 301, 400, 401, 403, 404, 405, 500]),
            randint(1, 1024),
        )
    )
    stdout.flush()
