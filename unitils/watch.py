import unitils
import time

def watch(command, interval=2):
    while True:
        yield unitils.system_call(command)
        time.sleep(interval)
