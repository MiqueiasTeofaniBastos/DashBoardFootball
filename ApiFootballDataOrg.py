import requests
import json
import model

Url = 'http://api.football-data.org'
Version = '/v4/'
Headers = {
    'X-Auth-Token': '3c24f9a66baf42248b8637d06aa08cff'
    }

def getMatches():
    payload = {}
    response = requests.get(Url+Version+'matches/',params=payload ,headers=Headers)
    data = response.json()
    soccer_data = model.SoccerData(**data)
    soccer_data.matches = list(filter(lambda x: x.status == 'LIVE' or x.status == 'IN_PLAY' or x.status == 'PAUSED' or x.status == 'TIMED', soccer_data.matches))    
    return soccer_data


def getMatchesByTeamId(id):
    payload = {} #{'status':['SCHEDULED', 'IN_PLAY']}
    response = requests.post(Url+Version+'teams/'+ id +'/matches',json=payload ,headers=Headers)
    data = response.json()
    soccer_data = model.SoccerData(**data)
    return soccer_data 


