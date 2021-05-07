"""
Task sink
Collects results from workers
"""
import json
import logging
from pynng import Push0, Pull0, Timeout
import time


def main():
    addr = "tcp://127.0.0.1:5558"
    with Pull0() as work:
        work.listen(addr)
        time.sleep(0.01)
        logging.info("receive messages on 5558")
        while True:
            time.sleep(0.01)
            print("waiting for next message")
            message = work.recv(block=True)
            print(f"message={message}")
            content = message.decode("utf-8")
            print(f"content={content}")
            content_dict = json.loads(content)
            print(f"message_dict={content_dict}")


if __name__ == "__main__":
    main()
