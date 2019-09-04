import os

from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    res = main.run_board("clayboards/IMG_1353.jpg", "board2.jpg")
    return f'Hello {target}!\nres: {res}\n'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    # app.run(debug=True,host='127.0.0.1',port=int(os.environ.get('PORT', 8081)))
