from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route("/<int:first_num>/<int:second_num>")
def sum(first_num,second_num):
    return f"{first_num+second_num}"


if __name__ == '__main__':
    app.run()
