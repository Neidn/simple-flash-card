from tkinter import Canvas

from .config import *


class CardCanvas(Canvas):
    def __init__(self, canvas_front_image):
        super().__init__()

        self.create_card(canvas_front_image)
        self.create_word()
        self.card_config()

    def create_card(self, canvas_front_image):
        # Front image file check
        self.create_image(CARD_WIDTH, CARD_HEIGHT, image=canvas_front_image)

    def create_word(self, **kwargs):
        self.create_text(CARD_TITLE_WIDTH, CARD_TITLE_HEIGHT, font=TITLE_FONT, fill=CARD_FRONT_TITLE_COLOR)
        self.create_text(CARD_WORD_WIDTH, CARD_WORD_HEIGHT, font=WORD_FONT, fill=CARD_FRONT_WORD_COLOR)

    def change_word(self, **kwargs):
        self.itemconfig(2, text=kwargs['title'], fill=kwargs['title_color'])
        self.itemconfig(3, text=kwargs['word'], fill=kwargs['word_color'])

    def card_config(self):
        self.config(width=WIDTH, height=HEIGHT)
        self.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.grid(row=0, column=0, columnspan=2)

    def flip_card(self, **kwargs):
        self.itemconfig(1, image=kwargs['image'])
