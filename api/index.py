from flask import Flask, Response
app = Flask(__name__)


@app.route('/')
def catch_all():
    return Response("HELLOOOOOOOO")

@app.route('/pls')
def catch_all():
    return Response("HELLOOOOOOOO")
