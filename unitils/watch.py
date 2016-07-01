import unitils
import time

def watch(command, interval=2):
    """Iterator yielding a tuple of (stdout, stderr, returncode)
    returned by issuing command to the system repeatedly. By default
    sleeps for 2 seconds between issuing commands.

    :param command: The command to issue to the system
    :param interval: The number of seconds to wait before issuing command again
    :type command: str, list
    :type interval: int
    :returns: Iterator of three-tuples containing (stdout, stderr, returncode)
    """
    while True:
        yield unitils.system_call(command)
        time.sleep(interval)
