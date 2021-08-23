import friday
from friday.skill.response import Response


class FridaySkill:
    def __init__(self):
        # handle inputs
        self.input = friday.handlers.Input()
        self.config_input = friday.handlers.Config()
        self.response = Response()

        # process inputs
        if self.config_input.available:
            self.config()
        elif self.input.available:
            self.process()

        # return answer
        print(self.response)

    # method for handling a setup
    def config(self):
        raise NotImplementedError

    # method for handling a regular command
    def process(self):
        raise NotImplementedError
