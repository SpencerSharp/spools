import os, signal, sys, time, logging, http.server, socketserver, json, datetime, webbrowser
import requests
import ipc, filesys

client_key = 'b4847d3dd2464848bc7f1f34b04f9509'
secret_key = '1ebd017edc044803906b36e81bd48cc3'
url        = 'http://localhost:8888/callback/'

username   = 'sharpieman20'
scopes     = [
'user-top-read',
'user-read-recently-played',
'user-read-playback-state',
'user-read-currently-playing',
'user-modify-playback-state',
'user-library-modify',
'user-library-read',
'streaming',
'app-remote-control',
'user-read-private',
'user-read-email',
'user-follow-modify',
'user-follow-read',
'playlist-modify-public',
'playlist-read-collaborative',
'playlist-read-private',
'playlist-modify-private']
scope = ' '.join(scopes)

def do_GET(request, client_address, self):
    data = request.recv(1024).strip()
    data_str = str(data)
    data_str = data_str[data_str.find('code=')+5:]
    user_code = data_str[:data_str.find('HTTP/1.1')-1]

    params = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': url,
    'client_id': client_key,
    'client_secret': secret_key
    }

    result = requests.post('https://accounts.spotify.com/api/token',data=params)
    res_dict = json.loads(result.text)
    print(res_dict)
    token = res_dict['access_token']
    refresh_token = res_dict['refresh_token']
    seconds_til_expiry = res_dict['expires_in']
    refresh_time = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(seconds=int(seconds_til_expiry)),'%Y%m%d %H:%M:%S')

    filesys.write('.token',token,overwrite=True)
    filesys.write('.refresh',refresh_token,overwrite=True)
    filesys.write('.refreshtime',refresh_time,overwrite=True)

    sys.exit()

def create_tcpserver(to_kill):
    import http.server
    import socketserver

    PORT = 8888
    Handler = do_GET

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        ipc.send_signal(to_kill, signal.SIGUSR1)
        req = httpd.handle_request()
        sys.exit()

def init_token():
    params = {
        'client_id': client_key,
        'response_type': 'code',
        'redirect_uri': url,
        'scope': scope,
        'show_dialog': False
    }
    to_access = requests.get('https://accounts.spotify.com/authorize',params=params)

    save_handler = signal.getsignal(signal.SIGUSR1)
    signal.signal(signal.SIGUSR1, signal.SIG_DFL)

    to_kill = os.fork()
    if to_kill == 0:
        signal.pause()
        sys.exit()
    tcpserver = os.fork()
    if tcpserver == 0:
        create_tcpserver(to_kill)
        sys.exit()
    try:
        os.waitpid(to_kill, 0)
    except:
        pass
    callback = webbrowser.open(to_access.url)
    try:
        os.waitpid(tcpserver,0)
    except:
        n = 1

    signal.signal(signal.SIGUSR1, save_handler)

# TODO: Replace spotipy's authentication process with your own
def get_token():
    if not filesys.does_exist('.token'):
        init_token()
    elif filesys.does_exist('.refreshtime'):
        cur_time = datetime.datetime.now()
        expiry_time_str = filesys.read('.refreshtime')
        expiry_time = datetime.datetime.strptime(expiry_time_str,'%Y%m%d %H:%M:%S')
        if cur_time > expiry_time:
            refresh_token = filesys.read('.refresh')
            params = {
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token,
                'client_id': client_key,
                'client_secret': secret_key
            }
            result = requests.post('https://accounts.spotify.com/api/token',data=params)
            res_dict = json.loads(result.text)

            token = res_dict['access_token']
            seconds_til_expiry = res_dict['expires_in']

            refresh_time = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(seconds=int(seconds_til_expiry)),'%Y%m%d %H:%M:%S')
            filesys.write('.refreshtime',refresh_time,overwrite=True)
            filesys.write('.token',token,overwrite=True)
            if 'refresh_token' in res_dict.keys():
                filesys.write('.refresh', res_dict['refresh_token'],overwrite=True)
    return filesys.read('.token')

def api_put(url):
    token = get_token()

    headers = {'Authorization': 'Bearer ' + token}

    requests.put(url, headers=headers)

def api_get(url, data=None):
    token = get_token()

    headers = {'Authorization': 'Bearer ' + token}

    if(data != None):
        result = requests.get(url, data=data, headers=headers)
    else:
        result = requests.get(url,headers=headers)
        
    try:
        return json.loads(result.text)
    except:
        return None

def api_post(url, data=None):
    token = get_token()

    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

    if(data != None):
        result = requests.get(url, json=data, headers=headers)
    else:
        result = requests.get(url, headers=headers)
    print(result.__dict__)

    try:
        return json.loads(result.text)
    except:
        return None

def get_track(id):
    url_to_query = 'https://api.spotify.com/v1/tracks/{}'
    url_to_query = url_to_query.format(id[:-1])
    result = api_get(url_to_query)
    
    return result

def get_track_named(name):
    url = 'https://api.spotify.com/v1/search'
    params = {
    'q': name,
    'type': 'track',
    'limit': 1
    }

    result = api_get('https://api.spotify.com/v1/search',params)

    if(result == None):
        return None

    val = result['tracks']['items']
    if len(val) == 0:
        return None
    return val[0]

def current_track():
    track = api_get('https://api.spotify.com/v1/me/player/currently-playing')
    if track == None:
        return track
    return track['item']

def get_user_id():
    url = 'https://api.spotify.com/v1/me'
    response = api_get(url)
    return response['id']

def make_playlist(name):
    base_url = 'https://api.spotify.com/v1/users/{}/playlists'
    user_id = get_user_id()
    print("userid is: " + user_id)
    url = base_url.format(user_id)
    params = {
        'name': name
    }
    result = api_post(url, params)
    print(result)
    if result != None:
        return result['id']
    return result

def pause_player():
    api_put('https://api.spotify.com/v1/me/player/pause')

def unpause_player():
    api_put('https://api.spotify.com/v1/me/player/play')