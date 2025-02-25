# Quiz032 2025/01

## Paper solution


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

