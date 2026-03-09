import customtkinter as ctk
from Defaults import *
from CircleButton import CircleButton

class SidebarFrame(ctk.CTkFrame):

    expanded = False
    
    def __init__(self, master):
        super().__init__(master, corner_radius = defaultCornerRadius + defaultPadding)

        self.columnconfigure(1, weight = 1)

        self.menuButton = CircleButton(self, text = "\u2261", font = ("Arial", 27), textYOffset = 0.03, command = self.toggleExpanded)
        self.menuButton.grid(row = 0, column = 0, padx = defaultPadding, pady = (defaultPadding, 0), sticky = "nw")

        self.examplePlaceHolderButton = defaultButton(self, "Test Button")

    def toggleExpanded(self):
        if self.expanded == False:
            self.expand()
            self.expanded = True
        else:
            self.collapse()
            self.expanded = False

    def expand(self):
        self.examplePlaceHolderButton.grid(row=1, column = 0, columnspan = 2, padx = defaultPadding, pady = (defaultPadding, 0), sticky = "ew")

    def collapse(self):
        self.examplePlaceHolderButton.grid_remove()
