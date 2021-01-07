# imports 

from tkinter import *

# class that will create the toolbar

class Toolbar():
	def __init__(self, main):

		# window 

		self.main = main

		# frame of the toolbar

		self.tool_frame = Frame(self.main)
		self.tool_frame.pack(fill=X)

		# toolbar items

		# (just to fill with something)

		for item in range(0, 10):
			bt = Button(self.tool_frame, height=1, width=2, text='T', borderwidth=0)
			bt.pack(side=LEFT, padx=5)

