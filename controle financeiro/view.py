#importando sqlite
import sqlite3 as lite

#criando conexao
con = lite.connect("dados.db")


#funcoes de insercao------------------------------

# inserir categoria
def inserir_categoria():
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria(nome) VALUES(?)"
        cur.execute(query, )
        
# inserir receita
def inserir_receitas():
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas(categoria, adicionado_em,valor) VALUES(?,?,?)"
        cur.execute(query, )
        
# inserir gastos
def inserir_gastos():
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em,valor) VALUES(?,?,?)"
        cur.execute(query, )
        
#funcoes de deletar------------------------------

#deletar receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DESLETE FROM Receitas WHERE id=?"
        cur.execute(query, i)
        
        #deletar gastos
def deletar_gastos(i): 
    with con:
        cur = con.cursor()
        query = "DESLETE FROM Gastos WHERE id=?"
        cur.execute(query, i)
        
#funcoes de ver dados------------------------------

#ver categoria
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
            
    return lista_itens

       
#ver receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
            
    return lista_itens


#ver Gastos
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
            
    return lista_itens

# funçao para dados do grafico de barra
def bar_valores():
    #receita Total -----------
    receitas = ver_receitas()
    receitas_lista = []
    
    for i in receitas:
        receitas_lista.append(i[3])

