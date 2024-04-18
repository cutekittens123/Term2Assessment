from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

n = 0
symbol = []
turn = 1
board = [" "]*9

def winner(x):
    pass




@app.route('/', methods=['GET', 'POST'])
def index():
    global n
    if request.method == 'POST':
        n = int(request.form["players"])
        return redirect(url_for("symbols"))
    return render_template("index.html")

@app.route('/symbols', methods=['GET', 'POST'])
def symbols():
    global symbol
    if request.method == 'POST':
        symbol = [request.form[f"player_{i}_symbol"] for i in range(1,1+n)]
        if len(set(symbol)) < n:
            return render_template("duplicate.html", players=n)
        else:
            return redirect(url_for("game"))
    return render_template('symbols.html', players=n)

@app.route("/game", methods=["GET","POST"])
def game():
    global turn
    global board
    global symbol
    if request.method == "POST":
        board[int(request.form.get("rows"))] = symbol[turn-1]
        turn += 1
        if turn > n:
            turn = 1
    return render_template("game.html",board=board)

@app.route("/win", methods=["GET","POST"])
def win():
    pass
    
app.run()
