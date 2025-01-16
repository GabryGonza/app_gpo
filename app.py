from flask import Flask, render_template, request, redirect, url_for
from collections import defaultdict

app = Flask(__name__)

# Utilizziamo un dizionario per simulare il database del magazzino
magazzino = defaultdict(int)

@app.route('/')
def index():
    return render_template('index.html', magazzino=magazzino)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    prodotto = request.form['prodotto']
    quantita = int(request.form['quantita'])
    magazzino[prodotto] += quantita
    return redirect(url_for('index'))

@app.route('/aggiorna', methods=['POST'])
def aggiorna():
    prodotto = request.form['prodotto']
    quantita = int(request.form['quantita'])
    if prodotto in magazzino:
        magazzino[prodotto] = quantita
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
