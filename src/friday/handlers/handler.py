class Handler:
    def __init__(self):
        self.available = False


class Context:
    def __init__(self, information):
        self.interaction = Interaction(information["interaction"])
        self.device = Device(information["device"])
        self.room = Room(information["room"])
        self.payload = information["payload"]


class Interaction:
    def __init__(self, information):
        self.type = information["type"]


class Device:
    def __init__(self, information):
        self.id = information["id"]
        self.name = information["name"]


class Room:
    def __init__(self, information):
        self.id = information["id"]
        self.name = information["name"]
        self.floor = Floor(information["floor"])


class Floor:
    def __init__(self, information):
        self.id = information["id"]
        self.name = information["name"]
