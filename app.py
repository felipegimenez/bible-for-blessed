import os
import json
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/amor')
def amor():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_amor.json').read())
    return render_template('amor.html', versiculos=versiculos)

@app.route('/fe')
def fe():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_fe.json').read())
    return render_template('fe.html', versiculos=versiculos)

@app.route('/arrependimento')
def arrependimento():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_arrependimento.json').read())
    return render_template('arrependimento.html', versiculos=versiculos)

@app.route('/amizade')
def amizade():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_amizade.json').read())
    return render_template('amizade.html', versiculos=versiculos)

@app.route('/casamento')
def casamento():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_casamento.json').read())
    return render_template('casamento.html', versiculos=versiculos)

@app.route('/paz')
def paz():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_paz.json').read())
    return render_template('paz.html', versiculos=versiculos)

@app.route('/forca')
def forca():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_forca.json').read())
    return render_template('forca.html', versiculos=versiculos)

@app.route('/familia')
def familia():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_familia.json').read())
    return render_template('familia.html', versiculos=versiculos)

@app.route('/cura')
def cura():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_cura.json').read())
    return render_template('cura.html', versiculos=versiculos)

@app.route('/trabalho')
def trabalho():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_trabalho.json').read())
    return render_template('trabalho.html', versiculos=versiculos)

@app.route('/vergonha')
def vergonha():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_vergonha.json').read())
    return render_template('vergonha.html', versiculos=versiculos)

@app.route('/gratidao')
def gratidao():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_gratidao.json').read())
    return render_template('gratidao.html', versiculos=versiculos)

@app.route('/traicao')
def traicao():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_traicao.json').read())
    return render_template('traicao.html', versiculos=versiculos)

@app.route('/medo')
def medo():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_medo.json').read())
    return render_template('medo.html', versiculos=versiculos)

@app.route('/morte')
def morte():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_morte.json').read())
    return render_template('morte.html', versiculos=versiculos)

@app.route('/vidaeterna')
def vidaeterna():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_vidaeterna.json').read())
    return render_template('vidaeterna.html', versiculos=versiculos)

@app.route('/perdao')
def perdao():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_perdao.json').read())
    return render_template('perdao.html', versiculos=versiculos)

@app.route('/coragem')
def coragem():
    versiculos = json.loads(open('versiculos-por-tema/versiculos_coragem.json').read())
    return render_template('coragem.html', versiculos=versiculos)