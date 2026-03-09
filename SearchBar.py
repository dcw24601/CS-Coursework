import customtkinter as ctk
from Defaults import *

class SearchBar(ctk.CTkEntry):

    def __init__(self, master, width = defaultTextEntryWidth, height = defaultButtonSize, font = defaultFont):

        super().__init__(master, width = width, height = height, corner_radius = defaultCornerRadius, state = "normal", font = font)

        root = self.winfo_toplevel()
        root.bind_all("<Button-1>", self.globalClick, add = "+")

    def globalClick(self, event):
        widget = event.widget

        while widget is not None and widget is not self:
            widget = widget.master

        if widget is self:
            self.configure(border_color = defaultButtonHoverColour)
        else:
            self.configure(border_color = defaultBorderColour)
            self.winfo_toplevel().focus()