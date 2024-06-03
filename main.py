from tkinter import Frame, NSEW, NW
from tkinter import Tk, ttk, Label, RAISED, LEFT
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
from tkinter import Entry, Button, RIDGE, messagebox
import view

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
janela.geometry("1100x670")
janela.configure(bg=verde2)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frames
frame1 = Frame(janela, width=1350, height=50, bg=branca, relief="flat")
frame1.grid(row=0, column=0)

frame2 = Frame(
    janela, width=1043, height=361, bg=branca, pady=20, relief="raised")
frame2.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame3 = Frame(janela, width=1350, height=300, bg=branca, relief="flat")
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


# button_details_page = Button(
#     frame2,
#     text="Detalhes",
#     command=view.show_new_window,
#     font=("Ivy 7 bold"),
#     overrelief=RIDGE,
#     width=10,
#     anchor=NW,
#     bg=verde1,
#     fg=branca,
# )
# button_details_page.place(x=1000, y=10)

global tree


def insert_category():
    name = entry_category.get()

    list_insert = [name]

    for i in list_insert:
        if i == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
    view.inserir_categoria(list_insert)
    messagebox.showinfo("Sucesso", "Categoria inserida com sucesso")
    entry_category.delete(0, "end")

    function_category = view.listar_categorias()
    category = []

    for i in function_category:
        category.append(i[1])

    combo_categoria_despesas["values"] = category


def insert_description():
    name = entry_description.get()

    list_insert = [name]

    for i in list_insert:
        if i == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
    view.inserir_descricao(list_insert)
    messagebox.showinfo("Sucesso", "Descrição inserida com sucesso")
    combo_descrição_despesas.set("end")

    function_description = view.listar_descrição()
    description = []

    for i in function_description:
        description.append(i[1])

    combo_descrição_despesas["values"] = description


def insert_revenue():
    name = "Receita"
    date = entrada_categoria_receitas.get()
    description = "extra"
    value = cal_receitas.get()

    list_insert = [name, date, description, float(value)]

    for i in list_insert:
        if i == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
    view.inserir_receita(list_insert)
    messagebox.showinfo("Sucesso", "Receita inserida com sucesso")
    cal_receitas.delete(0, "end")
    entrada_categoria_receitas.delete(0, "end")

    # atualizando dados
    table()
    resumo()
    pie_graph()
    expenses_percentage()
    grafico_barra()


def insert_expense():
    name = combo_categoria_despesas.get()
    date = cal_despesas.get()
    description = combo_descrição_despesas.get()
    value = valor_despesas.get()

    list_insert = [name, date, description, float(value)]

    for i in list_insert:
        if i == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
    view.inserir_despesa(list_insert)
    messagebox.showinfo("Sucesso", "Despesa inserida com sucesso")
    cal_despesas.delete(0, "end")
    valor_despesas.delete(0, "end")

    # atualizando dados
    table()
    resumo()
    pie_graph()
    expenses_percentage()
    grafico_barra()


def delete():
    try:
        treev_data = tree.focus()
        treev_dict = tree.item(treev_data)
        treev_values = treev_dict["values"]
        if not treev_values:
            messagebox.showerror("Erro", "Nenhum item selecionado")
            return
        item_id = treev_values[0]

        # Verifica se o item é uma despesa ou receita
        item_categoria = treev_values[1]

        if item_categoria in (
            [categoria[1] for categoria in view.listar_categorias()]
        ):
            view.excluir_item("Despesas", item_id)
            messagebox.showinfo("Sucesso", "Despesa excluída com sucesso")
        else:
            view.excluir_item("Receitas", item_id)
            messagebox.showinfo("Sucesso", "Receita excluída com sucesso")

        # Atualizando dados
        table()
        resumo()
        pie_graph()
        expenses_percentage()
        grafico_barra()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir dado: {str(e)}")


# frame2
def expenses_percentage():
    label_porcentagem = Label(
        frame2,
        text="Percentual Receita Restante",
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
    label_progressbar["value"] = view.line_chart()

    percentual = view.line_chart()

    label_porcentagem_text = Label(
        frame2,
        text="{:.2f}%".format(percentual),
        font=("Arial", 16),
        anchor=NW,
        bg=branca,
        fg=valor,
    )
    label_porcentagem_text.place(x=200, y=35)


def grafico_barra():
    lista_categorias = ["Renda", "Despesas", "Saldo"]
    lista_valores = view.bar_graph()

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


expenses_percentage()
grafico_barra()

frame_renda = Frame(frame3, width=300, height=280, bg=branca)
frame_renda.grid(row=0, column=0)

frame_despesas = Frame(frame3, width=220, height=280, bg=branca)
frame_despesas.grid(row=0, column=1, padx=5)

frame_receitas = Frame(frame3, width=250, height=280, bg=branca)
frame_receitas.grid(row=0, column=2, padx=5)

frame_gra_2 = Frame(frame2, width=300, height=250, bg=branca)
frame_gra_2.place(x=500, y=5)

frame_add_category_description = Frame(
    frame3, width=300, height=280, bg=branca)
frame_add_category_description.grid(row=0, column=3, padx=5)

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
    valor = view.bar_graph()
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


def pie_graph():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)
    lista_valores = view.pie_chart()[1]
    lista_categorias = view.pie_chart()[0]

    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = []
    for i in lista_categorias:
        explode.append(0.05)
    ax.pie(
        lista_valores,
        explode=explode,
        wedgeprops=dict(width=0.2),
        autopct="%1.1f%%",
        colors=colors,
        shadow=True,
        startangle=90,
    )
    ax.legend(
        lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_2)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


pie_graph()


def table():
    tabela_head = ["ID", "Cat", "Data", "Desc", "Valor"]

    despesas = view.listar_despesas()
    receitas = view.listar_receitas()

    # Concatenar as listas de despesas e receitas
    lista_itens = despesas + receitas

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

    hd = ["center", "center", "center", "center", "center"]
    h = [0, 80, 70, 70, 70]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor="center")
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in lista_itens:
        tree.insert("", "end", values=item)


label_titulo = Label(
    frame_despesas,
    text="Insira novas despesas",
    height=1,
    font=("Arial", 10, "bold"),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_titulo.place(x=10, y=10)

label_categoria = Label(
    frame_despesas,
    text="Categoria",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)

label_categoria.place(x=10, y=40)

categoria_box = view.listar_categorias()
categoria = []

for i in categoria_box:
    categoria.append(i[1])

combo_categoria_despesas = ttk.Combobox(
    frame_despesas, width=10, font=("Arial", 10))
combo_categoria_despesas["values"] = categoria
combo_categoria_despesas.place(x=110, y=41)

label_descrição = Label(
    frame_despesas,
    text="Descrição",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_descrição.place(x=10, y=70)

descrição_box = view.listar_descrição()
descrição = []

for i in descrição_box:
    descrição.append(i[1])

combo_descrição_despesas = ttk.Combobox(
    frame_despesas, width=10, font=("Arial", 10))
combo_descrição_despesas["values"] = descrição
combo_descrição_despesas.place(x=110, y=71)

label_cal_despesas = Label(
    frame_despesas,
    text="Data",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)

label_cal_despesas.place(x=10, y=100)

cal_despesas = DateEntry(
    frame_despesas,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    year=2023,
)

cal_despesas.place(x=110, y=101)

label_valor_despesas = Label(
    frame_despesas,
    text="Valor",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_valor_despesas.place(x=10, y=131)

valor_despesas = Entry(
    frame_despesas, width=12, justify="left", relief="solid")
valor_despesas.place(x=110, y=131)

img_add_despesa = Image.open("add.png")
img_add_despesa = img_add_despesa.resize((17, 17))
img_add_despesa = ImageTk.PhotoImage(img_add_despesa)

add_button = Button(
    frame_despesas,
    image=img_add_despesa,
    command=insert_expense,
    text="Adicionar",
    font=("Ivy 7 bold"),
    overrelief=RIDGE,
    width=80,
    compound=LEFT,
    anchor=NW,
    bg=branca,
    fg=preto,
)
add_button.place(x=110, y=161)

img_delete_despesa = Image.open("remove.png")
img_delete_despesa = img_delete_despesa.resize((17, 17))
img_delete_despesa = ImageTk.PhotoImage(img_delete_despesa)

delete_button = Button(
    frame_despesas,
    command=delete,
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
delete_button.place(x=110, y=201)

label_receitas = Label(
    frame_receitas,
    text="Insira novas receitas",
    height=1,
    font=("Arial", 10, "bold"),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_receitas.place(x=30, y=10)

label_categoria_receitas = Label(
    frame_receitas,
    text="Data",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_categoria_receitas.place(x=30, y=40)
entrada_categoria_receitas = DateEntry(
    frame_receitas,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    year=2023,
    justify="left",
    relief="solid",
)
entrada_categoria_receitas.place(x=130, y=41)

label_cal_receitas = Label(
    frame_receitas,
    text="Valor",
    height=1,
    font=("Arial 10"),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_cal_receitas.place(x=30, y=71)

cal_receitas = Entry(
    frame_receitas, width=12, justify="left", relief="solid")
cal_receitas.place(x=130, y=71)

img_add_receitas = Image.open("add.png")
img_add_receitas = img_add_receitas.resize((17, 17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)

add_button = Button(
    frame_receitas,
    image=img_add_receitas,
    command=insert_revenue,
    text="Adicionar",
    font=("Ivy 7 bold"),
    overrelief=RIDGE,
    width=80,
    compound=LEFT,
    anchor=NW,
    bg=branca,
    fg=preto,
)
add_button.place(x=130, y=105)

label_receitas = Label(
    frame_add_category_description,
    text="Insira descrição e categoria",
    height=1,
    font=("Arial", 10, "bold"),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_receitas.place(x=30, y=10)

label_insert_category = Label(
    frame_add_category_description,
    text="Categoria",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_insert_category.place(x=30, y=40)

entry_category = Entry(
    frame_add_category_description, width=12, justify="left", relief="solid")
entry_category.place(x=130, y=40)

label_insert_description = Label(
    frame_add_category_description,
    text="Descrição",
    height=1,
    font=("Arial", 10),
    anchor=NW,
    bg=branca,
    fg=valor,
)
label_insert_description.place(x=30, y=110)

entry_description = Entry(
    frame_add_category_description, width=12, justify="left", relief="solid")
entry_description.place(x=130, y=110)

img_add_category = Image.open("add.png")
img_add_category = img_add_category.resize((17, 17))
img_add_category = ImageTk.PhotoImage(img_add_category)

add_category_button = Button(
    frame_add_category_description,
    command=insert_category,
    image=img_add_category,
    text="Adicionar",
    font=("Ivy 7 bold"),
    overrelief=RIDGE,
    width=80,
    compound=LEFT,
    anchor=NW,
    bg=branca,
    fg=preto,
)
add_category_button.place(x=130, y=70)

add_description_button = Button(
    frame_add_category_description,
    command=insert_description,
    image=img_add_category,
    text="Adicionar",
    font=("Ivy 7 bold"),
    overrelief=RIDGE,
    width=80,
    compound=LEFT,
    anchor=NW,
    bg=branca,
    fg=preto,
)
add_description_button.place(x=130, y=140)

table()
janela.mainloop()
