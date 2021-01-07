# imports 

from tkinter import *
import sys
import textbox

# class that will create the menu

class MenuBar():
	def __init__(self, main):

		# window

		self.main = main

		# menu

		self.menu = Menu(self.main)
		self.main.config(menu=self.menu)

		# item "file"

		self.file_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='File', menu=self.file_menu)

		# subitems

		self.file_menu.add_command(label='New', command=self.new)
		self.file_menu.add_command(label='Save', command=self.save)
		self.file_menu.add_command(label='Exit', command=sys.exit)

		# item "edit"

		self.edit_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='Edit', menu=self.edit_menu)

		# subitems

		self.edit_menu.add_command(label='Clear All')
		self.edit_menu.add_command(label='Copy All')
		self.edit_menu.add_command(label='Paste')
		self.edit_menu.add_command(label='Substitute All')

		# item "preferences"

		self.prefs_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='Preferences', menu=self.prefs_menu)

		# subitems

		self.prefs_menu.add_command(label='Background Color')
		self.prefs_menu.add_command(label='Textbox Color')
		self.prefs_menu.add_command(label='Default Text Color')

	# new file command

	def new(self):
		pass

	# save file command 

	def save(self):
		pass
	
