from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_data():
    user_info = {
        'name': 'Иван',
        'age': 25,
        'city': 'Москва'
    }

    return render_template('data.html', user=user_info)


app.run()
