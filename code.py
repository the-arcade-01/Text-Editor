from tkinter import *

# tkinter.scrolledtext provides us a text widget with vertical scrollbar
import tkinter.scrolledtext as scrolledtext

window = Tk(className = ' Text Editor')
text = scrolledtext.ScrolledText(window,width = 100, height=50)
text.pack()

# keeping the window open
window.mainloop()
