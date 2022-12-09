# coding=utf-8
# !/usr/bin/env python
# -*- coding :latin1 -*-
import math
import sqlite3

nome = raw_input('Digite seu nome: ')
altura = input('Digite sua altura em metros: ')
peso = input('Digite seu peso em KG: ')
imc = ''
imcValor = peso / altura**2

if (imcValor < 17):
	imc = "Muito abaixo do peso"

elif (imcValor >= 17 and imcValor < 18.5 ):
	imc = "Abaixo do peso"

elif imcValor > 18.5 and imcValor < 24.5:
	imc = "Peso normal"

elif imcValor > 25 and imcValor < 30:
	imc = "Acima do peso"

elif imcValor > 30 and imcValor < 35:
	imc = "Obesidade I"

elif imcValor > 35 and imcValor < 40:
	imc = "Obesidade II (severa)"

elif imcValor > 40:
	imc = "Obesidade III (mórbida)"

print imc

con = sqlite3.connect('imc.db')
con.text_factory = str
cur = con.cursor()

sql = 'insert into imc values (null , ? , ? , ? , ?, ?)'

recset = (nome, altura, peso, imc, imcValor)

cur.execute(sql, recset)

con.commit()

con.close()