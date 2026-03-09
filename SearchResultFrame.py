import customtkinter as ctk
from ItemDisplayWidget import *

class SearchResultFrame(ctk.CTkScrollableFrame):

    def __init__(self, master):

        super().__init__(master, fg_color = "transparent", scrollbar_button_color = defaultButtonColour, scrollbar_button_hover_color = defaultButtonHoverColour, corner_radius = 0)

        self.columnconfigure(0, weight = 1)

    def displayItems(self):

        items = self.items()

        for i in range(len(items)):

            ItemDisplayWidget(self, items[i][0], items[i][1], items[i][2], items[i][3]).grid(row = i, column = 0, sticky = "ew", pady = (0, defaultPadding))

    # replace with sql at some point
    def items(self):
        return [("The all new iPhone " + str(i + 1) + " Pro Max", "Totally legit iPhone", "assets/test_image.bmp", 99999) for i in range(10)]