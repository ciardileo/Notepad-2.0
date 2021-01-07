'''
This simple program is just to practice.
Adds new features and customization
to the classic notepad.
(made in my father's pc)
Complete ()
'''

# imports 

from tkinter import *
import menu
import toolbar
import textbox


# class that will execute all the program

class Notepad():
    def __init__(self):
        # window

        self.main = Tk()
        self.main.geometry('900x480')
        self.main.title('untiled - Notepad 2.0')

        # creating the toolbar

        # toolbar.Toolbar(self.main)

        # creating the menu

        menu.MenuBar(self.main)

        # executing the window

        self.main.mainloop()


# executing the program

if __name__ == "__main__":
    Notepad()
