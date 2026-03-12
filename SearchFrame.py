import customtkinter as ctk
from Defaults import *
from TextEntry import TextEntryBar
from CircleButton import CircleButton
from SearchResultFrame import SearchResultFrame

class SearchFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius = defaultCornerRadius + defaultPadding)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)

        self.searchBar = TextEntryBar(self)
        self.searchBar.grid(padx = defaultPadding, pady = (defaultPadding, 0), row = 0, column = 0, sticky = "ew")
        self.searchBar.lift()

        searchButton = CircleButton(self, text = "\u2315", textYOffset = 0.05)
        searchButton.grid(row = 0, column = 1, padx = defaultPadding, pady = (defaultPadding, 0))

        resultsFrame = SearchResultFrame(self)
        resultsFrame.displayItems()
        resultsFrame.grid(row = 1, column = 0, columnspan = 2, sticky = "nsew", padx = defaultPadding, pady = defaultPadding)

