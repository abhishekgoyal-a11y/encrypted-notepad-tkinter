from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400")
    root.title("Notepad")
    root.wm_iconbitmap("notepad.ico")
# text area
    text_area = Text(root, font="lucida 10 normal")
    text_area.pack(expand=True, fill=BOTH)
    file = None
# scrollbar
    scroll = Scrollbar(text_area)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=text_area.yview)
    text_area.config(yscrollcommand=scroll.set)

    def newfile():
        inputvalue = text_area.get("1.0", "end-1c")
        y = len(inputvalue)
        if y == 0:
            return None
        else:
            r = msg.askquestion("Notepad", "Are you sure , you want to delete")
            if r == "yes":
                global file
                root.title("Unititled - Notepad")
                text_area.delete("1.0", "end")
            else:
                return None

    def openfile():
        global file
        inputvalue = text_area.get("1.0", "end-1c")
        y = len(inputvalue)
        if y == 0:
            file = askopenfilename(defaultextension=".txt", filetypes=[
                                   ("All files", "*.*"), ("Text Document", "*.txt")])
            root.title(os.path.basename(file))
            text_area.delete("1.0", "end-1c")
            f = open(file, "r")
            inputvalue = f.read()
            oldpassword = ''
            alphabet = 'qwe!r1@ty}#u]2$\io |%p;3^:as&4"d*<f(g>5)h'',j-6.k_l?7=z+/x 8c{v9[bnmqwe!r1@ty}#u]2$\io|%p; 3^:as&4"d*<f(g>5)h'',j-6.k_l?7=z+/x8c{v9[bnm'
            for i in inputvalue:
                position1 = alphabet.find(i)
                newposition1 = position1+5
                oldpassword += alphabet[newposition1]
            text_area.insert("1.0", oldpassword)
        else:
            q = msg.askquestion("Notepad", "You want to save current file")
            if q == "yes":
                savefile()
                text_area.delete("1.0", "end-1c")
            else:
                file = askopenfilename(defaultextension=".txt", filetypes=[
                    ("All files", "*.*"), ("Text Document", "*.txt")])
                root.title(os.path.basename(file))
                text_area.delete("1.0", "end-1c")
                f = open(file, "r")
                inputvalue = f.read()
                oldpassword = ''
                alphabet = 'qwe!r1@ty}#u]2$\io |%p;3^:as&4"d*<f(g>5)h'',j-6.k_l?7=z+/x 8c{v9[bnmqwe!r1@ty}#u]2$\io|%p; 3^:as&4"d*<f(g>5)h'',j-6.k_l?7=z+/x8c{v9[bnm'
                for i in inputvalue:
                    position1 = alphabet.find(i)
                    newposition1 = position1+5
                    oldpassword += alphabet[newposition1]
                text_area.insert("1.0", oldpassword)

    def savefile():
        global file
        file = asksaveasfilename(initialfile="Untit.txt", defaultextension="d.txt", filetypes=[
            ("All files", "*.*"), ("Text Document", "*.txt")])
        f = open(file, "w")
        message = text_area.get("1.0", "end-1c")
        alphabet = 'qwe!r1@ty}#u]2$\io |%p;3^:as&4"d*<f(g>5)h'',j-6.k_l?7=z+/x 8c{v9[bnmqwe!r1@ty}#u]2$\io|%p; 3^:as&4"d*<f(g>5)h'',j-6.k_l?7=z+/x8c{v9[bnm'
        new_password = ''
        for i in message:
            position = alphabet.find(i)
            newposition = position-5
            new_password += alphabet[newposition]
        f.write(new_password)

    def exitfile():
        inputvalue = text_area.get("1.0", "end-1c")
        y = len(inputvalue)
        if y == 0:
            root.destroy()
        else:
            q = msg.askquestion(
                "Notepad", "Are you sure, you don't want to save file ")
            if q == "yes":
                root.destroy()
            else:
                return None

    def cut():
        text_area.event_generate(("<<Cut>>"))

    def copy():
        text_area.event_generate(("<<Copy>>"))

    def paste():
        text_area.event_generate(("<<Paste>>"))

    def Help():
        msg.showinfo("Help", "hello everyone")

    def about():
        msg.showinfo("About", "Code is written by abhishek ")
# Menubar starts
    menubar = Menu(root)
    # file menu
    filemenu = Menu(menubar, tearoff=0)
    # open new file
    filemenu.add_command(label="New", command=newfile)
    # open existing file
    filemenu.add_command(label="Open", command=openfile)
    # save current file
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    # exit
    filemenu.add_command(label="Exit", command=exitfile)
    menubar.add_cascade(label="file", menu=filemenu)
    # Edit menu
    editmenu = Menu(menubar, tearoff=0)
    # cut
    editmenu.add_command(label="Cut", command=cut)
    # copy
    editmenu.add_command(label="Copy", command=copy)
    # paste
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editmenu)
    root.config(menu=menubar)
    # help menu
    helpmenu = Menu(root, tearoff=0)
    # help
    helpmenu.add_command(label="View help", command=Help)
    # about
    helpmenu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
# Menubar ends

    root.mainloop()
