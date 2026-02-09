from pyexpat.errors import messages

from flask import Flask, render_template
from werkzeug.utils import redirect

from register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello hello hello hello'


def check_password(password):
    if len(password) < 8:
        return 'Длина меньше 8 символов'
    elif password.lower() == password or password.upper() == password:
        return 'Все буквы в одном регистре'
    elif sum([int(i) in password for i in range(9)]) == 0:
        return 'Пароль не может состоять без цифр'
    return True


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        result = check_password(form.data['password'])
        if result != True :
            render_template('reg.html', form=form, message=result)
        redirect('/')
    return render_template('reg.html', form=form)

@app.route('/') # GET
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