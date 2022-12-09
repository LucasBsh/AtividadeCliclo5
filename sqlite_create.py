# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sqlite3

con = sqlite3.connect('imc.db')
cur = con.cursor()

sql = 'create table imc'\
      '(id integer primary key, ' \
      'nome varchar(100), ' \
      'altura varchar(100), '\
      'peso varchar(50), ' \
      'imc varchar(50), ' \
      'imcValor varchar(50))'
cur.execute(sql)

con.close()

print "Banco criado com sucesso"