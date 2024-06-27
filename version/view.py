from tkinter import Frame, Label, RAISED, LEFT, NW, Button, ttk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from model import ControleFinanceiroModel
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import tkinter as tk

fundo_tela = "#1e3743"
frame_bg = "#dfe3ee"
fonte = "#38576B"
colors = ["#5588bb", "#66bbbb", "#99bb55", "#ee9944", "#444466", "#bb5555"]


class ControleFinanceiroView:
    def __init__(self, master):
        self.root = master
        self.model = ControleFinanceiroModel()
        self.criar_tela()
        self.criar_frames()
        self.associar_modelo_com_frames()

    def criar_tela(self):
        self.root.title("Controle Financeiro")
        self.root.geometry("1300x670")
        self.root.configure(bg=fundo_tela)
        self.root.resizable(True, True)
        self.root.maxsize(width=1380, height=800)
        self.root.minsize(width=1100, height=670)

    def criar_frames(self):
        self.frame1 = Frame1(self)
        self.frame2 = Frame2(self)
        self.frame3 = Frame3(self)

    def associar_modelo_com_frames(self):
        self.model.frame2_view = self.frame2
        self.model.frame3_view = self.frame3


class Frame1:
    def __init__(self, controle_financeiro_view):
        self.root = controle_financeiro_view.root
        self.frame1 = Frame(
            self.root, width=1350, height=50, bg=frame_bg, relief="flat", bd=4
        )
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.08)
        self.img = Image.open("version/cofrinho.jpg")
        self.img = self.img.resize((45, 45))
        self.img = ImageTk.PhotoImage(self.img)

        self.img_logo = Label(
            self.frame1,
            image=self.img,
            text=" Bem-vindo(a) ao seu controle financeiro",
            font=("Arial", 16),
            compound=LEFT,
            padx=5,
            relief=RAISED,
            anchor=NW,
            bg=frame_bg,
        )
        self.img_logo.place(relx=0.02, rely=0.02, relwidth=0.95, relheight=1)


class Frame2(Frame):
    def __init__(self, controle_financeiro_view):
        super().__init__(
            controle_financeiro_view.root,
            width=1350,
            height=370,
            bg=frame_bg,
            pady=5,
            relief="raised",
        )
        self.model = controle_financeiro_view.model
        self.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.42)
        self.criar_componentes()
        self.atualizar_frame()

    def criar_componentes(self):
        self.criar_progressbar()
        self.criar_grafico_barras()
        self.criar_resumo()
        self.criar_grafico_pizza()

    def atualizar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.criar_componentes()

    def criar_progressbar(self):
        self.label = Label(
            self,
            text="Percentual da Receita Restante",
            font=("Arial", 12),
            height=1,
            bg=frame_bg,
            fg=fonte,
        )
        self.label.place(x=5, y=5)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("black.Horizontal.TProgressbar", background="#daed6b")
        style.configure("TprogressBar", thickness=25)

        self.label_progressbar = Progressbar(
            self,
            style="black.Horizontal.TProgressbar",
            length=180,
        )
        self.label_progressbar.place(x=5, y=30)
        percentual = self.model.line_chart()
        self.label_progressbar["value"] = percentual

        self.label_percentual_texto = Label(
            self,
            text="{:.2f}%".format(percentual),
            font=("Arial", 12),
            anchor=NW,
            bg=frame_bg,
            fg=fonte,
        )
        self.label_percentual_texto.place(x=200, y=30)

    def criar_grafico_barras(self):
        lista_categorias = ["Renda", "Despesas", "Saldo"]
        lista_valores = self.model.bar_graph()

        fig = plt.figure(figsize=(4, 3.45), dpi=60, facecolor=frame_bg)
        ax = fig.add_subplot(111, facecolor=frame_bg)
        ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)

        for i, rect in enumerate(ax.patches):
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                rect.get_height(),
                str("{:.2f}".format(lista_valores[i])),
                ha="center",
                va="bottom",
                fontsize=14,
                fontstyle="italic",
                color="dimgrey",
            )

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

        canva = FigureCanvasTkAgg(fig, master=self)
        canva.get_tk_widget().place(x=10, y=70)

    def criar_resumo(self):
        valor = self.model.bar_graph()
        self._criar_label_sumario("Total Renda Mensal", valor[0], 35, 70)
        self._criar_label_sumario("Total Despesas Mensais", valor[1], 115, 150)
        self._criar_label_sumario("Total Saldo da Caixa", valor[2], 190, 220)

    def _criar_label_sumario(self, texto, valor, y_texto, y_valor):
        Label(
            self,
            text="",
            width=215,
            height=1,
            anchor=NW,
            font=("arial 1 "),
            bg="#545454",
        ).place(x=309, y=y_texto + 17)

        Label(
            self,
            text=texto.upper(),
            height=1,
            anchor=NW,
            font=("Verdana 12"),
            bg=frame_bg,
            fg="#83a9e6",
        ).place(x=306, y=y_texto)

        Label(
            self,
            text="R$ {:,.2f}".format(valor),
            height=1,
            anchor=NW,
            font=("arial 17 "),
            bg=frame_bg,
            fg="#545454",
        ).place(x=306, y=y_valor)

    def criar_grafico_pizza(self):
        fig = plt.figure(figsize=(4.9, 3), dpi=90, facecolor=frame_bg)
        plt.subplots_adjust(left=0)
        ax = fig.add_subplot(111, facecolor=frame_bg)
        lista_categorias, lista_valores = self.model.pie_chart()
        explode = [0.05 for _ in lista_categorias]
        ax.pie(
            lista_valores,
            shadow=True,
            wedgeprops=dict(width=0.2),
            autopct="%1.1f%%",
            startangle=90,
            explode=explode,
            colors=colors,
        )
        ax.legend(
            lista_categorias,
            loc="center right",
            bbox_to_anchor=(1.55, 0.50),
            fontsize=8,
        )

        canva = FigureCanvasTkAgg(fig, master=self)
        canva.get_tk_widget().place(x=600, y=0)


class Frame3(Frame):
    def __init__(self, controle_financeiro_view):
        self.controle_financeiro_view = controle_financeiro_view
        self.frame3 = Frame(
            controle_financeiro_view.root,
            width=1350,
            height=360,
            bg=frame_bg,
            relief="flat",
            bd=4,
        )
        self.frame2 = Frame2(controle_financeiro_view)
        self.frame3.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.42)
        self.model = controle_financeiro_view.model

        self.frame3.columnconfigure([0, 1, 2, 3], weight=1)
        self.frame3.rowconfigure(0, weight=1)

        self.create_subframes()
        self.create_treeview()
        self.create_despesas_frame()
        self.create_receitas_frame()
        self.create_inserir_categoria_frame()

    def update_comboboxes(self):
        categorias = self.model.listar_categorias()
        descricoes = self.model.listar_descricoes()

        if hasattr(self, "combo_categoria_despesa"):
            self.combo_categoria_despesa["values"] = [
                item[1] for item in categorias]
        if hasattr(self, "combo_descricao_despesa"):
            self.combo_descricao_despesa["values"] = [
                item[1] for item in descricoes]
        if hasattr(self, "combo_categoria_receitas"):
            self.combo_categoria_receitas["values"] = [
                item[1] for item in categorias]
        if hasattr(self, "combo_descricao"):
            self.combo_descricao["values"] = [item[1] for item in descricoes]

    def create_subframes(self):
        self.frames = {}
        frame_names = ["tabela", "despesas", "receitas", "inserir_categoria"]
        for idx, name in enumerate(frame_names):
            frame = Frame(self.frame3, width=220, height=280, bg=frame_bg)
            frame.grid(row=0, column=idx, sticky="nsew", padx=5, pady=5)
            self.frames[name] = frame

    def create_treeview(self):
        tabela_head = ["Id", "Cat", "Desc", "Data", "Valor"]
        self.tree = ttk.Treeview(
            self.frames["tabela"],
            columns=tabela_head,
            show="headings",
            selectmode="extended",
        )
        vsb = ttk.Scrollbar(
            self.frames["tabela"], orient="vertical", command=self.tree.yview
        )
        hsb = ttk.Scrollbar(
            self.frames["tabela"], orient="horizontal", command=self.tree.xview
        )

        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")
        hsb.grid(column=0, row=1, sticky="ew")

        for col in tabela_head:
            self.tree.heading(col, text=col.title(), anchor="center")
            self.tree.column(col, anchor="center")

        self.frames["tabela"].grid_rowconfigure(0, weight=1)
        self.frames["tabela"].grid_columnconfigure(0, weight=1)

        self.update_treeview()

    def create_despesas_frame(self):
        frame = self.frames["despesas"]
        labels = ["Despesas", "Categoria", "Descrição", "Data", "Valor"]
        y_positions = [5, 30, 75, 120, 165]

        for label, y in zip(labels, y_positions):
            Label(
                frame, text=label, font=("Arial", 10),
                bg=frame.cget("bg"), fg=fonte
            ).place(x=5, y=y)

        self.combo_categoria_despesa = self.create_combobox(
            frame, self.model.listar_categorias(), 50
        )
        self.combo_descricao_despesa = self.create_combobox(
            frame, self.model.listar_descricoes(), 95
        )
        self.entry_data_despesa = self.create_date_entry(frame, 140)
        self.entry_valor_despesas = ttk.Entry(frame, width=12)
        self.entry_valor_despesas.place(x=5, y=185)

        self.add_button_despesa = self.create_button(
            frame, "add.png", self.add_despesa, 220, 5
        )
        self.delete_button_despesa = self.create_button(
            frame, "delete.png", self.delete_despesa, 220, 40
        )

    def create_receitas_frame(self):
        frame = self.frames["receitas"]
        labels = ["Receitas", "Categoria", "Descrição", "Data", "Valor"]
        y_positions = [5, 30, 75, 120, 165]

        for label, y in zip(labels, y_positions):
            Label(
                frame, text=label, font=("Arial", 10),
                bg=frame.cget("bg"), fg=fonte
            ).place(x=5, y=y)

        self.combo_categoria_receitas = self.create_combobox(
            frame, self.model.listar_categorias(), 50
        )
        self.combo_descricao = self.create_combobox(
            frame, self.model.listar_descricoes(), 95
        )
        self.entry_data_receitas = self.create_date_entry(frame, 140)
        self.entry_valor_receitas = ttk.Entry(frame, width=12)
        self.entry_valor_receitas.place(x=5, y=185)

        self.add_button_receitas = self.create_button(
            frame, "add.png", self.add_receita, 220, 5
        )
        self.delete_button_receitas = self.create_button(
            frame, "delete.png", self.delete_receita, 220, 40
        )

    def create_inserir_categoria_frame(self):
        frame = self.frames["inserir_categoria"]
        Label(
            frame,
            text="Inserir Categoria",
            font=("Arial", 10),
            bg=frame.cget("bg"),
            fg=fonte,
        ).place(x=5, y=5)
        self.entry_categoria = ttk.Entry(frame, width=15)
        self.entry_categoria.place(x=5, y=30)

        Label(
            frame,
            text="Inserir Descrição",
            font=("Arial", 10),
            bg=frame.cget("bg"),
            fg=fonte,
        ).place(x=5, y=80)
        self.entry_descricao = ttk.Entry(frame, width=15)
        self.entry_descricao.place(x=5, y=110)

        self.add_button_categoria = self.create_button(
            frame, "add.png", self.add_categoria, 55, 5
        )
        self.delete_button_categoria = self.create_button(
            frame, "delete.png", self.delete_categoria, 55, 40
        )
        self.add_button_descricao = self.create_button(
            frame, "add.png", self.add_descricao, 135, 5
        )
        self.delete_button_descricao = self.create_button(
            frame, "delete.png", self.delete_descricao, 135, 40
        )

    def create_combobox(self, frame, items, y):
        values = [item[1] for item in items]
        combobox = ttk.Combobox(frame, values=values, width=10)
        combobox.place(x=5, y=y)
        self.update_comboboxes()
        return combobox

    def create_date_entry(self, frame, y):
        entry = DateEntry(
            frame, width=10, background="darkblue", foreground=fonte, year=2023
        )
        entry.place(x=5, y=y)
        return entry

    def create_button(self, frame, image_file, command, y, x):
        image = self.load_image(image_file)
        button = Button(
            frame, image=image, command=command,
            relief=tk.FLAT, bg=frame.cget("bg")
        )
        button.image = image
        button.place(x=x, y=y)
        return button

    def add_despesa(self):
        despesa = (
            self.combo_categoria_despesa.get(),
            self.combo_descricao_despesa.get(),
            self.entry_data_despesa.get(),
            self.entry_valor_despesas.get(),
        )
        self.model.inserir_despesa(despesa)
        self.update_treeview()
        self.update_comboboxes()
        self.update_charts()

    def delete_despesa(self):
        self.delete_item("Despesas")
        self.update_comboboxes()
        self.update_charts()

    def add_receita(self):
        receita = (
            self.combo_categoria_receitas.get(),
            self.combo_descricao.get(),
            self.entry_data_receitas.get(),
            self.entry_valor_receitas.get(),
        )
        self.model.inserir_receita(receita)
        self.update_treeview()
        self.update_comboboxes()
        self.update_charts()

    def delete_receita(self):
        self.delete_item("Receitas")
        self.update_comboboxes()
        self.update_charts()

    def add_categoria(self):
        categoria = self.entry_categoria.get()
        self.model.inserir_categoria(categoria)
        self.update_treeview()
        self.entry_categoria.delete(0, "end")
        self.update_comboboxes()
        self.update_charts()

    def delete_categoria(self):
        self.delete_item("Categorias")
        self.update_comboboxes()
        self.update_charts()

    def add_descricao(self):
        descricao = self.entry_descricao.get()
        self.model.inserir_descricao(descricao)
        self.update_treeview()
        self.entry_descricao.delete(0, "end")
        self.update_comboboxes()
        self.update_charts()

    def delete_descricao(self):
        self.delete_item("Descrições")
        self.update_comboboxes()
        self.update_charts()

    def delete_item(self, table):
        selected_item = self.tree.selection()
        if selected_item:
            item_id = self.tree.item(selected_item, "values")[0]
            self.model.delete_item(table, item_id)
            self.tree.delete(selected_item)
            self.update_treeview()
            self.update_comboboxes()

    def load_image(self, image_file):
        base_dir = os.path.dirname(__file__)
        img_path = os.path.join(base_dir, image_file)
        img = Image.open(img_path).resize((17, 17))
        return ImageTk.PhotoImage(img)

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        despesas = self.model.listar_despesas()
        receitas = self.model.listar_receitas()
        lista_itens = despesas + receitas

        for item in lista_itens:
            self.tree.insert("", "end", values=item)

    def update_charts(self):
        self.frame2.atualizar_frame()
