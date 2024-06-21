from tkinter import Label, NW
from tkinter.ttk import Progressbar
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame

frame = "#dfe3ee"
fonte = "#38576B"
colors = ["#5588bb", "#66bbbb", "#99bb55", "#ee9944", "#444466", "#bb5555"]


class Frame2(Frame):
    def __init__(self, controle_financeiro_view):
        super().__init__(controle_financeiro_view.root)
        self.root = controle_financeiro_view.root
        self.model = controle_financeiro_view.model
        self.criar_componentes()

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
            bg=frame,
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
            bg=frame,
            fg=fonte,
        )
        self.label_percentual_texto.place(x=200, y=30)

    def criar_grafico_barras(self):
        lista_categorias = ["Renda", "Despesas", "Saldo"]
        lista_valores = self.model.bar_graph()

        fig = plt.figure(figsize=(4, 3.45), dpi=60, facecolor=frame)
        ax = fig.add_subplot(111, facecolor=frame)
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
            bg=frame,
            fg="#83a9e6",
        ).place(x=306, y=y_texto)

        Label(
            self,
            text="R$ {:,.2f}".format(valor),
            height=1,
            anchor=NW,
            font=("arial 17 "),
            bg=frame,
            fg="#545454",
        ).place(x=306, y=y_valor)

    def criar_grafico_pizza(self):
        fig = plt.figure(figsize=(4.9, 3), dpi=90, facecolor=frame)
        plt.subplots_adjust(left=0)
        ax = fig.add_subplot(111, facecolor=frame)
        lista_categorias, lista_valores = (
            self.model.pie_chart())
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
