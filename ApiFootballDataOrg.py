import requests
import json

Headers = {
    'X-Auth-Token': '3c24f9a66baf42248b8637d06aa08cff'
    }

def getAreaId(Sigla):
    response = requests.get('http://api.football-data.org/v4/areas/', headers = Headers)
    dados = response.json()["areas"]
    Area = [obj for obj in dados if obj['countryCode'] == Sigla]
    AreaId = Area[0]['id']
    return AreaId


def getCompetitionsArea(Sigla, AreaId):
    payload = {'areas': AreaId}
    response = requests.get('http://api.football-data.org/v4/competitions/',params=payload, headers=Headers)
    dados = response.json()['competitions']
    Competition = [obj for obj in dados if obj['code'] == Sigla]
    CompetitionCode = Competition[0]['code']
    #print(json.dumps(dados, indent=4))
    return CompetitionCode


def getEquipIdByCompetitionCode(Code):
    payload = {}
    response = requests.get('http://api.football-data.org/v4/competitions/'+ Code +'/teams',params=payload ,headers=Headers)
    dados = response.json()['teams']
    Equips = [obj for obj in dados if ('Fortaleza' in obj['shortName']) or ('Corinthians' in obj['shortName'])]
    EquipsCode = Equips[0]['code']
    # print(json.dumps(Competition, indent=4))
    return dados

def getNextPlayer(id):
    payload = {'status':'SCHEDULED'}
    response = requests.get('https://api.football-data.org/v4/teams/'+ id +'/matches',params=payload ,headers=Headers)
    dados = response.json()
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
