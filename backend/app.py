from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

passwords = {
    "saihsu" : "Pokemon10", 
    "aki" : "password",
    "parker" : "password",
    "henry" : "password",

}
@app.route("/")
def hello_world():
    page = """
    <form action="/chat" method="get">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    <label for="password">Password:</label><br>
    <input type="text" id="password" name="password"><br>
    <input type ="submit" value="Submit">
    </form> 
    """
    return page
    
# In-memory message history
message_history = []

@app.route('/chat')
def index():
    return render_template('chat.html')

@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')
    emit('chat_history', message_history, to=request.sid)

@socketio.on('message')
def handle_message(msg):
    print(f'Message: {msg}')
    message_history.append(msg)
    send(msg, broadcast=True)

@socketio.on('clear_messages')
def handle_clear_messages():
    print("Clearing message history")
    message_history.clear()
    emit('chat_cleared', broadcast=True)

if __name__ == '__main__':
    print("Starting chat server on http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000)
