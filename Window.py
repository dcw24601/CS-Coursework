import customtkinter as ctk
from MainContentPage import MainContentPage
from SignInPage import SignInPage

class Window(ctk.CTk):

    def __init__(self, windowText = ""):
        super().__init__()

        self.title(windowText)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.geometry("800x600")

        self.mainPage = MainContentPage(self)
        self.signIn = SignInPage(self)

        self.openPage(self.signIn)

        self.mainloop()


    def openPage(self, page):
        page.grid(row = 0, column = 0, sticky = "nsew")