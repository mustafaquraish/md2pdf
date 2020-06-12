from flask import Flask, Response, request
app = Flask(__name__)

# @app.get('/api')
# def api():
#     md = request.query.get('md')
#     return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (md), mimetype="text/html")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    user = request.args.get('md')
    return Response("<h1>Flask</h1><p>You visited: /%s, %s</p>" % (path, user), mimetype="text/html")