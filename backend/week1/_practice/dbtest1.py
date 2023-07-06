import sqlite3
import os


def abs_path(relative_pos):
    return os.path.join(os.path.dirname(__file__), relative_pos)


conn = sqlite3.connect(abs_path("test.db"))

cur = conn.cursor()
# cur.execute("create table movie(title, year, score)")
# cur.execute("create table some_list(item)")
# conn.commit()
res = cur.execute("select * from sqlite_master where type = 'table'")

print(res.fetchall())
