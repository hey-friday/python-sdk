import sys
import json
from friday.handlers.handler import Handler, Context


class Config(Handler):
    def __init__(self):
        super().__init__()
        argv = sys.argv
        for i in range(1, len(argv), 2):
            if argv[i] == "--inputConfig":
                data = json.loads(sys.argv[i + 1])
                self.context = Context(data["context"])
                self.configuration = Configuration(data["configuration"])
                self.available = True


class Configuration:
    def __init__(self, information):
        self.state = information["state"]
        self.data = information["data"]
