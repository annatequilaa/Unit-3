# Quiz039 2025/01

## Paper solution
None because this was done directly on computer.

## Code
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

## Proof of work
![image](https://github.com/user-attachments/assets/f5b72dae-d349-4618-be1f-3415070d5ef1)


## Diagrams
ER Diagram


![image](https://github.com/user-attachments/assets/3887e9ed-379a-44ec-821f-7b1ed5b52a57)




Figure taken from '[2024] Quizzes' Google Slides presentation


