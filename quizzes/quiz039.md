## code
```.py
import sqlite3

haiku = """Code flows like a stream 
Algorithms guide its way 
In silence, it solves"""

database = "quiz39.db"
con = sqlite3.connect(database)
cursor = con.cursor()

cursor.execute("""
create table if not exists words (
    word text,
    length integer
)
""")
con.commit()

for i in haiku.split():
    aye = f"insert into words(word, length) values ('{i}', {len(i)})"
    cursor.execute(aye)
    con.commit()

cursor.execute("select AVG(length) FROM Words")
output = cursor.fetchone()[0]

print(f"average word length is {output:.2f}")
```
