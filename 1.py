from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def base():
    param = {}
    param['title'] = 'MeToo'
    return render_template('base.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')