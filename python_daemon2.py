#!/usr/bin/env python3

import sys
import time
import datetime
from pathlib import Path
from daemon import Daemon  # Ensure this is a Python 3-compatible daemon library

class MyDaemon(Daemon):
    def run(self):
        Path("/var/log/python_daemon").mkdir(parents=True, exist_ok=True)
        while True:
            with open("/var/log/python_daemon/timestamp.log", "a") as fh:
               fh.write(str(datetime.datetime.now()) + "\n")
            time.sleep(1)

if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print(f"usage: {sys.argv[0]} start|stop|restart")
        sys.exit(2)
