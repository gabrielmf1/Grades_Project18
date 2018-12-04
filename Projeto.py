#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:51:57 2018

@author: gabrielmiras
"""

from __future__ import print_function
import sys

db = {
      "Matematica da Variação": {
          "media": 0.0,
          "notas":{
                  "Prova Intermediária": {
                      "nota": 0.0,
                      "peso": 0.30
                  },
                  "Prova Final": {
                      "nota": 0.0,
                      "peso": 0.50
                  },
                  "Trabalhos": {
                      "nota": 0.0,
                      "peso": 0.10
                  },
                  "Diagnósticos": {
                      "nota": 0.0,
                      "peso": 0.10
                  }
          }
      },
      "Física do Movimento": {
          "media": 0.0,
          "notas":{
                  "Prova Intermediária": {
                      "nota": 0.0,
                      "peso": 0.30
                  },
                  "Prova Final": {
                      "nota": 0.0,
                      "peso": 0.50
                  },
                  "Trabalhos": {
                      "nota": 0.0,
                      "peso": 0.10
                  },
                  "Diagnósticos": {
                      "nota": 0.0,
                      "peso": 0.10
                  }
          }
      },
      "Ciência dos Dados": {
          "media": 0.0,
          "notas":{
                  "Prova Intermediária": {
                      "nota": 0.0,
                      "peso": 0.30
                  },
                  "Prova Final": {
                      "nota": 0.0,
                      "peso": 0.50
                  },
                  "Trabalhos": {
                      "nota": 0.0,
                      "peso": 0.10
                  },
                  "Diagnósticos": {
                      "nota": 0.0,
                      "peso": 0.10
                  }
          }
      },
      "Co-Design de Aplicativos": {
          "media": 0.0,
          "notas":{
                  "Prova Intermediária": {
                      "nota": 0.0,
                      "peso": 0.30
                  },
                  "Prova Final": {
                      "nota": 0.0,
                      "peso": 0.50
                  },
                  "Trabalhos": {
                      "nota": 0.0,
                      "peso": 0.10
                  },
                  "Diagnósticos": {
                      "nota": 0.0,
                      "peso": 0.10
                  }
          }
      },
      "Acionamentos Elétricos": {
          "media": 0.0,
          "notas":{
                  "Prova Intermediária": {
                      "nota": 0.0,
                      "peso": 0.30
                  },
                  "Prova Final": {
                      "nota": 0.0,
                      "peso": 0.50
                  },
                  "Trabalhos": {
                      "nota": 0.0,
                      "peso": 0.10
                  },
                  "Diagnósticos": {
                      "nota": 0.0,
                      "peso": 0.10
                  }
          }
      }
}


dbu = {
    0: {
        "username": "gabrielmf1",
        "password": "677292"           
    }
             
}

contagem_login = 0
             
def calcula_media(db, materia):
    print("oi")
    media_final = 0.0
    
    for prova in db[materia]["notas"]:
        print(db[materia]["notas"])
        media_final += db[materia]["notas"][prova]["nota"] * db[materia]["notas"][prova]["peso"]
        
    return media_final


#def verifica_senha(dbu, senha):
#    if senha >= 4:
#        return sem mensagem de erro
#    else:
#        return mensagem de erro
    
#def mensagem_erro(string):
#    if len(string) > 0:
#        sem mensagem de erro
#    else:
#        mensagem de erro = "Não pode ser vazio."


        
from flask import Flask, render_template, request, session, flash
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nota = request.form.get("nota")
        materia = request.form.get("materia")
        tp = request.form.get("tipo_de_prova")
        
        print(nota, materia, tp)
        db[materia]["notas"][tp]["nota"] = int(nota)
    lista_materias = []
    
    for materia in db:
        media = calcula_media(db, materia)
    
        lista_materias.append([materia, media])
            
        
    
        
        
    return render_template("home_completo.html", lista_materias=lista_materias)

@app.route('/login')
def login():
    if not session.get('logged_in'):
        return render_template('user.html')
    else:
        return render_template("home_completo.html")
 
@app.route('/signin', methods=['POST'])
def do_admin_login():
    for e in dbu:
        if request.form['password'] == dbu[e]["password"] and request.form['username'] == dbu[e]["username"]:
            session['logged_in'] = True
        else:
            flash('wrong password!')
        return login()

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)