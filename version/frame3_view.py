import tkinter as tk
from tkinter import ttk
from tkinter import Frame, Label, Button
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from model import ControleFinanceiroModel
import os

fundo_tela = "#1e3743"
frame_bg = "#dfe3ee"
fonte = "#38576B"
colors = ["#5588bb", "#66bbbb", "#99bb55", "#ee9944", "#444466", "#bb5555"]


class Frame3:
    def __init__(self, controle_financeiro_view):
        self.root = controle_financeiro_view.root
        self.frame3 = tk.Frame(self.root)
        self.frame3.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.42)
        self.model = ControleFinanceiroModel()

        self.frame3.columnconfigure([0, 1, 2, 3], weight=1)
        self.frame3.rowconfigure(0, weight=1)

        self.create_subframes()
        self.create_treeview()

    def create_subframes(self):
        self.frames = {}
        frame_names = ["tabela", "despesas", "receitas", "inserir_categoria"]
        frame_bg = fundo_tela
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
                bg=frame.cget("bg"), fg="fonte"
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
                bg=frame.cget("bg"), fg="fonte"
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
            fg="fonte",
        ).place(x=5, y=5)
        self.entry_categoria = ttk.Entry(frame, width=15)
        self.entry_categoria.place(x=5, y=30)

        Label(
            frame,
            text="Inserir Descrição",
            font=("Arial", 10),
            bg=frame.cget("bg"),
            fg="fonte",
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
        return combobox

    def create_date_entry(self, frame, y):
        entry = DateEntry(
            frame, width=10, background="darkblue",
            foreground="fonte", year=2023
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

    def delete_despesa(self):
        self.delete_item("Despesas")

    def add_receita(self):
        receita = (
            self.combo_categoria_receitas.get(),
            self.combo_descricao.get(),
            self.entry_data_receitas.get(),
            self.entry_valor_receitas.get(),
        )
        self.model.inserir_receita(receita)
        self.update_treeview()

    def delete_receita(self):
        self.delete_item("Receitas")

    def add_categoria(self):
        categoria = self.entry_categoria.get()
        self.model.inserir_categoria(categoria)
        self.update_treeview()
        self.entry_categoria.delete(0, "end")

    def delete_categoria(self):
        self.delete_item("Categorias")

    def add_descricao(self):
        descricao = self.entry_descricao.get()
        self.model.inserir_descricao(descricao)
        self.update_treeview()
        self.entry_descricao.delete(0, "end")

    def delete_descricao(self):
        self.delete_item("Descrições")

    def delete_item(self, table):
        selected_item = self.tree.selection()
        if selected_item:
            item_id = self.tree.item(selected_item, "values")[0]
            self.model.delete_item(table, item_id)
            self.tree.delete(selected_item)
            self.update_treeview()

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
