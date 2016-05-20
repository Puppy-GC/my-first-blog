import requests

url='http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
status_url='http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
ban_url ='http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/'
twitch_url= 'https://api.twitch.tv/kraken/streams/'
params ={
    'key' :'BAD358880600F14DEF9CDFE81B148849',
    'steamid': '76561198039024195',
    'format': 'json'
}

params_stats = {
    'key': 'BAD358880600F14DEF9CDFE81B148849',
    'steamids': '76561198039024195'

}

params_ban ={
    'key': 'BAD358880600F14DEF9CDFE81B148849',
    'steamids': '76561198013737709'

}
channel_name = 'etozhemad'
res=requests.get(url, params=params)
res_stats=requests.get(status_url, params=params_stats)
res_vac = requests.get(ban_url, params=params_ban)
res_twitch = requests.get(twitch_url + channel_name)
data = res.json()
data_stats = res_stats.json()
data_vac = res_vac.json()
data_twitch = res_twitch.json()
print(data['response']['games'])
print(data_stats['response']['players'][0].get('profileurl'))
print(data_vac)
print(data_twitch)