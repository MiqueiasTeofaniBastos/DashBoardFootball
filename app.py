from flask import Flask, render_template, redirect
import ApiFootballDataOrg as ApiFoot
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    
    response = []
    for item in ApiFoot.getNextPlayer('86')['matches']:
        dateFormat = datetime.strptime(item['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
        date = dateFormat.strftime('%d %b %y ')
        hour = dateFormat.strftime('  %H:%M')
        response.append({
            "competition": item['area']['name'] + ' - ' + item['competition']['name'],
            "competitionEmblem": item['competition']['emblem'],
            "date": date,
            "hour": hour,
            "homeTeam": item['homeTeam'],
            "awayTeam": item['awayTeam']
        })
        
    return render_template('index.html', dataList = response)


if __name__ == '__main__':
    app.run(debug=True)