import sqlite3 as lite


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
