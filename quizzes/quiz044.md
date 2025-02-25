# Quiz044 2025/01

## Paper solution
Wasn't in class that day hence no paper solution

## Code
```.py
class rainDrops():
    def pour(n:int) -> str:
        output = ""
        div = False
        if n % 3 == 0:
            output += "Pling"
            div = True
        if n % 5 == 0:
            output += "Plang"
            div = True
        if n % 7 == 0:
            output += "Plong"
            div = True
        if div == False:
            output = str(n)
        return output
```

## Proof of Work
![image](https://github.com/user-attachments/assets/ee83e563-d526-4697-b34e-afdc6a2af8b5)


## Diagram
![image](https://github.com/user-attachments/assets/45c79cc3-c582-4d26-87c7-3c0b6d8ce4b8)


