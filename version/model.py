import sqlite3 as lite
import pandas as pd
from tkinter import messagebox


class ControleFinanceiroModel:
    def __init__(self):
        self.conn = lite.connect("tabela.db")
        self.cur = self.conn.cursor()

    def inserir_categoria(self, categoria):
        if categoria:
            try:
                with self.conn:
                    query = "INSERT INTO Categoria(nome) VALUES (?)"
                    self.cur.execute(query, (categoria,))
                    self.conn.commit()
                    messagebox.showinfo(f"Categoria inserida: {categoria}")
            except Exception as e:
                messagebox.showerror("Erro ao inserir categoria", str(e))
        else:
            messagebox.showerror("Erro", "Categoria vazia fornecida")

    def inserir_descricao(self, descricao):
        if descricao:
            try:
                with self.conn:
                    query = "INSERT INTO Descricoes(descricao) VALUES (?)"
                    self.cur.execute(query, (descricao,))
                    self.conn.commit()
                    messagebox.showinfo(f"Descrição inserida: {descricao}")
            except Exception as e:
                messagebox.showerror("Erro ao inserir descrição", str(e))
        else:
            messagebox.showerror("Erro", "Descrição vazia fornecida")

    def inserir_receita(self, receita):
        try:
            with self.conn:
                query = """INSERT INTO Receitas(
                           categoria, descricao, adicionado_em, valor)
                           VALUES (?, ?, ?, ?)"""
                self.cur.execute(query, receita)
                self.conn.commit()
                messagebox.showinfo(f"Receita inserida: {receita}")
        except Exception as e:
            messagebox.showerror("Erro ao inserir receita", str(e))

    def inserir_despesa(self, despesa):
        try:
            with self.conn:
                query = """INSERT INTO Despesas(
                           categoria, descricao, adicionado_em, valor)
                           VALUES (?, ?, ?, ?)"""
                self.cur.execute(query, despesa)
                self.conn.commit()
                messagebox.showinfo(f"Despesa inserida: {despesa}")
        except Exception as e:
            messagebox.showerror("Erro ao inserir despesa", str(e))
            self.frame2_view.pie_chart()
            self.frame2_view.bar_graph()
            self.frame2_view.line_chart()

    def delete_item(self, table, item_id):
        try:
            with self.conn:
                query = f"DELETE FROM {table} WHERE id = ?"
                self.cur.execute(query, (item_id,))
                self.conn.commit()
                messagebox.showinfo(f"Item deletado: {item_id}")
        except Exception as e:
            messagebox.showerror("Erro ao deletar item", str(e))
        self.pie_chart()
        self.bar_graph()
        self.line_chart()

    def listar_itens(self, table):
        try:
            with self.conn:
                query = f"SELECT * FROM {table}"
                self.cur.execute(query)
                return self.cur.fetchall()
        except Exception as e:
            messagebox.showerror(f"Erro ao listar {table}", str(e))
            return []

    def listar_receitas(self):
        return self.listar_itens("Receitas")

    def listar_despesas(self):
        return self.listar_itens("Despesas")

    def listar_categorias(self):
        return self.listar_itens("Categoria")

    def listar_descricoes(self):
        return self.listar_itens("Descricoes")

    def line_chart(self):
        receitas = self.listar_receitas()
        total_revenue = sum(
            [float(row[4]) for row in receitas if self.is_valid_number(row[4])]
        )

        despesas = self.listar_despesas()
        total_expense = sum(
            [float(row[4]) for row in despesas if self.is_valid_number(row[4])]
        )

        if total_revenue == 0:
            percentual = 0
        else:
            percentual = (
                (total_revenue - total_expense) / total_revenue) * 100

        return percentual

    def bar_graph(self):
        receitas = self.listar_receitas()
        despesas = self.listar_despesas()

        total_revenue = sum(
            [float(row[4]) for row in receitas if self.is_valid_number(row[4])]
        )
        total_expense = sum(
            [float(row[4]) for row in despesas if self.is_valid_number(row[4])]
        )

        balance = total_revenue - total_expense

        return [total_revenue, total_expense, balance]

    def pie_chart(self):
        lista_despesas = self.listar_despesas()
        df = pd.DataFrame(
            lista_despesas,
            columns=["id", "categoria", "descricao", "adicionado_em", "valor"],
        )
        df = df.groupby("categoria")["valor"].sum()

        category_list = df.index.tolist()
        value_list = df.values.tolist()

        return [category_list, value_list]

    def is_valid_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
