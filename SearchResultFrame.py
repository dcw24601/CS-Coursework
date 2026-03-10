import customtkinter as ctk
from ItemDisplayWidget import *

class SearchResultFrame(ctk.CTkScrollableFrame):

    def __init__(self, master):

        super().__init__(master, fg_color = "transparent", scrollbar_button_color = defaultColour, scrollbar_button_hover_color = defaultHoverColour, corner_radius = 0)

        self.columnconfigure(0, weight = 1)


    def displayItems(self):

        items = itemManager.getItems(self.getSearchTerm())

        for item in range(len(items)):

            ItemDisplayWidget(self, items[item][0]).grid(row = item, column = 0, sticky = "ew", pady = (0, defaultPadding))


    def getSearchTerm(self):
        return self.master.master.master.searchBar.get()
