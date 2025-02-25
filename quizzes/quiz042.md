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
        print(f'\33[1;32mTx(id={id})Signature matches\033[00m')
    else:
        print(f'\33[1;31mTx(id={id})Error signature\033[00m')
```

## Proof of Work
![image](https://github.com/user-attachments/assets/289421cd-a8a2-4b70-8781-eec43f5c0b60)


## Diagram


