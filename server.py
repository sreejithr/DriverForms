from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('message', namespace='/sign')
def handle_message(message):
    print message

@app.route('/upload/', methods=['POST'])
def upload_signature():
    image = request.form['signature']
    socketio.emit('message', {"image": image}, namespace='/sign')

if __name__ == '__main__':
    socketio.run(app)
