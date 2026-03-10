import customtkinter as ctk
from SignInFrame import SignInFrame
from Defaults import *

class SignInPage(ctk.CTkFrame):

    def __init__(self, master):
        
        super().__init__(master, fg_color = "transparent")

        self.columnconfigure(1, weight = 1)
        self.rowconfigure(1, weight = 1)

        ctk.CTkLabel(self, text = "Welcome.", font = ("Arial", 100, "bold"), text_color = defaultTextColour)\
        .grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 25, sticky = "nsew")

        SignInFrame(self).grid(row = 1, column = 1, padx = 50, pady = 25)


    def signIn(self):

        self.grid_remove()

        self.master.openPage(self.winfo_toplevel().mainPage)
        