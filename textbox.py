# imports 

from tkinter import *

# class that will create the text input area

class TextBox():
    def __init__(self, main):
        
        # window

        self.main = main

        # textbox frame 

        self.text_frame = Frame(self.main)
        self.text_frame.pack(fill=BOTH, expand=True)

        # vertical scrollbar

        self.vertical_scroll = Scrollbar(self.text_frame)
        self.vertical_scroll.pack(side=RIGHT, fill=Y)

        # textbox

        self.text_box = Text(self.text_frame, yscrollcommand=self.vertical_scroll.set, font='OpenSans 12')
        self.text_box.pack(fill=BOTH, padx=5, expand=True)

        # configure vertical scrollbar

        self.vertical_scroll.configure(command=self.text_box.yview)

        # bottom frame

        self.bottom_frame = Frame(self.main)
        self.bottom_frame.pack(fill=X)

        # path label

        self.path_lb = Label(self.bottom_frame, text='Path         ')
        self.path_lb.pack(fill=X, side=RIGHT)




    # clear the textbox

    def clear_text(self):

        self.text_box.delete(1.0, END)

