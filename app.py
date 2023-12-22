from flask import Flask, render_template, redirect
import ApiFootballDataOrg

app = Flask(__name__)


@app.route('/')
def index():
    
    ListMatches = ApiFootballDataOrg.getMatches().matches
    ListMatchesByTeam = ApiFootballDataOrg.getMatchesByTeamId('86').matches
    return render_template('index.html', listMatches = ListMatches)


if __name__ == '__main__':
    app.run(debug=True)