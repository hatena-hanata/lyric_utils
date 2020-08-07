from flask import Flask, render_template, Markup, request, jsonify, json
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

@app.route('/')
def hello():
    # name = "Hello World"
    # return name
    return render_template('top.html')

@app.route('/result', methods=['POST'])
def scraping():
    url = request.form['url']
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    kashi_area_str = str(soup.find('div', id='kashi_area'))
    kashi = kashi_area_str.replace('<div id="kashi_area" itemprop="text">', '')
    kashi = kashi.replace('</div>', '')
    return jsonify({'output': Markup(kashi)})
    # return render_template('res.html', kashi=Markup(kashi))
    # kashi = kashi_area.text
    # print(kashi)
    # kashi = kashi.replace('　', '\n')
    # return render_template('res.html', kashi=Markup(kashi.replace('\n', '<br>')))

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
