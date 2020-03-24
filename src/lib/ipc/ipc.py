import os, signal, sys
import filesys
def send_signal(pid, sig):
    if pid > 0:
        try:
            os.kill(pid,sig)
        except:
            raise

def create_process(file, critical):
    to_kill = os.fork()
    if to_kill == 0:
        signal.pause()
        sys.exit()
    if os.fork() == 0:
        if os.fork() != 0:
            sys.exit()
        critical()
        send_signal(to_kill, signal.SIGUSR1)
        return True
    else:
        os.waitpid(to_kill, 0)
        return False

def get_process_info(process):
    details = filesys.read(process.get_desc_file(), overwrite=False, splitlines=True)
    return int(details[0]),details[1]

def check_if_process_exists(process):
    if not filesys.does_exist(process.get_desc_file()):
        return False
    pid,starttime = get_process_info(process)
    try:
        send_signal(pid,0)
        return True
    except:
        return False

def send_message_to(process, message, shouldAlert=True):
    pid = get_process_info(process)[0]
    filesys.write(process.get_input_file(), message, overwrite=False)
    if shouldAlert:
        send_signal(pid, process.signal)

def set_handler(params, method, sig):
    def wrapper(a,b):
        method()
    signal.signal(sig, wrapper)