import time


def strategy_three(self, payload):
    """
    # Replacement method 3
    :param self:
    :return:
    """
    self.name = "Strategy Three"
    time.sleep(payload['workloadasdf'])
    print("{} is used to execute method 2".format(self.name))