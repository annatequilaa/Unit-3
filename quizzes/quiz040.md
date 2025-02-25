# Quiz032 2025/01

## Paper solution
database so none

## Code
```.sql
select * from (select sum(case when T.transaction_type = 'deposit' then T.amount else 0 end)  as sum_deposit,
                      sum(case when T.transaction_type = 'withdraw' then T.amount else 0 end) as sum_withdraw,
                      sum(case when T.transaction_type = 'deposit' then T.amount else 0 end) -
                      sum(case when T.transaction_type = 'withdraw' then T.amount else 0 end) as true_balance,
                      A.balance, T.account_id
               from transactions T join accounts A on T.account_id = A.account_id
               group by t.account_id) where true_balance != balance;

select * from customers where customer_id = 12

```

## Proof of Work
![image](https://github.com/user-attachments/assets/dca6990c-9087-4564-bacf-1a4194543eaf)
![image](https://github.com/user-attachments/assets/6a5dee7e-6a7d-4ee4-9e9c-4585648ed15a)


## Diagram
![image](https://github.com/user-attachments/assets/fc308dec-c6b8-4d96-ad14-ea325f84f358)

