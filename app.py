from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
app = Flask(__name__)

data = [
    {'role': 'user', 'username': 'Sai', 'content': 'Hello!', 'timestamp': '2023-10-01 10:00:00'},
    {'role': 'assistant', 'username': 'Assistant', 'content': 'Hi there!', 'timestamp': '2023-10-01 10:01:00'}
]

# def all_roleslist():
#     return list(set(msg['username'] for msg in data if msg['role'] in ['user', 'assistant']))

def role_of(username):
    for msg in data:
        if msg['username'] == username:
            return msg['role']
    return None

# def role_exists(username):
#     x = all_roleslist()  # Always update latest
#     return any(msg['username'] == username for msg in data if msg['role'] in x)

@app.route('/', methods=['GET', 'POST'])
def chat_listener():
    if request.method == 'POST':
        y = request.form.get('username')
        if role_of(y) != None:
            new_message = {
                'role': role_of(y),
                'username': y,
                'content': request.form.get('content'),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            data.append(new_message)
            # Redirect after successful POST to show updated chat
            return redirect(url_for('chat_listener', data=data))
        elif request.method == 'GET':
            return render_template('chatlist.html', data=data)
        else:
            return """<h1>Invalid username. Please try again.</h1> <br>
                    <button onclick="window.history.back()">Go Back</button>"""

    # For GET requests, always show the chat list
    print("Current chat data:", data)
    return render_template('chatlist.html', data=data)

if __name__ == '__main__':
    app.run(debug=False)
