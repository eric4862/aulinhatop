from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"

@app.route('/compras')
def compras():
    return render_template("compras.html")

if __name__ == '__main__':
    app.ron()