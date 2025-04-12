from flask import Flask  
app = Flask(__name__)

@app.route('/SIU')
def index():
    return '<h1>Welcome to SIU</h1>'
@app.route('/SIU/user/<name>')
def user_name(name):
    return '<h1>hello,{}</h1>'.format(name)


  
def username(name):
     return '<h1>hello,{}</h1>'.format(name)

    

if __name__ == "__main__":
    app.run(debug=True)