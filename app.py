from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/amor')
def amor():
    return render_template('amor.html')

@app.route('/fe')
def fe():
    return render_template('fe.html')

@app.route('/arrependimento')
def arrependimento():
    return render_template('arrependimento.html')

@app.route('/amizade')
def amizade():
    return render_template('amizade.html')

@app.route('/casamento')
def casamento():
    return render_template('casamento.html')

@app.route('/paz')
def paz():
    return render_template('paz.html')

@app.route('/forca')
def forca():
    return render_template('forca.html')

@app.route('/familia')
def familia():
    return render_template('familia.html')

@app.route('/cura')
def cura():
    return render_template('cura.html')

@app.route('/trabalho')
def trabalho():
    return render_template('trabalho.html')

@app.route('/vergonha')
def vergonha():
    return render_template('vergonha.html')

@app.route('/gratidao')
def gratidao():
    return render_template('gratidao.html')

@app.route('/traicao')
def traicao():
    return render_template('traicao.html')

@app.route('/medo')
def medo():
    return render_template('medo.html')

@app.route('/morte')
def morte():
    return render_template('morte.html')

@app.route('/vidaeterna')
def vidaeterna():
    return render_template('vidaeterna.html')

@app.route('/perdao')
def perdao():
    return render_template('perdao.html')

@app.route('/coragem')
def coragem():
    return render_template('coragem.html')