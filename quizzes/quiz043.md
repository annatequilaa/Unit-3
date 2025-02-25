![image](https://github.com/user-attachments/assets/6b480876-fc94-44a6-a7e3-9dab0151faec)# Quiz043 2025/01

## Paper solution
![image](https://github.com/user-attachments/assets/1d15b61c-5106-454b-b791-70211cc0c8c2)


## Code
```.py
class palNum:
    def __init__(self, A: int, B: int):
        self.A = A
        self.B = B

    def get_pal_list(self):
        output = []
        for i in range(self.A, self.B+1):
            if str(i)[::-1] == str(i):
                output.append(i)
        return output
```

## Proof of Work
![image](https://github.com/user-attachments/assets/5c50d50a-6438-4e47-b9b5-554efb7f7df0)

## Diagram
![image](https://github.com/user-attachments/assets/6c065baf-0f73-497d-bc46-16dbd45c9481)


