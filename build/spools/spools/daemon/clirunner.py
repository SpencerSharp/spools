import main
from runner import RunnerDaemon

class CLIRunnerDaemon(RunnerDaemon):
    def __init__(self):
        super().__init__(main.run_message)
