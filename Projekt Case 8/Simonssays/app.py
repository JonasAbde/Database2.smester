from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import game  # Importerer Pygame-spillet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Start Pygame i en separat tråd
def start_game():
    game.run_game(socketio)

threading.Thread(target=start_game).start()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print("Klient forbundet.")

if __name__ == '__main__':
    socketio.run(app)
