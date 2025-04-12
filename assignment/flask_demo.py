from flask import Flask  
app = Flask(__name__)

@app.route("/hello")
def index():
    return '<h1>hello world</h1>'


   
def username(name):
    return '<h1>f"username : {name}"</h1>'

    app.add_url("/hello/<name>",username)

if __name__ == "__main__":
    app.run(debug=True)