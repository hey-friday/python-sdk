import sys
import json
from friday.handlers.handler import Handler, Context


class Input(Handler):
    def __init__(self):
        super().__init__()
        argv = sys.argv
        for i in range(1, len(argv), 2):
            if argv[i] == "--input":
                data = json.loads(sys.argv[i + 1])
                self.command = Command(data["command"])
                self.context = Context(data["context"])
                self.available = True


class Command:
    def __init__(self, information):
        self.lang = information["lang"]
        self.content = information["content"]
        self.category = information["category"]
        self.ner_items = [NerItem(item) for item in information["ner_items"]]


class NerItem:
    def __init__(self, information):
        self.entity_group = information["entity_group"]
        self.score = information["score"]
        self.word = information["word"]
        self.start = information["start"]
        self.end = information["end"]
