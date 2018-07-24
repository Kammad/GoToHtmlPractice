import flask
import random


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return\
        """<html> <body> Оно вроде работает... Секунду. Такс... Вот! Нашёл. Напишите после всего в адресной строке
        "/me" и тогда я смогу рассказать о себе! А, точно! Я умею предсказывать погоду.  Мои дарования пророка дают о
        себе знать. Напишите "/weather".
        <center><b><u><a href="http://172.7.0.58:8080/me" title="ME! CLICK ON ME!"></u></b></center></body>
        </html> """
@app.route('/me')
def meme():
    return render_template('page.html')


@app.route('/weather')
def weathers():
    import random
    weather = ["Завтра будет дождь, атвичаю!",
               "Завтра будет снег, атвичаю!",
               "Завтра будет солнечно, атвичаю!",
               "Завтра будет песчаная буря, атвичаю!",
               "Завтра будет ураган, атвичаю!",
               "Завтра будет... А ничего завтра не будет! Всё, мы умрём."]
    wea = random.choice(weather)
    return wea


app.run(debug=True, port=8080, host=0.0.0.0)
