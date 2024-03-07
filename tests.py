import sqlite3
# from random import shuffle
con = sqlite3.connect("test1.db")
cur = con.cursor()

# # # # # cur.execute("""UPDATE vbirreguliers SET preterit = 'was/were', participe_passe = 'been' WHERE id = 4""")
# # # # # cur.execute("""INSERT INTO vbirreguliers (trad, present, preterit, participe_passe) VALUES( 'gronder', 'chide','chid' ,'chid' )""")
# # # # con.commit()
# # # # print("t")
for row in cur.execute("SELECT id, trad, present, preterit, participe_passe, is_found FROM test2"):
    print(row, '\n')
con.close()
