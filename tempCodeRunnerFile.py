import sqlite3 as lite


con = lite.connect("tabela.db")
# Drop table if it exists
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Categoria")
    cur.execute("DROP TABLE IF EXISTS Receitas")
    cur.execute("DROP TABLE IF EXISTS Despesas")
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY, nome TEXT)")
    cur.execute(
        "CREATE TABLE Receitas(id INTEGER PRIMARY KEY, categoria TEXT, adicionado_em DATE, valor REAL)" # noqa
    )
    cur.execute(
        "CREATE TABLE Despesas(id INTEGER PRIMARY KEY, categoria TEXT, adicionado_em DATE, valor REAL)" # noqa
    )
