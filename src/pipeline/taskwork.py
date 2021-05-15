"""
Task worker
Collect workload from ventilator
Sends results to sink
"""

import json
import logging
import time
import traceback

from pynng import Push0, Pull0

from pipeline import vent_addr, sink_addr
from pipeline.strategies import Strategy
from pipeline.strategies.strategy_one import strategy_one
from pipeline.strategies.strategy_three import strategy_three
from pipeline.strategies.strategy_two import strategy_two


def select_strategy(strategy_str: str):
    curr_strategy = strategy_one
    if strategy_str == "strategy_one":
        curr_strategy = strategy_one
    elif strategy_str == "strategy_two":
        curr_strategy = strategy_two
    elif strategy_str == "strategy_three":
        curr_strategy = strategy_three
    return curr_strategy


def main():
    with Pull0() as vent:
        vent.listen(vent_addr)
        time.sleep(0.01)
        logging.info("receive messages from vent")
        while True:
            print("waiting for message")
            message = vent.recv()
            message_str = message.decode("utf-8")
            message_dict = json.loads(message_str)
            print(f"start message_dict={message_dict}")
            time.sleep(message_dict['workload'])
            strategy_str = message_dict.get('strategy', "strategy_one")

            curr_strategy = select_strategy(strategy_str)

            try:
                curr_strategy = Strategy(curr_strategy)
                curr_strategy.execute(message_dict)
                message_dict['result'] = 'done'
                print(f"done message_dict={message_dict}")

            except:
                exceptiondata = traceback.format_exc().splitlines()
                exceptionarray = [exceptiondata[-1]] + exceptiondata[1:-1]
                message_dict['result'] = exceptionarray
                print("failed")

            with Push0(dial=sink_addr) as sink:
                time.sleep(0.01)
                message_str = json.dumps(message_dict)
                message_bytes = message_str.encode("utf-8")
                sink.send(message_bytes)
                logging.info("send messages to sink")


if __name__ == "__main__":
    main()
