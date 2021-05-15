import time


def strategy_two(self, payload):
    """
    # Replacement method 2
    :param self:
    :return:
    """
    self.name = "Strategy Two"
    time.sleep(payload['workload'])
    print("{} is used to execute method 2".format(self.name))