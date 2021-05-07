"""
Task worker
Collect workload from ventilator
Sends results to sink
"""

import logging
import time
import traceback
from types import MethodType
from pynng import Push0, Pull0
import json


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function):
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)


def strategy_one(self, payload):
    """
    # Replacement method 1
    :param self:
    :return:
    """

    self.name = "Strategy One"
    time.sleep(payload['workload'])
    print("{} is used to execute method 1".format(self.name))


def strategy_two(self, payload):
    """
    # Replacement method 2
    :param self:
    :return:
    """
    self.name = "Strategy Two"
    time.sleep(payload['workload'])
    print("{} is used to execute method 2".format(self.name))


def strategy_three(self, payload):
    """
    # Replacement method 3
    :param self:
    :return:
    """
    self.name = "Strategy Three"
    time.sleep(payload['workloadasdf'])
    print("{} is used to execute method 2".format(self.name))


def main():
    vent_addr = "tcp://127.0.0.1:5557"
    sink_addr = "tcp://127.0.0.1:5558"
    with Pull0() as vent:
        vent.listen(vent_addr)
        time.sleep(0.01)
        logging.info("receive messages on 5557")
        while True:
            print("waiting for message")
            message = vent.recv()
            message_str = message.decode("utf-8")
            message_dict = json.loads(message_str)
            print(f"start message_dict={message_dict}")
            time.sleep(message_dict['workload'])
            strategy_str = message_dict.get('strategy', "strategy_one")
            curr_strategy = Strategy(eval(strategy_str))
            try:
                curr_strategy.execute(message_dict)
                message_dict['result'] = 'done'
                print(f"done message_dict={message_dict}")
            except:
                exceptiondata = traceback.format_exc().splitlines()
                exceptionarray = [exceptiondata[-1]] + exceptiondata[1:-1]
                message_dict['result'] = exceptionarray
                print("failed")
            with Push0() as sink:
                sink.listen(sink_addr)
                time.sleep(0.01)
                message_str = json.dumps(message_dict)
                message_bytes = message_str.encode("utf-8")
                sink.send(message_bytes)
                logging.info("send messages to 5558")


if __name__ == "__main__":
    main()
