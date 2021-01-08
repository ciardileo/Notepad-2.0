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

		# selected text

		self.selected_text = False

		# menu

		self.menu = Menu(self.main)
		self.main.config(menu=self.menu)

		# item "file"

		self.file_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='File', menu=self.file_menu)

		# subitems

		self.file_menu.add_command(label='New          Ctrl+N', command=lambda: self.new(False))
		self.file_menu.add_command(label='Save           Ctrl+S', command=lambda: self.save(False))
		self.file_menu.add_command(label='Save As', command=self.save_as)
		self.file_menu.add_command(label='Open', command=self.open)
		self.file_menu.add_separator()
		self.file_menu.add_command(label='Exit', command=sys.exit)

		# item "edit"

		self.edit_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='Edit', menu=self.edit_menu)

		# subitems

		self.edit_menu.add_command(label='Clear All', command=self.txt.clear_text)
		self.edit_menu.add_command(label='Copy             Ctrl+C', command=lambda: self.copy_text(False))
		self.edit_menu.add_command(label='Paste             Ctrl+V', command=lambda: self.paste_text(False))
		self.edit_menu.add_command(label='Cut                Ctrl+X', command=lambda: self.cut_text(False))
		self.edit_menu.add_command(label='Undo')
		self.edit_menu.add_command(label='Redo')

		# item "preferences"

		self.prefs_menu = Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label='Preferences', menu=self.prefs_menu)

		# subitems

		self.prefs_menu.add_command(label='Background Color')
		self.prefs_menu.add_command(label='Textbox Color')
		self.prefs_menu.add_command(label='Default Text Color')

		# key bindings

		self.main.bind('<Control-c>', self.copy_text)
		self.main.bind('<Control-v>', self.paste_text)
		self.main.bind('<Control-x>', self.cut_text)
		self.main.bind('<Control-s>', self.save)
		self.main.bind('<Control-Key-n>', self.new)

	# new file command

	def new(self, n):

		# clear textbox

		self.txt.clear_text()

		# changing the path_lb

		self.txt.path_lb['text'] = 'Path     '

		# changing the window title

		self.main.title('untiled - Notepad 2.0')

	# save file command

	def save(self, n):

		verify = self.txt.path_lb['text']

		if verify.strip() == 'Path':
			self.save_as()
		else:
			file = open(verify, 'w')
			file.write(self.txt.text_box.get(1.0, END))
			file.close()

	def save_as(self):

		# where the file will be save

		save_path = tkinter.filedialog.asksaveasfilename(defaultextension=".*", initialdir=self.app_path, filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("HTML Files", "*.html"), ("All Files", "*.*")))

		# "IF REALLY SAVED"

		if save_path:

			# changing the path_lb

			self.txt.path_lb['text'] = f'Saved: {save_path}'

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

		self.txt.path_lb['text'] = f'Saved: {file}'

		# changing the window title

		self.main.title(f'{file} - Notepad 2.0')

		# opening the file

		file_text = open(file_path, 'r')

		# insert the file text to the textbox

		self.txt.text_box.insert(END, file_text.read())

		# closing the file

		file_text.close()

	# the edit functions was a litle bit complicated to resolve, so i just copied a part from the codemy video
	# cut text

	def cut_text(self, n):

		# if this function was called by the key binding

		if n:

			self.selected_text = self.main.clipboard_get()

		else:

			# "if has something selected

			if self.txt.text_box.selection_get():

				# deleting the selected text (sel=selected)

				self.txt.text_box.delete('sel.first', 'sel.last')

				self.main.clipboard_clear()

				self.main.clipboard_append(self.selected_text)

	# copy text

	def copy_text(self, n):

		# "if has something selected

		if n:
			self.main.clipboard_get()
		else:
			if self.txt.text_box.selection_get():
				# getting the selected text

				self.selected_text = self.txt.text_box.selection_get()
				self.main.clipboard_clear()
				self.main.clipboard_append(self.selected_text)

	# paste text

	def paste_text(self, n):

		if n:
			self.selected_text = self.main.clipboard_get()

		else:

			if self.selected_text:

				# position where will be paste (INSERT = actual pointer focus line)

				position = self.txt.text_box.index(INSERT)

				# insert the text

				self.txt.text_box.insert(position, self.selected_text)





