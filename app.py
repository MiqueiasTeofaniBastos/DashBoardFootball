from flask import Flask, render_template, redirect
import model

app = Flask(__name__)


@app.route('/')
def index():
    
    NextPlayers  = model.modelNextPlayer('86')
    return render_template('index.html', listPlayers = NextPlayers)


if __name__ == '__main__':
    app.run(debug=True)