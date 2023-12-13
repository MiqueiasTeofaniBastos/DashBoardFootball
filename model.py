import ApiFootballDataOrg as ApiFoot
from datetime import datetime

def modelNextPlayer(id):
    response = ApiFoot.getNextPlayer(id)
    return populatePlayer(response) 

def populatePlayer(request):
    response = []
    for item in request:
        dateFormat = datetime.strptime(item['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
        date = dateFormat.strftime('%d %b %y ')
        hour = dateFormat.strftime('  %H:%M')
        response.append({
            "competition": item['area']['name'] + ' - ' + item['competition']['name'],
            "competitionEmblem": item['competition']['emblem'],
            "date": date,
            "hour": hour,
            "homeTeam": item['homeTeam'],
            "awayTeam": item['awayTeam'],
            "status": item['status']
        })
    return response