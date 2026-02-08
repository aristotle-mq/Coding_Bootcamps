from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', title='Главная страница 2.0') # каталог templates имеет уникальное имя, не подлежит изменению

@app.route('/stud')
def students():
    list_students = ['Первый студент', "Второй студент", "Третий студент", "Четвертый студент", "Пятый студент", "Шестой студент"]
    return render_template('students.html', title='Список студентов',
                           data=list_students)

@app.route('/info')
def info():
    return "<h3>Это я написал</h3>"

@app.route('/calc/<int:x>/<int:y>')
def calc(x, y):
    return f'{x} + {y} = {x + y}'

@app.route('/hi/<name>')
def hi(name):
    return f'Hello, {name}'

if __name__ == '__main__':
    app.run()