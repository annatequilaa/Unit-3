# Quiz047 2025/02

## Paper solution
![image](https://github.com/user-attachments/assets/5123c623-fa33-473c-95f2-4de4ff6bb4c7)


## Code
```.py
class CalorieCount():
    def __init__(self, daily_limit: int):
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0

    def addMeal(self, cal, pro, car, fat):
        self.daily_intake += cal
        self.protein += pro
        self.carbs += car
        self.fat += fat

    def getProteinPercentage(self) -> float:
        return 4*self.protein/self.daily_intake

    def onTrack(self) -> bool:
        if self.daily_intake > 1500:
            return False
        else:
            return True
```

## Proof of Work
![image](https://github.com/user-attachments/assets/9f9f344f-3acb-444b-b6a3-658b30cbaf7c)


## Diagram
![image](https://github.com/user-attachments/assets/f5232430-9b2d-460d-ad6c-ae89af1f8c01)



