# Quiz033 2025/01

## Paper solution
I wasn't in class because I was sick so no paper solution

## Code
```.py
class CompoundInterest():
    def __init__(self, principal: float, rate:float):
        self.principal = principal
        self.rate = rate

    def calculate(self, years: int) -> float:
        return f"result: {self.principal * (1 + self.rate) ** years}"
```

## Proof of Work
![image](https://github.com/user-attachments/assets/299bfe8e-8428-4547-b1be-bcea220637fa)

## Diagrams
UML Diagram
![image](https://github.com/user-attachments/assets/4d2bcd7b-29f2-4efc-86b5-7a480dee773a)
Figure taken from '[2024] Quizzes' Google Slides presentation
