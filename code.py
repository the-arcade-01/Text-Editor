from tkinter import *

# tkinter.scrolledtext provides us a text widget with vertical scrollbar
import tkinter.scrolledtext as scrolledtext

window = Tk(className = ' Text Editor')
text = scrolledtext.ScrolledText(window,width = 100, height=80)
text.pack()

# creating a menu in the window
menu  = Menu(window)
window.config(menu = menu)

filemenubar = Menu(menu)
# adding a File button the menubar
menu.add_cascade(label='File',menu = filemenubar)
# adding options to the File option
filemenubar.add_command(label = 'New')
filemenubar.add_command(label = 'Open')
filemenubar.add_command(label = 'Save')
filemenubar.add_separator()
filemenubar.add_command(label = 'Exit')

menu.add_cascade(label = 'Help')
menu.add_cascade(label = 'About')

# keeping the window open
window.mainloop()
