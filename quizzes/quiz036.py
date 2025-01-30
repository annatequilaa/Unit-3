# Quiz036 2025/01

## Paper solution
This was done on computer because it's kivy

## Code
###kivy
```.kv
MDScreen:
    size: 500, 500

    MDLabel:
        id: msg
        size_hint: 1, 1
        font_size: "64pt"
        color: "black"
        halign: "center"
        text: "Your name"
        pos_hint: {"center_x":.5, "center_y": .5}
        md_bg_color: "white"

    MDRaisedButton:
        id:  bbtn
        text: "Dark mode"
        text_color: "white"
        pos_hint: {"center_x":.1, "center_y": .1}
        font_size: "10pt"
        md_bg_color: "black"
        on_press:
            app.button_pressed()
```

### Python
```.py
from kivymd.app import MDApp

class quiz036(MDApp):
    def build(self):
        return

    def button_pressed(self):
        label = self.root.ids.msg
        btn = self.root.ids.bbtn
        if label.md_bg_color == [1,1,1,1]:
            label.md_bg_color = 'black'
            label.color = 'white'
            btn.md_bg_color = 'white'
            btn.text_color = 'black'
            btn.text = 'Light mode'
        else:
            label.md_bg_color = 'white'
            label.color = 'black'
            btn.md_bg_color = 'black'
            btn.text_color = 'white'
            btn.text = 'Dark mode'
            print("yo")

GUI = quiz036()
GUI.run()
```


## Proof of Work
