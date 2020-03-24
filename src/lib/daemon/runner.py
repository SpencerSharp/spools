import signal
from daemon import Daemon
import data
class RunnerDaemon(Daemon):
    def __init__(self, run_message):
        self.run_message = run_message
        super().__init__(signal.SIGUSR1, self.run)

    def run(self, messages):
        data.load_tables()
        for message in messages:
            self.run_message(message)
        self.sleep()