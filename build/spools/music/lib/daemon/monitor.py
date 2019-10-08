# import time, os, sys, signal, subprocess
# from ipc.terminal import send_signal, wake_on_signal_received
# from lib.spotify  import current, get, get_spotify_permissions
# from filesys.file   import get_path, music_home
# from lib.data     import load_from_local, save_to_local
# from ipc.terminal import prompt_and_get_rating

# def monitor():
#     prev_track = None
#     prev_album = None
#     signal.signal(signal.SIGUSR1, signal.SIG_IGN)
#     while True:
#         cur_track = current()
#         cur_album = None
#         if cur_track != None:
#             if prev_track != None:
#                 if cur_track.id != prev_track.id:
#                     prompt_and_get_rating(prev_track)
#                     prev_track = cur_track
#             else:
#                 prev_track = cur_track
#         if False and cur_album != None:
#             cur_album = get('album', cur_track.album_id)
#             if prev_album != None:
#                 if cur_album.id != prev_album.id:
#                     prompt_and_get_rating(prev_album)
#                     prev_album = cur_album
#             else:
#                 prev_album = cur_album
#         time.sleep(0.1)

# def create_monitor():
#     top_fork = os.fork()
#     if top_fork == 0:
#         signal.pause()
#         sys.exit()
#     signal.signal(signal.SIGUSR1, wake_on_signal_received)
#     blocked = open(music_home + 'monitor_block', 'w')
#     if os.fork() == 0:
#         blocked.close()
#         blocked = open(music_home + 'monitor_block', 'w')
#         if os.fork() > 0:
#             sys.exit()
        
#         set_monitor_pid(os.getpid())
#         send_signal(top_fork,signal.SIGUSR1)
#         monitor()
#     return top_fork, blocked
    

# def get_monitor_path():
#     return get_path('monitor')

# def set_monitor_pid(pid):
#     path = get_monitor_path()
#     file = open(path, 'w')
#     file.write(str(pid))
#     file.close()

# def get_monitor_pid():
#     path = get_monitor_path()
#     if not os.path.exists(path):
#         return -1
#     file = open(path, 'r')
#     result = file.read()
#     file.close()
#     return int(result)

# def does_monitor_exist():
#     pid = get_monitor_pid()
#     if pid == -1:
#         return False
#     try:
#         os.kill(pid, 0)
#     except:
#         return False
#     return True