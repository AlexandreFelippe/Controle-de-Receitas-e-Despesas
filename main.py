from tkinter import Frame, NSEW, NW
from tkinter import Tk, ttk, Label, RAISED, LEFT
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# from matplotlib.figure import Figure
from tkcalendar import DateEntry
# from datetime import date
from tkinter import Entry, Button, RIDGE


preto = "#000000"
branca = "#FFFFFF"
verde = "#00FF00"
valor = "#38576B"
letra = "#403d3d"
profit = "#e06636"
verde = "#3fbfb9"
verde1 = "#263238"
verde2 = "#e9edf5"

colors = ["#5588bb", "#66bbbb", "#99bb55", "#ee9944", "#444466", "#bb5555"]


janela = Tk()
janela.title("Controle Financeiro")
janela.geometry("1050x670")
janela.configure(bg=verde2)

style = ttk.Style(janela)
style.theme_use("clam")
# criando frames
frame1 = Frame(janela, width=1043, height=50, bg=branca, relief="flat")
frame1.grid(row=0, column=0)

frame2 = Frame(
    janela, width=1043, height=361, bg=branca, pady=20, relief="raised")
frame2.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame3 = Frame(janela, width=1043, height=300, bg=branca, relief="flat")
frame3.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

# frame1
img = Image.open("cofrinho.jpg")
img = img.resize((45, 45))
img = ImageTk.PhotoImage(img)

img_logo = Label(
    frame1,
    image=img,
    text=" Olá, seja bem-vindo(a) ao seu controle financeiro",
    font=("Arial", 16),
    width=1050,
    compound=LEFT,
    padx=5,
    relief=RAISED,
    anchor=NW,
    bg=branca,
)
img_logo.place(x=0, y=0)


# frame2
def percentual_gastos():
    label_porcentagem = Label(
        frame2,
        text="Percentual da Receita Gasta",
        font=("Arial", 12),
        height=1,
        anchor=NW,
        bg=branca,
        fg=valor,
    )
    label_porcentagem.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("black.Horizontal.TProgressbar", background="#daed6b")
    style.configure("TProgressbar", thicness=25)

    label_progressbar = Progressbar(
        frame2, length=180, style="black.Horizontal.TProgressbar"
    )
    label_progressbar.place(x=10, y=35)
    label_progressbar["value"] = 50

    percentual = 50

    label_porcentagem_text = Label(
        frame2,
        text="{:.2f}%".format(percentual),
        font=("Arial", 16),
        anchor=NW,
        bg=branca,
        fg=valor,
    )
    label_porcentagem_text.place(x=200, y=35)


def grafico():
    lista_categorias = ["Renda", "Despesas", "Saldo"]
    lista_valores = [1000, 600, 400]

    fig = plt.figure(figsize=(4, 3.45), dpi=60)
    ax = fig.add_subplot(111)
    # ax.autoscale(enable=True, axis='both, tight=True')

    ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)

    counter = 0
    for i in ax.patches:
        ax.text(
            i.get_x() - 0.001,
            i.get_height() + 0.5,
            str("{:.2f}".format(lista_valores[counter])),
            fontsize=17,
            fontstyle="italic",
            verticalalignment="bottom",
            color="dimgrey",
        )
        counter += 1

    ax.set_xticks(range(len(lista_categorias)))
    ax.set_xticklabels(lista_categorias, fontsize=16)
    ax.spines["bottom"].set_color("#ffffff")
    ax.spines["bottom"].set_linewidth(1)
    ax.spines["right"].set_linewidth(0)
    ax.spines["top"].set_linewidth(0)
    ax.spines["left"].set_linewidth(1)
    ax.spines["left"].set_color("#cccccc")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(fig, master=frame2)
    canva.get_tk_widget().place(x=10, y=70)


percentual_gastos()
grafico()

frame_renda = Frame(frame3, width=300, height=250, bg=branca)
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frame3, width=220, height=250, bg=branca)
frame_operacoes.grid(row=0, column=1, padx=5)

frame_configuracao = Frame(frame3, width=220, height=250, bg=branca)
frame_configuracao.grid(row=0, column=2, padx=5)

frame_gra_2 = Frame(frame2, width=300, height=250, bg=branca)
frame_gra_2.place(x=415, y=5)


img_tabela = Label(
    frame2,
    text=" Tabela Receitas e Despesas",
    font=("Arial", 12),
    anchor=NW,
    bg=branca,
    fg=valor,
)
img_tabela.place(x=5, y=309)


def resumo():
    valor = [345, 225, 534]
    label_linha = Label(
        frame2,
        text="",
        width=215,
        height=1,
        anchor=NW,
        font=("arial 1"),
        bg="#545454",
    )
    label_linha.place(x=309, y=52)
    label_sumario = Label(
        frame2,
        text="Total Renda Mensal      ".upper(),
        height=1,
        anchor=NW,
        font=("Verdana 12"),
        bg=branca,
        fg="#83a9e6",
    )
    label_sumario.place(x=306, y=35)
    label_sumario = Label(
        frame2,
        text="R$ {:,.2f}".format(valor[0]),
        height=1,
        anchor=NW,
        font=("arial 17 "),
        bg=branca,
        fg="#545454",
    )
    label_sumario.place(x=306, y=70)

    label_linha = Label(
        frame2,
        text="",
        width=215,
        height=1,
        anchor=NW,
        font=("arial 1 "),
        bg="#545454",
    )
    label_linha.place(x=309, y=132)
    label_sumario = Label(
        frame2,
        text="Total Despesas Mensais".upper(),
        height=1,
        anchor=NW,
        font=("Verdana 12"),
        bg=branca,
        fg="#83a9e6",
    )
    label_sumario.place(x=306, y=115)
    label_sumario = Label(
        frame2,
        text="R$ {:,.2f}".format(valor[1]),
        height=1,
        anchor=NW,
        font=("arial 17 "),
        bg=branca,
        fg="#545454",
    )
    label_sumario.place(x=306, y=150)

    label_linha = Label(
        frame2,
        text="",
        width=215,
        height=1,
        anchor=NW,
        font=("arial 1 "),
        bg="#545454",
    )
    label_linha.place(x=309, y=207)
    label_sumario = Label(
        frame2,
        text="Total Saldo da Caixa    ".upper(),
        height=1,
        anchor=NW,
        font=("Verdana 12"),
        bg=branca,
        fg="#83a9e6",
    )
    label_sumario.place(x=306, y=190)
    label_sumario = Label(
        frame2,
        text="R$ {:,.2f}".format(valor[2]),
        height=1,
        anchor=NW,
        font=("arial 17 "),
        bg=branca,
        fg="#545454",
    )
    label_sumario.place(x=306, y=220)


resumo()


def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)
    lista_valores = [345, 225, 534]
    lista_categorias = ['Alimentação', 'Aluguel', 'Vestuário']

    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = []
    for i in lista_categorias:
        explode.append(0.05)
    ax.pie(
        lista_valores,
        explode=explode,
        wedgeprops=dict(width=0.2),
        autopct='%1.1f%%',
        colors=colors,
        shadow=True,
        startangle=90)
    ax.legend(
        lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_2)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


grafico_pie()


def mostrar_renda():
    tabela_head = ["id", "Categoria", "Data", "Valor"]

    lista_itens = [[0, 2, 3, 4], [1, 2, 3, 4], [2, 2, 3, 4], [3, 2, 3, 4]]

    global tree

    tree = ttk.Treeview(
        frame_renda,
        selectmode="extended",
        columns=tabela_head,
        show="headings"
    )

    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    hsb.grid(column=0, row=1, sticky="ew")

    hd = ["center", "center", "center", "center"]
    h = [30, 100, 100, 100]
    n = 0

    for i in tabela_head:
        tree.heading(i, text=i.title(), anchor="center")
        tree.column(i, width=h[n], anchor=hd[n])

        n += 1

    for i in lista_itens:
        tree.insert("", "end", values=i)


label_titulo = Label(
    frame_operacoes,
    text="Insira novas despesas",
    height=1,
    font=("Arial", 10, "bold"),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_titulo.place(x=10, y=10)

label_categoria = Label(
    frame_operacoes,
    text="Categoria",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)

label_categoria.place(x=10, y=40)

categoria_box = ["Viagem", "Comida"]
categoria = []

for i in categoria_box:
    categoria.append(i[1])

combo_categoria_despesas = ttk.Combobox(
    frame_operacoes, width=10, font=("Arial", 10))
combo_categoria_despesas["values"] = categoria
combo_categoria_despesas.place(x=110, y=41)

label_cal_despesas = Label(
    frame_operacoes,
    text="Data",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)

label_cal_despesas.place(x=10, y=70)

cal_despesas = DateEntry(
    frame_operacoes,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    year=2023,
)

cal_despesas.place(x=110, y=71)

label_valor_despesas = Label(
    frame_operacoes,
    text="Valor",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_valor_despesas.place(x=10, y=100)

valor_despesas = Entry(
    frame_operacoes, width=12, justify="left", relief="solid")
valor_despesas.place(x=110, y=101)

img_add_despesa = Image.open("add.png")
img_add_despesa = img_add_despesa.resize((17, 17))
img_add_despesa = ImageTk.PhotoImage(img_add_despesa)

add_button = Button(
    frame_operacoes,
    image=img_add_despesa,
    text="Adicionar",
    font=("Ivy 7 bold"),
    overrelief=RIDGE,
    width=80,
    compound=LEFT,
    anchor=NW,
    bg=branca,
    fg=preto,
)
add_button.place(x=110, y=131)


img_delete_despesa = Image.open("remove.png")
img_delete_despesa = img_delete_despesa.resize((17, 17))
img_delete_despesa = ImageTk.PhotoImage(img_delete_despesa)

delete_button = Button(
    frame_operacoes,
    image=img_delete_despesa,
    text="Excluir",
    font=("Ivy 7 bold"),
    overrelief=RIDGE,
    width=80,
    compound=LEFT,
    anchor=NW,
    bg=branca,
    fg=preto,
)
delete_button.place(x=110, y=171)


label_receitas = Label(
    frame_configuracao,
    text="Insira novas receitas",
    height=1,
    font=("Arial", 10, "bold"),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_receitas.place(x=10, y=10)

label_categoria_receitas = Label(
    frame_configuracao,
    text="Data",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_categoria_receitas.place(x=10, y=40)
entrada_categoria_receitas = DateEntry(
    frame_configuracao,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    year=2023,
    justify="left",
    relief="solid"
    )
entrada_categoria_receitas.place(x=110, y=41)

label_cal_receitas = Label(
    frame_configuracao,
    text="Valor",
    height=1,
    font=("Arial 10"),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_cal_receitas.place(x=10, y=71)

cal_receitas = Entry(
    frame_configuracao, width=12, justify="left", relief="solid")
cal_receitas.place(x=110, y=71)

img_add_receitas = Image.open("add.png")
img_add_receitas = img_add_receitas.resize((17, 17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)

add_button = Button(
    frame_configuracao,
    image=img_add_receitas,
    text="Adicionar",
    font=("Ivy 7 bold"),
    overrelief=RIDGE,
    width=80,
    compound=LEFT,
    anchor=NW,
    bg=branca,
    fg=preto,
)
add_button.place(x=110, y=105)

label_insert_category = Label(
    frame_configuracao,
    text="Categoria",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_insert_category.place(x=10, y=140)

entry_category = Entry(
    frame_configuracao, width=12, justify="left", relief="solid")
entry_category.place(x=110, y=160)

img_add_category = Image.open("add.png")
img_add_category = img_add_category.resize((17, 17))
img_add_category = ImageTk.PhotoImage(img_add_category)

add_button = Button(
    frame_configuracao,
    image=img_add_category,
    text="Adicionar Categoria",
    font=("Ivy 7 bold"),
    overrelief=RIDGE,
    width=80,
    compound=LEFT,
    anchor=NW,
    bg=branca,
    fg=preto,
)
add_button.place(x=110, y=190)

mostrar_renda()
janela.mainloop()
