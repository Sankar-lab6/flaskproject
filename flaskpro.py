from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'
    return '<h2>Hello, India.!</h2>'
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5052)

