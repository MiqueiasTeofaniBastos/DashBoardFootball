import requests
import json

Url = 'http://api.football-data.org'
Version = '/v4/'
Headers = {
    'X-Auth-Token': '3c24f9a66baf42248b8637d06aa08cff'
    }

def getAreaId(Sigla):
    response = requests.get(Url+Version+'areas/', headers = Headers)
    dados = response.json()["areas"]
    Area = [obj for obj in dados if obj['countryCode'] == Sigla]
    AreaId = Area[0]['id']
    return AreaId


def getCompetitionsArea(Sigla, AreaId):
    payload = {'areas': AreaId}
    response = requests.get(Url+Version+'competitions/',params=payload, headers=Headers)
    dados = response.json()['competitions']
    Competition = [obj for obj in dados if obj['code'] == Sigla]
    CompetitionCode = Competition[0]['code']
    #print(json.dumps(dados, indent=4))
    return CompetitionCode


def getEquipIdByCompetitionCode(Code):
    payload = {}
    response = requests.get(Url+Version+'competitions/'+ Code +'/teams',params=payload ,headers=Headers)
    dados = response.json()['teams']
    Equips = [obj for obj in dados if ('Fortaleza' in obj['shortName']) or ('Corinthians' in obj['shortName'])]
    EquipsCode = Equips[0]['code']
    # print(json.dumps(Competition, indent=4))
    return dados

def getNextPlayer(id):
    payload = {} #{'status':['SCHEDULED', 'IN_PLAY']}
    response = requests.post(Url+Version+'teams/'+ id +'/matches',json=payload ,headers=Headers)
    dados = response.json()['matches']
    dados = list(filter(lambda x: x['status'] == 'SCHEDULED' or x['status'] == 'IN_PLAY' or x['status'] == 'PAUSED', dados))
    # Equips = [obj for obj in dados if ('Fortaleza' in obj['shortName']) or ('Corinthians' in obj['shortName'])]
    # EquipsCode = Equips[0]['code']
    # print(json.dumps(dados, indent=4))
    return dados 


# areaId = getAreaId('BRA')
# competitionCode = getCompetitionsArea('BSA', areaId)
# getEquipByCompetitionCode(competitionCode)
# getNextPlayer('1779')


#1779 SC Corinthians Paulista
#1779 Fortaleza EC
#print(json.dumps(dados, indent=4))
