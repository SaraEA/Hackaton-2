# Importar
from flask import Flask, render_template, redirect, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from random import choice
import requests
import time
from speech import speech
from game import *


app = Flask(__name__)
app.secret_key = "supersecretkey"
nivel = "1"


# La primera página
@app.route('/')
def index():
    session["intentos"]=0
    session['score'] = 0
    session['correcto']=0
    return render_template('inicio.html', word=None, score=session['score'], spoken_word=None, error=None, recognizing=False)


@app.route('/<size>')
def lights(size):
    global nivel
    nivel = size
    try:
        return render_template(f'nivel{nivel}.html',size=size) 
    except:
        return render_template("inicio.html")

@app.route('/favicon.ico')
def favicon():
    return render_template('inicio.html')
@app.route('/voices', methods=["POST"])
def voices():
    global nivel
    text = None
    tips_eco= None
    
    try:
        correct_word = request.form["correct_word"]
        text= speech()
        num, tips_eco = compara(correct_word, text)
        error= None
        print(compara(correct_word, text ))
        print(text)

        if num==1:
            session["score"]+=1
            session['correcto']+=1
            session["intentos"]+=1
            if session["score"] >=10:
                return render_template("game_over.html", score=session["score"], intentos= session["intentos"], correcto=session['correcto'])
        elif num==2:
            session["score"]+=2
            session['correcto']+=1
            session["intentos"]+=1
            if session["score"] >=10:
                return render_template("game_over.html", score=session["score"], intentos= session["intentos"], correcto=session['correcto'])
        else:
            session["intentos"]+=1
            error= "Palabra pronunciada: "+ text + " La palabra correcta era: " + correct_word
            return render_template(f"nivel{nivel}.html",word=None, score=session['score'], intentos= session["intentos"], spoken_word=None, error=error, recognizing=False, tips=tips_eco)
    except:
        session["intentos"]+=1
        error= "No pude reconocer lo que dijiste"
        
    return render_template(f"nivel{nivel}.html",word=None, score=session['score'], intentos= session["intentos"], spoken_word=text, error=error, recognizing=False, tips=tips_eco)


@app.route('/mostrar', methods=["POST"])
def mostrar():
    global nivel
    word = play_game(nivel)
    return render_template(f"nivel{nivel}.html", word=word, score=session['score'], spoken_word=None, error=None, recognizing=False)


@app.route('/recognize', methods=['POST'])
def recognize():
    global nivel
    correct_word = request.form['correct_word']
    return render_template(f'nivel{nivel}.html', word=correct_word, score=session['score'], spoken_word=None, error=None, recognizing=True)


app.run(debug=True)
