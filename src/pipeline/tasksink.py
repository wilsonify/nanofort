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
    with Pull0(dial=addr) as pull0:
        time.sleep(0.01)
        logging.info("receive messages on 5558")
        while True:
            print("waiting for next message")
            message = pull0.recv()
            print(f"message={message}")
            content = message.bytes.decode("utf-8")
            print(f"content={content}")
            content_dict = json.load(content)
            print(f"message_dict={message_dict}")


if __name__ == "__main__":
    main()
