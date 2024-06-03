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
        query = "DELETE FROM Categoria WHERE id = ?"
        cur.execute(query, i)


def inserir_descricao(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Descricoes(descricao) VALUES (?)" # noqa
        cur.execute(query, i)


def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas(categoria, descricao, adicionado_em, valor) VALUES (?, ?, ?, ?)" # noqa
        cur.execute(query, i)


def inserir_despesa(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Despesas(categoria, descricao, adicionado_em, valor) VALUES (?, ?, ?, ?)" # noqa
        cur.execute(query, i)


def excluir_item(tabela, i):
    try:
        with con:
            cur = con.cursor()
            query = f"DELETE FROM {tabela} WHERE id = ?"
            cur.execute(query, (i,))
    except lite.Error as e:
        print(f"Erro ao excluir item: {e}")


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
        cur.execute(
            "SELECT * FROM Receitas") # noqa
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


def listar_descrição():
    lista_descrição = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Descricoes")
        rows = cur.fetchall()
        for row in rows:
            lista_descrição.append(row)
        return lista_descrição


def bar_graph():
    receitas = listar_receitas()
    despesas = listar_despesas()

    list_revenue = [
        float(row[4]) for row in receitas if is_valid_number(row[4])]
    list_expense = [
        float(row[4]) for row in despesas if is_valid_number(row[4])]

    total_revenue = sum(list_revenue)
    total_expense = sum(list_expense)

    balance = total_revenue - total_expense

    return [total_revenue, total_expense, balance]


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def pie_chart():
    despesas = listar_despesas()
    list_expense = []
    for i in despesas:
        list_expense.append(i)

    df = pd.DataFrame(list_expense, columns=[
        'id', 'categoria', 'descrição', 'adicionado_em', 'valor'])
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
        list_revenue.append(i[4])

    total_revenue = sum(list_revenue)

    despesas = listar_despesas()
    list_expense = []
    for i in despesas:
        list_expense.append(i[4])

    total_expense = sum(list_expense)

    if total_revenue == 0:
        percentage = 0
    else:
        percentage = ((total_revenue - total_expense) / total_revenue) * 100

    return percentage
