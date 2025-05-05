from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def main(name=None):
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'name' : name, 
        'title' : 'Hello!',
        'now' : now_str
    }
    return render_template('hello.html', **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
