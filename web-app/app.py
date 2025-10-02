from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>DevOps Hunter у продакшені!</h1><p>Цей сайт розгорнуто автоматично.</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
