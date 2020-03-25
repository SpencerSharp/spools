import os
class Terminal(object):
    def __init__(self, bash_profile):
        bash_profile.save()
        self.run_cmd('chmod +x ~/.spools/test/music/.bash')

    def run_cmd(self, cmd):
        os.system(cmd)
