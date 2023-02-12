import sqlite3
from tkinter.messagebox import showerror

#OOP
class LoanDatabase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS loans (id INTEGER PRIMARY KEY, Firstname text, Lastname text, Principal text,  YearTerm text, LTA text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM loans")
        rows = self.cur.fetchall()
        return rows

    def insert(self, Firstname, Lastname, Principal, YearTerm, LTA):
        self.cur.execute("INSERT INTO loans VALUES (NULL, ?, ?, ?, ?, ?)",
                         (Firstname, Lastname, Principal, YearTerm, LTA))
        self.conn.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM loans WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, Firstname, Lastname, Principal, YearTerm, LTA):
        try:
            self.cur.execute("UPDATE loans SET Firstname = ?, Lastname = ?, Principal = ?, YearTerm = ?, LTA =?,  WHERE id = ?",
                            (Firstname, Lastname, Principal, YearTerm, LTA, id))
            
        except sqlite3.OperationalError as e:
            showerror ("", "Oh no")
        
        finally:
            self.conn.commit()
    
    def __del__(self):
        self.conn.close()