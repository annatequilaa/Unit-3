# Quiz046 2025/02

## Paper solution
![image](https://github.com/user-attachments/assets/30267480-7f71-4f7a-a9f6-7a6ea05adf39)


## Code
```.py
class Citizen():
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
    def getName(self):
        return f"name: {self.name}"
    def getCity(self):
        return f"city: {self.city}"
    def getStatus(self):
        return f"status: {self.status}"

class Employee(Citizen):
    def __init__(self, name, city, status, annualSalary):
        super().__init__(name, city, status)
        self.annualSalary = annualSalary

    def getAnnualSalary(self):
        return f"annual salary: {self.annualSalary}"

class PartTimeEmployee(Employee):
    def __init__(self, name, city, status, annualSalary, fraction: float, unionMember: bool):
        super().__init__(name, city, status, annualSalary)
        self.fraction = fraction
```

## Proof of Work
![image](https://github.com/user-attachments/assets/a0ebd1c0-77f1-482f-9f55-601513f63a0a)


## Diagram
![image](https://github.com/user-attachments/assets/9ade051d-cc5f-4c9a-b4a4-0eed80aade48)


