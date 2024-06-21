import sqlite3 as lite


def create_db():
    conn = lite.connect("tabela.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Categoria(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Receitas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT,
    descricao TEXT,
    adicionado_em DATE,
    valor REAL NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Despesas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT,
    descricao TEXT,
    adicionado_em DATE,
    valor REAL NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Descricoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()
