# Quiz035 2025/01

## Paper solution
UPLOADDDD

## Code
```.py
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return f"name is {self.name}"

    def get_age(self):
        return f"age is {self.age}"

class student(Person):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.grade = grade

    def get_grade(self):
        return f"{self.name}'s grade is {self.grade}"
```

## Proof of Work
![image](https://github.com/user-attachments/assets/3aded43d-78f5-40a5-8f0a-3922ee4ac6a1)

## Diagrams
UML Diagram
![image](https://github.com/user-attachments/assets/d15c4c3f-c790-4da3-bb97-8bd279be30a4)

