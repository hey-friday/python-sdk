import json
import time


class Response:
    def __init__(self):
        self._text = ""
        self.audio = None
        self.force_relaunch = False
        self.payload = None
        self.configuration = Configuration()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        if self.audio is None:
            self.audio = value

    def __str__(self):
        return json.dumps({
            "meta": {
                "timestamp": time.time()
            },
            "response": {
                "text": self.text,
                "audio": self.audio,
                "payload": self.payload
            },
            "configuration": {
                "state": self.configuration.state,
                "data": self.configuration.data,
            }
        })


class Configuration:
    def __init__(self):
        self.state = None
        self.data = None
