# Quiz032 2025/01

## Paper solution
I wasn't in class because I was sick so no paper solution

## Code
```.py
class HumanResources:
    def __init__(self, name: str, email:str, nationality: str, occupation: str):
        self.name = name
        self.email = email
        self.nationality = nationality
        self.occupation = occupation

    def get_email(self):
        return f"{self.name}'s email is {self.email}"

    def set_nationality(self, nationality: str):
        self.nationality = nationality
        return f"updated {self.name}'s nationality to {self.nationality}"

    def set_email(self, email: str):
        self.email = email
        return f"updated {self.name}'s email to {self.email}"

    def greet(self) -> str:
        return f"Welcome {self.name} working as {self.occupation}"
```

## Proof of Work
![image](https://github.com/user-attachments/assets/6ab64bca-e61a-4245-a439-f2a2ef5323db)



