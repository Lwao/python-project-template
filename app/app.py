#!/usr/bin/python

import logging
import module1 as mod1
import module2.submodule2 as mod2

logger = logging.getLogger(__name__)

logging.basicConfig( level=logging.INFO,
                     format="%(asctime)s.%(msecs)03d [%(levelname)s] (%(process)d) %(filename)s.%(funcName)s.%(lineno)s: %(message)s",
                     datefmt="%d-%m-%y %H:%M:%S"
)

def start():
    mod1.hello_world()
    mod2.hello_world()

if __name__ == "__main__":
    start()