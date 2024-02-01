from tkinter import *

from .config import *

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=WIDTH, height=HEIGHT)
canvas_front_image = PhotoImage(file=FRONT_IMAGE)
canvas.create_image(CARD_WIDTH, CARD_HEIGHT, image=canvas_front_image)
canvas.create_text(CARD_TITLE_WIDTH, CARD_TITLE_HEIGHT, text="Title", font=TITLE_FONT, fill=CARD_TITLE_COLOR)
canvas.create_text(CARD_WORD_WIDTH, CARD_WORD_HEIGHT, text="Word", font=WORD_FONT, fill=CARD_WORD_COLOR)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)

window.mainloop()
