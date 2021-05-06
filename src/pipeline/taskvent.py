"""
Task ventilator
push tasks to workers
"""

import logging
import json
from pynng import Push0
import random
import time


def main():
    addr = "tcp://127.0.0.1:5557"
    with Push0(dial=addr) as push:
        time.sleep(0.01)
        logging.info("send messages on 5557")
        logging.info("Sending tasks to workers")
        for task_nbr in range(10):
            workload = random.randint(1, 5)
            message_dict = {
                "task_nbr": task_nbr,
                "strategy": "strategy_one",
                "workload": workload
            }
            message_str = json.dumps(message_dict)
            message_bytes = message_str.encode("utf-8")
            push.send(message_bytes)
            print(f"message_dict={message_dict}")
        for task_nbr in range(10):
            workload = random.randint(1, 5)
            message_dict = {
                "task_nbr": task_nbr,
                "strategy": "strategy_two",
                "workload": workload
            }
            message_str = json.dumps(message_dict)
            message_bytes = message_str.encode("utf-8")
            push.send(message_bytes)
            print(f"message_dict={message_dict}")

        for task_nbr in range(10):
            workload = random.randint(1, 5)
            message_dict = {
                "task_nbr": task_nbr,
                "strategy": "strategy_three",
                "workload": workload
            }
            message_str = json.dumps(message_dict)
            message_bytes = message_str.encode("utf-8")
            push.send(message_bytes)
            print(f"message_dict={message_dict}")


if __name__ == "__main__":
    main()
