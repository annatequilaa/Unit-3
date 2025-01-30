# Quiz038 2025/01

## Paper solution
This was done on computer because it's kivy

## Code
### Kivy
```.kv
ScreenManager:
    MysteryPageA:
        name: 'MysteryPageA'
        md_bg_color: "#a1bfd2"

    MysteryPageB:
        name: 'MysteryPageB'
        md_bg_color: "#a1bfd2"



<MysteryPageA>:
    MDLabel:
        text: 'Mystery Page A'
        font_size: '30pt'
        halign: 'center'
    MDFloatingActionButton:
        icon: "eye-on"
        style: 'standard'
        on_press:
            root.parent.current = 'MysteryPageB'
            root.message1()

<MysteryPageB>:
    MDLabel:
        text: 'Mystery Page B'
        font_size: '30pt'
        halign: 'center'
    MDFloatingActionButton:
        icon: "eye-on"
        style: 'standard'
        on_press:
            root.parent.current = 'MysteryPageA'
            root.message2()

```

### Python
```.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class quiz038(MDApp):
    def build(self):
        return

class MysteryPageA(MDScreen):
    def message1(self):
        print("This is mystery page B you pressed the button")

class MysteryPageB(MDScreen):
    def message2(self):
        print("This is mystery page A you pressed the button")

GUI = quiz038()
GUI.run()
```


## Proof of Work
https://github.com/user-attachments/assets/7d548181-a54f-437a-a94e-57495a91cefe

## Diagrams

UML Diagram


![image](https://github.com/user-attachments/assets/552365dd-6268-4891-b6d2-1732636f188c)
Figure taken from '[2024] Quizzes' Google Slides presentation



