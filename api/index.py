from flask import Flask, Response
app = Flask(__name__)

# @app.get('/api')
# def api():
#     md = request.query.get('md')
#     return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (md), mimetype="text/html")

# @app.route('/api/', defaults={'path': ''})
# @app.route('/api/<path:path>')
# def catch_all(path):
    
# index.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'