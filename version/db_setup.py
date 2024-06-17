import sqlite3 as lite


def create_db():
    con = lite.connect("tabela.db")
    with con:
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Categoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Receitas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT,
        descricao TEXT,
        adicionado_em DATE,
        valor REAL
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Despesas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT,
        descricao TEXT,
        adicionado_em DATE,
        valor REAL
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Descricoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT
        )
        """)
        con.commit()


if __name__ == "__main__":
    create_db()
