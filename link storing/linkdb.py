import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS link_record (link_name text, link_url text)")
        self.conn.commit()

    def fetchRecord(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insertRecord(self, link_name, link_url):
        self.cur.execute("INSERT INTO link_record VALUES (?, ?)",
                         (link_name, link_url))
        self.conn.commit()

    def removeRecord(self, rwid):
        self.cur.execute("DELETE FROM link_record WHERE rowid=?", (rwid,))
        self.conn.commit()

    def updateRecord(self, link_name, link_url, rid):
        self.cur.execute("UPDATE link_record SET link_name = ?, link_url = ? WHERE rowid = ?",
                         (link_name, link_url, rid))
        self.conn.commit()

    def __del__(self):
        self.conn.close()