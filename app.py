from flask import Flask, render_template
import game_of_life

app = Flask(__name__)

@app.route('/')
def index():
    game_of_life.GameOfLife(25, 25)
    return render_template("index.html")

@app.route('/live/')
def live():
    life = game_of_life.GameOfLife()
    if life.counter > 0:
        life.form_new_generation()
    else:
        life.counter += 1
    return render_template("live.html", life=life)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)