from types import MethodType


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function):
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)