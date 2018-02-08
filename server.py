import urllib.request
import json
import os
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['GET'])
def webhook():
    url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=5cab5d5971064472bb501bd1d73a7a2d'
    response = requests.get(url)
    r = response.json()
    k = json.dumps(r, indent=4)
    res = json.loads(k)
    print()
    i=0
    x="NEWS\n"
    y=""
    while i<5:
        x+=(res['articles'][i]['title'])+"\n"
        x+=(res['articles'][i]['description'])+"\n\n"
        i=i+1
    return x


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False)