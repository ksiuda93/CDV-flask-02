from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
users = []

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/user/<int:user_id>')
def user_page(user_id):
    comments = ["Super", "Dzialaj dalej"]
    return render_template('user.html', user_id=user_id, comments=comments)

@app.route('/api', methods=["POST", "GET"])
def hello_api():
    return jsonify(
        {
            "Path": "/api"
        }
    )

@app.get('/api/user/<int:user_id>')
def get_user(user_id):
    return jsonify(
        {
            "user_id": user_id
        }
    )

@app.post('/api/user')
def add_user():
    data = request.json
    print(request.host)
    users.append(request.json)
    print(users)
    return jsonify(
        {
            "Path": "/api/user"
        }
    )

#int, float, any, uuid
@app.delete('/api/user/<int:user_id>')
def delete_user(user_id):
    return jsonify(
        {
            "user_id": user_id
        }
    )

if __name__ == "__main__":
    app.run()
