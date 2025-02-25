# Quiz042 2025/01

## Paper solution
![image](https://github.com/user-attachments/assets/38e5815f-8ada-43bc-800b-31660a037bfc)

## Code
```.py
from quiz040_secure_password import check_password
from mylib import DatabaseManager

x = DatabaseManager("bitcoin_exchange.db")
result = x.search("SELECT * from ledger")
x.close()

for row in result:
    id, send_id, rece_id, amount, signature = row
    string_hash = f"id {id},sender_id {send_id},receiver_id {rece_id},amount {amount}"
    if check_password(hashed_password = signature, user_password = string_hash):
        print("TX IS CORRECT")

    else:
        print("TX is bad")
```

## Proof of Work
![image](https://github.com/user-attachments/assets/d47749f5-3c1d-4542-b2eb-e93e1f505dd0)


## Diagram


