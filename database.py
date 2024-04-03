import sqlite3

#all comands for the database

class Table():
    def __init__(self, database_path: str) -> None:
        self.name_db = database_path
        self.con = sqlite3.connect(str(self.name_db))
        self.cur = self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        self.table_name = self.cur.fetchall()[0][0]
        self.cur.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        trad VARCHAR(100),
                        present VARCHAR(100),
                        preterit VARCHAR(100), 
                        participe_passe VARCHAR(100),
                        is_found INTEGER DEFAULT(0))""")
        self.con.commit()


    def cut(self) -> None:  # cut the connexion with database
        self.con.close()

    def reset(self) -> None:  # set is_found at 0
        self.cur.execute(
            f"SELECT id, trad, present, preterit, participe_passe FROM {self.table_name} WHERE is_found == 1"
        )
        for (row) in self.cur.fetchall():
            self.cur.execute(
                f"UPDATE {self.table_name} SET is_found = 0 WHERE id = ?", (row[0],)
            )
            self.con.commit()

    
    def select_isfound(self, is_found_value: int) -> list:  
        self.cur.execute(
            f"SELECT id, trad, present, preterit, participe_passe FROM {self.table_name} WHERE is_found == {is_found_value}"
        )
        return self.cur.fetchall()
    
    def add_vocabulary_four_fields(self, vocabulary: list[str, str, str, str]):
        self.cur.execute(
            f"INSERT INTO {self.table_name} (trad, present, preterit, participe_passe) VALUES( ?, ?, ?, ?)", vocabulary,)
        self.con.commit()
    
    def select_columns(self) -> list:
        self.cur.execute(f"PRAGMA table_info({self.table_name})")
        return self.cur.fetchall()


if __name__ == '__main__':
    a = Table('./vocabulary/english/verbesirr.db')
    b = [i[1] for i in a.select_columns()[1:-1]]
    print(b)
    