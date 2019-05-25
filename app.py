from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/amor')
def amor():
    versiculos = [  
                    {  
                        "title":"1João 4:8",
                        "verse":"Aquele que não ama não conhece a Deus, pois Deus é amor.",
                        "url":"https://www.bible.com/pt/bible/1608/1JN.4.ARA",
                    },
                    {  
                        "title":"Colossenses 3:14",
                        "verse":"acima de tudo isto, porém, esteja o amor, que é o vínculo da perfeição.",
                        "url":"https://www.bible.com/pt/bible/1608/COL.3.ARA",
                    },
                    {  
                        "title":"João 3:16",
                        "verse":"Porque Deus amou ao mundo de tal maneira que deu o seu Filho unigênito, para que todo o que nele crê não pereça, mas tenha a vida eterna.",
                        "url":"https://www.bible.com/pt/bible/1608/JHN.3.ARA",
                    },
                    {  
                        "title":"1João 4:7",
                        "verse":"Amados, amemo-nos uns aos outros, porque o amor procede de Deus; e todo aquele que ama é nascido de Deus e conhece a Deus.",
                        "url":"https://www.bible.com/pt/bible/1608/1JN.4.ARA",
                    },
                    {  
                        "title":"1Coríntios 13:4-7",
                        "verse":"O amor é paciente, é benigno; o amor não arde em ciúmes, não se ufana, não se ensoberbece, não se conduz inconvenientemente, não procura os seus interesses, não se exaspera, não se ressente do mal; não se alegra com a injustiça, mas regozija-se com a verdade; tudo sofre, tudo crê, tudo espera, tudo suporta.",
                        "url":"https://www.bible.com/pt/bible/1608/1CO.13.ARA",
                    },
                    {  
                        "title":"Romanos 5:8-10",
                        "verse":"Mas Deus prova o seu próprio amor para conosco pelo fato de ter Cristo morrido por nós, sendo nós ainda pecadores. Logo, muito mais agora, sendo justificados pelo seu sangue, seremos por ele salvos da ira. Porque, se nós, quando inimigos, fomos reconciliados com Deus mediante a morte do seu Filho, muito mais, estando já reconciliados, seremos salvos pela sua vida;",
                        "url":"https://www.bible.com/pt/bible/1608/RO.5.ARA",
                    },
                    {  
                        "title":"1João 4:9",
                        "verse":"Nisto se manifestou o amor de Deus em nós: em haver Deus enviado o seu Filho unigênito ao mundo, para vivermos por meio dele.",
                        "url":"https://www.bible.com/pt/bible/1608/1JN.4.ARA",
                    },
                    {  
                        "title":"1João 4:10",
                        "verse":"Nisto consiste o amor: não em que nós tenhamos amado a Deus, mas em que ele nos amou e enviou o seu Filho como propiciação pelos nossos pecados.",
                        "url":"https://www.bible.com/pt/bible/1608/1JN.4.ARA",
                    }
    ]
    return render_template('amor.html', versiculos=versiculos)

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