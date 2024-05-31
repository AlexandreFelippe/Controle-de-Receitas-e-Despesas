# import tkinter as tk
from tkinter import (
    ttk, Frame, Label, LEFT, RAISED, NSEW, NW, RIDGE, Entry, Button)
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class FinanceApp:
    def __init__(self, master):
        self.master = master
        self.colors = [
            "#5588bb", "#66bbbb", "#99bb55", "#ee9944", "#444466", "#bb5555"]
        self.setup_styles()
        self.create_frames()
        self.create_widgets()

    def setup_styles(self):
        self.master.configure(bg="#e9edf5")
        style = ttk.Style(self.master)
        style.theme_use("clam")

    def create_frames(self):
        self.frame1 = Frame(
            self.master, width=1043, height=50, bg="#FFFFFF", relief="flat"
        )
        self.frame1.grid(row=0, column=0)

        self.frame2 = Frame(
            self.master,
            width=1043,
            height=361,
            bg="#FFFFFF",
            pady=20,
            relief="raised"
        )
        self.frame2.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        self.frame3 = Frame(
            self.master, width=1043, height=300, bg="#FFFFFF", relief="flat"
        )
        self.frame3.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

    def create_widgets(self):
        # Frame 1
        img = Image.open("cofrinho.jpg").resize((45, 45))
        self.img_logo = ImageTk.PhotoImage(img)
        Label(
            self.frame1,
            image=self.img_logo,
            text=" Olá, seja bem-vindo(a) ao seu controle financeiro",
            font=("Arial", 16),
            width=1050,
            compound=LEFT,
            padx=5,
            relief=RAISED,
            anchor=NW,
            bg="#FFFFFF",
        ).place(x=0, y=0)

        # Frame 2
        self.create_percentual_gastos()
        self.create_grafico()
        self.create_resumo()

        # Frame 3
        self.frame_renda = Frame(
            self.frame3, width=300, height=250, bg="#FFFFFF")
        self.frame_renda.grid(row=0, column=0)

        self.frame_operacoes = Frame(
            self.frame3, width=220, height=250, bg="#FFFFFF")
        self.frame_operacoes.grid(row=0, column=1, padx=5)

        self.frame_configuracao = Frame(
            self.frame3, width=220, height=250, bg="#FFFFFF"
        )
        self.frame_configuracao.grid(row=0, column=2, padx=5)

        self.create_operacoes()
        self.create_configuracoes()
        self.create_grafico_pie()

    def create_percentual_gastos(self):
        Label(
            self.frame2,
            text="Percentual da Receita Gasta",
            font=("Arial", 12),
            height=1,
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=7, y=5)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("black.Horizontal.TProgressbar", background="#daed6b")
        style.configure("TProgressbar", thickness=25)

        label_progressbar = ttk.Progressbar(
            self.frame2, length=180, style="black.Horizontal.TProgressbar"
        )
        label_progressbar.place(x=10, y=35)
        label_progressbar["value"] = 50

        Label(
            self.frame2,
            text="{:.2f}%".format(50),
            font=("Arial", 16),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=200, y=35)

    def create_grafico(self):
        lista_categorias = ["Renda", "Despesas", "Saldo"]
        lista_valores = [1000, 600, 400]

        fig = plt.figure(figsize=(4, 3.45), dpi=60)
        ax = fig.add_subplot(111)
        ax.bar(lista_categorias, lista_valores, color=self.colors, width=0.9)

        for i, value in enumerate(lista_valores):
            ax.text(
                i,
                value + 0.5,
                f"{value:.2f}",
                fontsize=17,
                fontstyle="italic",
                verticalalignment="bottom",
                color="dimgrey",
            )

        ax.set_xticks(range(len(lista_categorias)))
        ax.set_xticklabels(lista_categorias, fontsize=16)
        ax.spines["bottom"].set_color("#ffffff")
        ax.spines["left"].set_color("#cccccc")
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(False)
        ax.xaxis.grid(False)

        canva = FigureCanvasTkAgg(fig, master=self.frame2)
        canva.get_tk_widget().place(x=10, y=70)

    def create_resumo(self):
        valores = [345, 225, 534]
        labels = [
            ("Total Renda Mensal", valores[0], 35, 70),
            ("Total Despesas Mensais", valores[1], 115, 150),
            ("Total Saldo da Caixa", valores[2], 190, 220),
        ]
        for text, value, y_text, y_value in labels:
            Label(
                self.frame2,
                text=text.upper(),
                height=1,
                anchor=NW,
                font=("Verdana 12"),
                bg="#FFFFFF",
                fg="#83a9e6",
            ).place(x=306, y=y_text)
            Label(
                self.frame2,
                text=f"R$ {value:,.2f}",
                height=1,
                anchor=NW,
                font=("arial 17 "),
                bg="#FFFFFF",
                fg="#545454",
            ).place(x=306, y=y_value)

    def create_grafico_pie(self):
        figura = plt.Figure(figsize=(5, 3), dpi=90)
        ax = figura.add_subplot(111)
        lista_valores = [345, 225, 534]
        lista_categorias = ["Alimentação", "Aluguel", "Vestuário"]
        explode = [0.05] * len(lista_categorias)

        ax.pie(
            lista_valores,
            explode=explode,
            wedgeprops=dict(width=0.2),
            autopct="%1.1f%%",
            colors=self.colors,
            shadow=True,
            startangle=90,
        )
        ax.legend(
            lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

        canva_categoria = FigureCanvasTkAgg(figura, self.frame2)
        canva_categoria.get_tk_widget().place(x=530, y=20)

    def create_operacoes(self):
        Label(
            self.frame_operacoes,
            text="Insira novas despesas",
            height=1,
            font=("Arial", 10, "bold"),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=10, y=10)

        Label(
            self.frame_operacoes,
            text="Categoria",
            height=1,
            font=("Arial", 10),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=10, y=40)

        self.combo_categoria_despesas = ttk.Combobox(
            self.frame_operacoes, width=10, font=("Arial", 10)
        )
        self.combo_categoria_despesas.place(x=110, y=41)

        Label(
            self.frame_operacoes,
            text="Data",
            height=1,
            font=("Arial", 10),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=10, y=70)

        self.cal_despesas = DateEntry(
            self.frame_operacoes,
            width=12,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            year=2023,
        )
        self.cal_despesas.place(x=110, y=71)

        Label(
            self.frame_operacoes,
            text="Valor",
            height=1,
            font=("Arial", 10),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=10, y=100)

        self.valor_despesas = Entry(
            self.frame_operacoes, width=12, justify="left", relief=RIDGE
        )
        self.valor_despesas.place(x=110, y=101)

        Button(
            self.frame_operacoes,
            command=self.inserir_despesas,
            text="Inserir",
            width=10,
            font=("Arial", 10, "bold"),
            overrelief=RIDGE,
            bg="#3fb5a3",
            fg="#ffffff",
        ).place(x=110, y=130)

    def create_configuracoes(self):
        Label(
            self.frame_configuracao,
            text="Insira novas rendas",
            height=1,
            font=("Arial", 10, "bold"),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=10, y=10)

        Label(
            self.frame_configuracao,
            text="Categoria",
            height=1,
            font=("Arial", 10),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=10, y=40)

        self.combo_categoria_renda = ttk.Combobox(
            self.frame_configuracao, width=10, font=("Arial", 10)
        )
        self.combo_categoria_renda.place(x=110, y=41)

        Label(
            self.frame_configuracao,
            text="Data",
            height=1,
            font=("Arial", 10),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=10, y=70)

        self.cal_renda = DateEntry(
            self.frame_configuracao,
            width=12,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            year=2023,
        )
        self.cal_renda.place(x=110, y=71)

        Label(
            self.frame_configuracao,
            text="Valor",
            height=1,
            font=("Arial", 10),
            anchor=NW,
            bg="#FFFFFF",
            fg="#38576B",
        ).place(x=10, y=100)

        self.valor_renda = Entry(
            self.frame_configuracao, width=12, justify="left", relief=RIDGE
        )
        self.valor_renda.place(x=110, y=101)

        Button(
            self.frame_configuracao,
            command=self.inserir_renda,
            text="Inserir",
            width=10,
            font=("Arial", 10, "bold"),
            overrelief=RIDGE,
            bg="#3fb5a3",
            fg="#ffffff",
        ).place(x=110, y=130)

    def set_controller(self, controller):
        self.controller = controller

    def inserir_despesas(self):
        categoria = self.combo_categoria_despesas.get()
        data = self.cal_despesas.get()
        valor = self.valor_despesas.get()
        self.controller.inserir_despesas(categoria, data, valor)

    def inserir_renda(self):
        categoria = self.combo_categoria_renda.get()
        data = self.cal_renda.get()
        valor = self.valor_renda.get()
        self.controller.inserir_renda(categoria, data, valor)

    def atualizar_graficos(self, dados):
        # # Atualizar o gráfico de barras
        # self.canva.get_tk_widget().destroy()
        # self.create_grafico()

        # # Atualizar o gráfico de pizza
        # self.canva_categoria.get_tk_widget().destroy()
        # self.create_grafico_pie()
        pass
