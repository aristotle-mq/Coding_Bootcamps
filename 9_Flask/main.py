from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Главная страница сайта</h2>"

@app.route('/info')
def info():
    return "<h3>Это я написал</h3>"

if __name__ == '__main__':
    app.run()