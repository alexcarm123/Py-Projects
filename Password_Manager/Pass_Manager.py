from tkinter import *
from tkinter import messagebox
import tkinter.messagebox


objects = []
window = Tk()
window.withdraw()
window.title('Password Manager')

class popupWindow(object):
    loop = False
    attempts = 0
    