from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#importando pillow
from PIL import Image, ImageTk

#importando barra de progresso do tlinter
from tkinter.ttk import Progressbar

#importando matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# tkcalendar 
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando funcoes da view 
from view import bar_valores, inserir_categoria, ver_categoria, inserir_receitas, inserir_gastos


#cores 
co0 = "#2e2d2"  # preta
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - peofit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde

colors =['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

#criando janela 
janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style= ttk.Style(janela)
style.theme_use("clam")

#criando frames para divisao da tela
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0,column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2,column=0, pady=0, padx=10, sticky=NSEW)



#trabalhando no frame cima

#acessando a imagem
app_img = Image.open('log.png.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento Pessoal", width=900,compound=LEFT, padx=5,relief=RAISED, anchor=NW, font=('verdana 20 bold'), bg=co1, fg=co4, )
app_logo.place(x=0, y=0)

# definindo tree como global
global tree

# Função inserir categoria
def inserir_categoria_b():
    nome = e_categoria.get()
       
    lista_inserir = [nome]
    
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    # passando para a funçao inserir gastos presente na view
    inserir_categoria(lista_inserir)
    
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
    
    e_categoria.delete(0,"end")
    #pegando os valores da categoria
    cotegoria_funcao = ver_categoria()
    categoria = []
    
    for i in categorias_funcao:
        categoria.append(i[1])
        
    #atualizando a lista de categorias
        combo_categoria_despesas['values'] = (categoria)
    # passando para a funçao inserir gastos presente na view        
    inserir_categoria(lista_inserir)   
         
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso ')
    
    e_categoria.delete(0,'end')
    
    
    # Pegando os valores da categoria
    categorias_funcao = ver_categoria()
    categoria = []
    
    
    
    for i in categorias_funcao:
        categoria.append(i[1])
    
    #atualizando a lista de categorias
    combo_categoria_despesas['values'] = (categoria)
    
    
    
    
    
    
    
    
#percentagem-----------------

def percentagem():
    l_nome = Label(frameMeio, text ="Porcentagem da Receita gasta", height=1,anchor=NW, font=('verdana 12'), bg=co1, fg=co4)
    l_nome.place(x=7, y=5)
    
    style=ttk.Style()
    style.theme_use('default')
    style.configure("black.horizontal.Tprogressbar", backgroud='#daed6b')
    style.configure('Tprogressbar',thickness=25)
    
    
     
    bar = Progressbar(frameMeio, length=180)
    bar.place(x=10, y=35)
    bar['value'] = 50
 
    valor =50
 
    l_percentagem = Label(frameMeio, text ="{:,.2f}%".format(valor), height=1,anchor=NW, font=('verdana 12'), bg=co1, fg=co4)
    l_percentagem.place(x=200, y=35)



# funçao para grafico bars-----------------
 
def grafico_bar():
    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6236]
    
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='ambos', tight=Nenhum)
    
    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    # crie uma lista para coletar os dados plt.patches 

    c = 0
    # definir rótulos de barras individuais usando a lista acima
    for i in ax.patches:
        # get_x puxa para a esquerda ou para a direita; get_height empurra para cima ou para baixo
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)


# funcao de resumo total
def resumo():
    valor = [500,600,420]
    
    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=132)
    l_linha = Label(frameMeio, text="Total Despesas Mensais      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg="#83a9e6")
    l_linha.place(x=309, y=115)
    l_linha = Label(frameMeio, text="R${:,.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=co1, fg="#545454")
    l_linha.place(x=309, y=150)
    
    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=52)
    l_linha = Label(frameMeio, text="Total Renda Mensal      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg="#83a9e6")
    l_linha.place(x=309, y=35)
    l_linha = Label(frameMeio, text="R${:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co1, fg="#545454")
    l_linha.place(x=309, y=70)
    
    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=207)
    l_linha = Label(frameMeio, text="Total Saldo da Caixa      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg="#83a9e6")
    l_linha.place(x=309, y=190)
    l_linha = Label(frameMeio, text="R${:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co1, fg="#545454")
    l_linha.place(x=309, y=220)
    
frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_pie.place(x=415, y=5)

# funcao grafico pie
def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

# only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frameMeio)
    canva_categoria.get_tk_widget().place(x=415, y=5)
    
    
percentagem()
grafico_bar()
resumo()
grafico_pie()


#criando frame dentro do frame baixo
frame_renda = Frame(frameBaixo, width=300, height=250, bg=co1)
frame_renda.grid(row=0,column=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_operacoes.grid(row=0,column=1, padx=5)

frame_configuracao = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_configuracao.grid(row=0,column=2, padx=5)

#Tabela Renda Mensal
app_tabela = Label(frameMeio, text=" Tabela Receitas e Despesas", anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
app_tabela.place(x=5, y=309)

# funçao para mostrar tabela
def mostrar_renda():
    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)



mostrar_renda()


# Configuracoes Despesas
l_info = Label(frame_operacoes, text='Insire novas despesas', height=1,anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)

# categoria------
l_categoria = Label(frame_operacoes, text='Categoria', height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_categoria.place(x=10, y=40)

# Pegando categorias
categoria_funcao=['Viagem', 'Comida']
categoria = []

for i in categoria_funcao:
    categoria.append(i[1])
    
    combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=10, font=('Ivy 10'))
    combo_categoria_despesas['values'] = (categoria)
    combo_categoria_despesas.place(x=110, y=41)
    
    # Despesas------
l_cal_despesas = Label(frame_operacoes, text='Data', height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_cal_despesas.place(x=10, y=70)
e_cal_despesas = DateEntry(frame_operacoes,width=12, background='darkblue', foreground='white', borderwisth=2, year=2)
e_cal_despesas.place(x=110, y=71)    

    # Valor------
l_valor_despesas = Label(frame_operacoes, text='Quatia Total', height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_valor_despesas.place(x=10, y=100)
e_valor_despesas = Entry(frame_operacoes, width=14,justify='left',relief='solid')
e_valor_despesas.place(x=110, y=101)

# Botao Inserir
img_add_despesas = Image.open('sinais.png')
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)

botao_inserir_despesas = Button(frame_operacoes, image=img_add_despesas, text=" Adicionar".upper(), width=80,compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co2, overrelief=RIDGE )
botao_inserir_despesas.place(x=110, y=131)

# Botao excluir
l_excluir = Label(frame_operacoes, text='Excluir ação', height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_excluir.place(x=10, y=190)

img_delete = Image.open('menos.png')
img_delete = img_delete.resize((17,17))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frame_operacoes, image=img_delete, text=" Deletar".upper(), width=80,compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co3, overrelief=RIDGE )
botao_deletar.place(x=110, y=190)

# Configurando Receitas

l_info = Label(frame_configuracao, text='Insire novas receitas', height=1,anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)
    
# calendario------
l_cal_receitas = Label(frame_configuracao, text='Data', height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_cal_receitas.place(x=10, y=40)
e_cal_receitas = DateEntry(frame_configuracao, width=12, background='darkblue', foreground='white', borderwisth=2, year=2)
e_cal_receitas.place(x=110, y=41) 
    
# Valor------
l_valor_receitas = Label(frame_configuracao, text='Quatia Total', height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_valor_receitas.place(x=10, y=70)
e_valor_receitas = Entry(frame_configuracao, width=14,justify='left',relief='solid')
e_valor_receitas.place(x=110, y=71)

# Botao Inserir
img_add_receitas = Image.open('sinais.png')
img_add_receitas = img_add_receitas.resize((17,17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)

botao_inserir_receitas = Button(frame_configuracao, image=img_add_receitas, text=" Adicionar".upper(), width=80,compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co2, overrelief=RIDGE )
botao_inserir_receitas.place(x=110, y=131)

# Operação Nova Categoria

l_info = Label(frame_configuracao, text='Categoria', height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=160)


e_categoria = Entry(frame_configuracao, width=14,justify='left',relief='solid')
e_categoria.place(x=110, y=160)

# Botao Inserir
img_add_categoria = Image.open('sinais.png')
img_add_categoria = img_add_categoria.resize((17,17))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria)
botao_inserir_categoria = Button(frame_configuracao,command=inserir_categoria_b, image=img_add_categoria, text=" Adicionar".upper(), width=80,compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co2, overrelief=RIDGE )
botao_inserir_categoria.place(x=110, y=190)




janela.mainloop()