# Quiz037 2025/01

## Paper solution
This was done on computer because it's kivy

## Code
### Kivy
```.kv
Screen:
    size: 500, 500

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 0.8, 0.8
        pos_hint: {'center_x':.5, 'center_y':.5}
        md_bg_color: '#334455'

        MDLabel:
            id:msg
            text: "X Player's turn"
            size_hint: 1, 0.25
            font_size: '24pt'
            halign: 'center'
            color: 'black'
            md_bg_color: 'white'

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25

            PlayButton:
                id:btn00
            PlayButton:
                id:btn01
            PlayButton:
                id:btn02

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25

            PlayButton:
                id:btn10
            PlayButton:
                id:btn11
            PlayButton:
                id:btn12

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25

            PlayButton:
                id:btn20
            PlayButton:
                id:btn21
            PlayButton:
                id:btn22


<PlayButton>:
    size_hint: 1, 1
    font_size: '20pt'
    text_color: 'white'
    md_bg_color: '#81d4bc'
    on_press:
        app.button_pressed(self)

```

### Python
```.py
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton


class PlayButton(MDFlatButton):
    pass


class quiz037(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        Window.size = (500, 500)
        pass

    def button_pressed(self, btn):
        self.count += 1
        if btn.text == '':
            if self.root.ids.msg.text == "X Player's turn":
                btn.text = 'X'
                btn.md_bg_color = '#be0000'
                self.root.ids.msg.text = "O Player's turn"
            elif self.root.ids.msg.text == "O Player's turn":
                btn.text = 'O'
                btn.md_bg_color = '#edd79f'
                self.root.ids.msg.text = "X Player's turn"

            if self.won() and btn.text != '':
                self.root.ids.msg.text = f'{btn.text} Player won!'
            elif self.count == 9 and 'won' not in self.root.ids.msg.text:
                self.root.ids.msg.text = 'Tie!'

    def won(self) -> bool:
        win = False
        board = [
            [self.root.ids.btn00.text, self.root.ids.btn01.text, self.root.ids.btn02.text],
            [self.root.ids.btn10.text, self.root.ids.btn11.text, self.root.ids.btn12.text],
            [self.root.ids.btn20.text, self.root.ids.btn21.text, self.root.ids.btn22.text]
            ]

        for i in range(3):
            if all(board[i][j] == 'X' for j in range(3)) or all(board[j][i] == 'X' for j in range(3)):
                win = True
            elif all(board[i][j] == 'O' for j in range(3)) or all(board[j][i] == 'O' for j in range(3)):
                win = True
        if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2-i] == 'X' for i in range(3)):
            win = True
        elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2-i] == 'O' for i in range(3)):
            win = True

        if win:
            return True
        else:
            return False


GUI = quiz037()
GUI.run()

```


## Proof of Work
https://github.com/user-attachments/assets/3eeaf189-f561-49b8-9535-3aa772ef16be



