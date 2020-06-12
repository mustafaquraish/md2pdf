from flask import Flask, Response
app = Flask(__name__)


@app.route('/api/', defaults={'path': ''})
@app.route('/api/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
