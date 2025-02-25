# Quiz032 2025/01

## Paper solution
![image](https://github.com/user-attachments/assets/7ffbba4d-209c-4e26-95ab-26c565e05f8c)



## Code
```.py
class quiz045():
    def __init__(self, text: str):
        self.text = text

    def wordCounter(self):
        output = {}
        lst = self.text.split(".")
        words = []
        for sentence in lst:
            words = words + sentence.split()
        for word in words:
            if word not in output.keys():
                output[word] = 1
            else:
                output[word] += 1
        return output
```

## Proof of Work
![image](https://github.com/user-attachments/assets/6a43cb10-2372-4aac-bf74-6ddf02f9138d)


## Diagram
UML Diagram


![image](https://github.com/user-attachments/assets/796393cf-77a1-43c6-889a-f3d4758b59c0)



