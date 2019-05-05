# coding:utf-8
<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask
>>>>>>> add986d637e26d86e75d5fbc81792b9eb15653a4

app = Flask(__name__)

@app.route('/')
<<<<<<< HEAD
def index():
    return 'hello world'#render_template('index.html')
=======
def hello():
    return '<h1>留言板</h1>'
>>>>>>> add986d637e26d86e75d5fbc81792b9eb15653a4

if __name__ == '__main__':
    app.run(debug=True)

<<<<<<< HEAD
=======
    
>>>>>>> add986d637e26d86e75d5fbc81792b9eb15653a4
