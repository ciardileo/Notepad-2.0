# imports 

from tkinter import *
import sys
import textbox
import os
import tkinter.filedialog


# class that will create the menu

class MenuBar:
	def __init__(self, main):
		# window

		self.main = main

		# textbox execute

		self.txt = textbox.TextBox(self.main)

		# file path

		self.app_path = os.path.dirname(os.path.realpath(__file__))

		# menu

		self.menu = Menu(self.main)
		self.main.config(menu=self.menu)

		# item "file"

		self.file_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='File', menu=self.file_menu)

		# subitems

		self.file_menu.add_command(label='New', command=self.new)
		self.file_menu.add_command(label='Save', command=self.save)
		self.file_menu.add_command(label='Save As', command=self.save_as)
		self.file_menu.add_command(label='Open', command=self.open)
		self.file_menu.add_command(label='Exit', command=sys.exit)

		# item "edit"

		self.edit_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='Edit', menu=self.edit_menu)

		# subitems

		self.edit_menu.add_command(label='Clear All', command=self.txt.clear_text)
		self.edit_menu.add_command(label='Copy')
		self.edit_menu.add_command(label='Paste')

		# item "preferences"

		self.prefs_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='Preferences', menu=self.prefs_menu)

		# subitems

		self.prefs_menu.add_command(label='Background Color')
		self.prefs_menu.add_command(label='Textbox Color')
		self.prefs_menu.add_command(label='Default Text Color')

	# new file command

	def new(self):

		# clear textbox

		self.txt.clear_text()

		# changing the path_lb

		self.txt.path_lb['text'] = 'Path     '

		# changing the window title

		self.main.title('untiled - Notepad 2.0')

	# save file command

	def save(self):
		pass

	def save_as(self):

		# where the file will be save

		save_path = tkinter.filedialog.asksaveasfilename(defaultextension=".*", initialdir=self.app_path, filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("HTML Files", "*.html"), ("All Files", "*.*")))

		# "IF REALLY SAVED"

		if save_path:

			# changing the path_lb

			self.txt.path_lb['text'] = save_path

			# changing the window title

			self.main.title(f'{save_path} - Notepad 2.0')

			# writing in the file

			file = open(save_path, 'w')

			file.write(self.txt.text_box.get(1.0, END))

			# closing the file

			file.close()

	# open file command

	def open(self):

		# cleaning the textbox

		self.txt.clear_text()

		# file dialog

		file = tkinter.filedialog.askopenfilename(initialdir = f'{self.app_path}', title = 'Open File', filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("HTML Files", "*.html"), ("All Files", "*.*")))
		file_path = file

		# changing the path_lb

		self.txt.path_lb['text'] = file

		# changing the window title

		self.main.title(f'{file} - Notepad 2.0')

		# opening the file

		file_text = open(file_path, 'r')

		# insert the file text to the textbox

		self.txt.text_box.insert(END, file_text.read())

		# closing the file

		file_text.close()
