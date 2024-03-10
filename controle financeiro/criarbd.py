#importando sqlite
import sqlite3 as lite

#criando conexao
con = lite.connect("dados.db")

#criando tabela de categoria
with con:
        cur = con.cursor()
        cur.execute("create table categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
        
        #criando tabela de receitas
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")
            
            
            
            #criando tabela de gasto
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")
            
            