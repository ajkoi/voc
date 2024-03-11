import sqlite3

#all comands for the database

class Table():
    def __init__(self, table_name, database_path) -> None:
        # Lancer la boucle principale de l'application
        self.name_db = database_path
        self.table_name = table_name
        self.con = sqlite3.connect(str(self.name_db))
        self.cur = self.con.cursor()
        self.cur.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
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

    
    def select_isfound(self, is_found_value) -> list:  
        self.cur.execute(
            f"SELECT id, trad, present, preterit, participe_passe FROM {self.table_name} WHERE is_found == {is_found_value}"
        )
        return self.cur.fetchall()
    
    def add_vocabulary(self, vocabulary):
        self.cur.execute(
            f"INSERT INTO {self.table_name} (trad, present, preterit, participe_passe) VALUES({vocabulary[0]},{vocabulary[0]}, {vocabulary[0]}, {vocabulary[0]})",  vocabulary)
        self.con.commit()