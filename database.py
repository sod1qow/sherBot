import sqlite3 as sql


async def sql_connector():
    con = sql.connect('sher.db')
    cur = con.cursor()
    return con, cur


async def create_tables():
    con, cur = await sql_connector()

    cur.execute("""CREATE TABLE IF NOT EXISTS sher(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matn TEXT
    )""")


async def get_sher():
    con, cur = await sql_connector()

    data = cur.execute("SELECT * FROM sher").fetchall()
    return data