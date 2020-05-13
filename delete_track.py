import sqlite3

db = "corrupt.sqlite"
conn = sqlite3.connect(db)
c = conn.cursor()


def delete_track(title):
    c.execute("DELETE FROM Track WHERE Name=:title", {"title" : title})
    return c.fetchone();

print(delete_track("Blame It on the Rain"))

conn.commit()
conn.close()
