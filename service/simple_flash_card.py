from tkinter import *

from .config import *
from .canvas import CardCanvas
from .button import CardButton
from .data import WordData

word_data = WordData(file_path=DATA_FILE_PATH)

current_word = {
    "French": "",
    "English": "",
}


def next_word():
    global current_word, window
    current_word = word_data.get_random_word()
    card_canvas.flip_card(image=canvas_front_image)
    card_canvas.change_word(
        title="French",
        word=current_word["French"],
        title_color=CARD_FRONT_TITLE_COLOR,
        word_color=CARD_FRONT_WORD_COLOR
    )
    window.after(3000, func=flip_card)


def flip_card():
    global current_word
    card_canvas.flip_card(image=canvas_back_image)
    card_canvas.change_word(
        title="English",
        word=current_word["English"],
        title_color=CARD_BACK_TITLE_COLOR,
        word_color=CARD_BACK_WORD_COLOR
    )


window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)

canvas_front_image = PhotoImage(file=FRONT_IMAGE)
canvas_back_image = PhotoImage(file=BACK_IMAGE)
first_word = word_data.get_random_word()
card_canvas = CardCanvas(
    canvas_front_image=canvas_front_image,
)

button_wrong_image = PhotoImage(file=WRONG_IMAGE)
button_wrong = CardButton(
    image=button_wrong_image,
    row=1,
    column=0,
    command=next_word,
)

button_right_image = PhotoImage(file=RIGHT_IMAGE)
button_right = CardButton(
    image=button_right_image,
    row=1,
    column=1,
    command=next_word,
)

next_word()

window.mainloop()
