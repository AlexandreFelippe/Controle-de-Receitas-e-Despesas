import sqlite3 as lite
import pandas as pd


con = lite.connect("tabela.db")


def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria(nome) VALUES (?)"
        cur.execute(query, i)


def excluir_categoria(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Categoria WHERE nome = ?"
        cur.execute(query, i)


def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas(categoria, adicionado_em, valor) VALUES (?, ?, ?)" # noqa
        cur.execute(query, i)


def excluir_receita(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id = ?"
        cur.execute(query, i)


def inserir_despesa(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Despesas(categoria, adicionado_em, valor) VALUES (?, ?, ?)" # noqa
        cur.execute(query, i)


def excluir_despesa(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Despesas WHERE id = ?"
        cur.execute(query, i)


def listar_categorias():
    lista_categorias = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        rows = cur.fetchall()
        for row in rows:
            lista_categorias.append(row)
        return lista_categorias


def listar_receitas():
    lista_receitas = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        rows = cur.fetchall()
        for row in rows:
            lista_receitas.append(row)
        return lista_receitas


def listar_despesas():
    lista_despesas = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Despesas")
        rows = cur.fetchall()
        for row in rows:
            lista_despesas.append(row)
        return lista_despesas


def bar_graph():
    receitas = listar_receitas()
    list_revenue = []
    for i in receitas:
        list_revenue.append(i[3])
    total_revenue = sum(list_revenue)

    despesas = listar_despesas()
    list_expense = []
    for i in despesas:
        list_expense.append(i[3])
    total_expense = sum(list_expense)

    balance = total_revenue - total_expense

    return [total_revenue, total_expense, balance]


def pie_chart():
    despesas = listar_despesas()
    list_expense = []
    for i in despesas:
        list_expense.append(i)

    df = pd.DataFrame(list_expense, columns=[
        'id', 'categoria', 'adicionado_em', 'valor'])
    df = df.groupby('categoria')['valor'].sum()

    value_list = df.values.tolist()
    category_list = []

    for i in df.index:
        category_list.append(i)
    return [category_list, value_list]


def line_chart():
    receitas = listar_receitas()
    list_revenue = []
    for i in receitas:
        list_revenue.append(i[3])

    total_revenue = sum(list_revenue)

    despesas = listar_despesas()
    list_expense = []
    for i in despesas:
        list_expense.append(i[3])

    total_expense = sum(list_expense)

    if total_revenue == 0:
        percentage = 0
    else:
        percentage = ((total_revenue - total_expense) / total_revenue) * 100

    return percentage
