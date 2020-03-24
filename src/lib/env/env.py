import re
import filesys
class SpoolsBashProfile(object):
    default_cmds = '''self.add_cmd('export SPOOLS_HOME=$HOME/.spools/test')
self.add_cmd('shopt -s extdebug')
self.add_cmd('export SPOOLS_RUNNER_DAEMON=$(head -n 1 ~/.spools/test/music/.daemons/.CLIRunnerDaemon)')
self.add_debug_trap('val=$BASH_COMMAND && REGEX="^[0-9]{1,2}\.[0-9].*" && if [[ $val =~ $REGEX ]]; then echo $val >> ~/.spools/test/music/.daemons/CLIRunnerDaemon && kill -30 $SPOOLS_RUNNER_DAEMON && false; else true; fi')
    '''

    cmd_map = {
    'alert'     : 'if [ $pid -ge 1 ]; then kill -30 $pid 2> /dev/null; fi',
    'runner_pid': '$(head -n 1 $SPOOLS_HOME/music/.CLIRunnerDaemon)',
    'out'       : '~/.terminal',
    'write'     : 'echo',
    'lastcmd'   : '$BASH_COMMAND'
    }

    def __init__(self):
        self.cmds = []

    def add_trap(self,cmd, signal):
        self.add_cmd("trap '{cmd}' {signal}".format(cmd=cmd, signal=signal))

    def add_debug_trap(self,cmd):
        self.add_trap(cmd, 'DEBUG')

    def save(self):
        exec(SpoolsBashProfile.default_cmds)
        self.cmds.insert(0,'#!/usr/bin/env bash')
        filesys.write('.bash','\n'.join(self.cmds),overwrite=True)

    def add_cmd(self,cmd,canadd=True):
        if '&&' in cmd:
            anded = []
            for sub_cmd in cmd.split('&&'):
                anded.append(self.add_cmd(sub_cmd,False))
            result = '&&'.join(anded)
            self.cmds.append(result)
            return result
        did_replace = False
        for possible in self.cmd_map.keys():
            if possible in cmd:
                did_replace = True
                if '{}' in cmd:
                    x = re.sub(possible + ' ', '', cmd)
                    cmd = re.sub(possible,self.cmd_map[possible].format(x), cmd)
                else:
                    cmd = re.sub(possible, self.cmd_map[possible], cmd)
        if canadd:
            if did_replace:
                self.add_cmd(cmd)
            else:
                self.cmds.append(cmd)
        return cmd