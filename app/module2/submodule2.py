import logging

import module2.submodule2 as mod2

logger = logging.getLogger(__name__)

def hello_world():
    print("submodule2: Hello World!")

if __name__ == "__main__":
    pass