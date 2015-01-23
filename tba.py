__author__ = 'Atle'
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "HEI HEI WHOOOO"

@app.route('/game/create')
def createGame():
    return "GameCreated"

@app.route('/game/join')
def joinGame():
    room = request.args.get('room')
    nick = request.args.get('nick')
    role = request.args.get('role')
    return ' - '.join([room, nick, role])

@app.route('/host')
def host():
    return render_template('/host/host.html')

@app.route('/join')
def join():
    return render_template("/client/client.html")

if __name__ == '__main__':
    app.run()