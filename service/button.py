from tkinter import Button


class CardButton(Button):
    def __init__(self, image, row, column, command):
        super().__init__()
        self.create_button(image)
        self.button_config(row, column, command)

    def create_button(self, image):
        self.config(image=image)

    def button_config(self, row, column, command):
        self.config(highlightthickness=0)
        self.config(command=command)
        self.grid(row=row, column=column)
