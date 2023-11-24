from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def get_form_data():
    name = request.form.get('name')
    password = request.form.get('password')
    return f'<h1>Name: {name}, Password: {password}</h1>'


if __name__ == '__main__':
    app.run()
