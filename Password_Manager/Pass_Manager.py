from tkinter import *
from tkinter import messagebox
import tkinter.messagebox


objects = []
window = Tk()
window.withdraw()
window.title('Password Manager')

#Class that builds window for initial login
class popupWindow(object):
    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input Password')
        top.geometry('{}x{}'.format(250,100))
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Password: ", font=('Courier', 14), justify=CENTER)
        self.l.pack()
        self.e = Entry(top, show='*', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit', command=self.cleanup, font=('Courier', 14))
        self.b.pack()
    def cleanup(self):
        self.value = self.e.get()
        access = 'alex'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.e .delete(0, 'end')
            messagebox.showerror('Incorrect Password, attempts remaining: ' + str(5-self.attempts))

# Class for adding login credentials to the list
class entity_add:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.username = e
        self.window = master

    def write(self):
        f = open('users.txt', 'a')
        n = self.name
        e = self.username
        p = self.password

        encryptedN = ''
        encryptedE = ''
        encryptedP = ''

        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter)+5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter)+5)
        
        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter)+5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ',\n')
        f.close()
    