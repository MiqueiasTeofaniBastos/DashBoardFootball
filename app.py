from flask import Flask, render_template, redirect
import requests
import json
import model

app = Flask(__name__)

@app.route('/')
def index():
    
    response = requests.get("https://dashboardfootballapi.onrender.com/api/getMatches").content
    data = json.loads(response)
    soccer_data = model.SoccerData(**data).matches
    # soccer_data.matches = list(filter(lambda x: x.status == 'LIVE' or x.status == 'IN_PLAY' or x.status == 'PAUSED' or x.status == 'TIMED', soccer_data.matches)) 
    
    response2 = requests.get("https://dashboardfootballapi.onrender.com/api/getNewsSport").content
    data2 = json.loads(response2)
    news_data = model.NewsData(**data2).articles
    news_data = list(filter(lambda x: x.urlToImage != None and x.author != None, news_data))[:4]

    return render_template('index.html', listMatches = soccer_data, listNews = news_data)




# if __name__ == '__main__':
#     app.run(debug=True)