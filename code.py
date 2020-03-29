from tkinter import Tk, scrolledtext, filedialog, Menu, END, messagebox, simpledialog
import os
# tkinter.scrolledtext provides us a text widget with vertical scrollbar

window = Tk(className = ' Text Editor')
text = scrolledtext.ScrolledText(window,width = 100, height=80)
text.pack()

def openFile():
    text.delete('1.0',END)
    file = filedialog.askopenfile(parent = window,mode='rb',title='Select a text file',filetype=(('Text File','*.txt'),('All Files','*.*')))
    window.title(os.path.basename(file.name) + '- Text Editor')
    contents = file.read()
    text.insert('1.0',contents)
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode='w')
    contents = text.get('1.0',END)
    file.write(contents)
    file.close()

def exitFile():
    if messagebox.askyesno('Exit','Are you sure want to quit ?'):
        window.destroy()

def aboutFile():
    label = messagebox.showinfo('About','A text editor, created using Python')

def newFile():
    if messagebox.askyesno('Save','Do you want to save?'):
        saveFile()
    text.delete('1.0',END)

def findtext():
    findstr = simpledialog.askstring('Find','Enter the text')
    contents = text.get('1.0',END)
    if findstr in contents:
        messagebox.showinfo('Result',f"{findstr}' string is present")
    else:
        messagebox.showinfo('Result','Not Found!!')


# creating a menu in the window
menu  = Menu(window)
window.config(menu = menu)

filemenubar = Menu(menu)
# adding a File button the menubar
menu.add_cascade(label='File',menu = filemenubar)
# adding options to the File option
filemenubar.add_command(label = 'New', command = newFile)
filemenubar.add_command(label = 'Open', command = openFile)
filemenubar.add_command(label = 'Save', command = saveFile)
filemenubar.add_command(label = 'Find', command = findtext)
filemenubar.add_separator()
filemenubar.add_command(label = 'Exit', command = exitFile)

menu.add_cascade(label = 'Help')
menu.add_cascade(label = 'About', command = aboutFile)

# keeping the window open
window.mainloop()
