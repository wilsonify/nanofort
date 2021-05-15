import time


def strategy_one(self, payload):
    """
    # Replacement method 1
    :param self:
    :return:
    """

    self.name = "Strategy One"
    time.sleep(payload['workload'])
    print("{} is used to execute method 1".format(self.name))
