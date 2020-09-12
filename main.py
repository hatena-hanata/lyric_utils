from flask import Flask, render_template, Markup, request, jsonify, json
import os
from src.modules.module import scraping

template_dir = os.path.abspath('src/templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def hello():
    return render_template('top.html')

@app.route('/convert')
def note():
    return render_template('convert.html')

@app.route('/result', methods=['POST'])
def result():
    url = request.form['url']
    kashi = scraping(url)
    return jsonify({'output': kashi})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
