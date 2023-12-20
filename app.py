from flask import Flask, render_template, redirect
import ApiFootballDataOrg

app = Flask(__name__)


@app.route('/')
def index():
    
    # NextPlayers  = model.modelNextPlayer('86')
    # return render_template('index.html', listPlayers = NextPlayers)
    ListMatches = ApiFootballDataOrg.getMatches()
    ListMatchesByTeam = ApiFootballDataOrg.getMatchesByTeamId('86')
    return render_template('index.html', listMatches = ListMatches.matches, listMatchesByTeam = ListMatchesByTeam.matches)


if __name__ == '__main__':
    app.run(debug=True)