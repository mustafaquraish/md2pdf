from flask import Flask, Response
app = Flask(__name__)

@app.get('/api')
def api():
    md = request.query.get('md')
    return Response("<h1>Flask</h1><p>You entered: /%s</p>" % (md), mimetype="text/html")