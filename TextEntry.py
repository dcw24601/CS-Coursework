import customtkinter as ctk
from Defaults import *

class TextEntryBar(ctk.CTkEntry):

    def __init__(self, master, width = defaultTextEntryWidth, height = defaultSize, font = defaultFont):

        super().__init__(master, width = width, height = height, corner_radius = height // 2, state = "normal", font = font)

        root = self.winfo_toplevel()
        root.bind_all("<Button-1>", self.globalClick, add = "+")

    def globalClick(self, event):
        widget = event.widget

        # find which widget was clicked on
        while widget is not None:
            clickedEntry = None

            if isinstance(widget, TextEntryBar):
                clickedEntry = widget
                break

            widget = widget.master

        # if the click was on the widget, focus and highlight border
        if clickedEntry is self:
            self.configure(border_color = defaultColour)

        # if not, set border colour to default and focus on entire screen
        else:
            self.configure(border_color = defaultBorderColour)

            if clickedEntry is None:
                self.winfo_toplevel().focus()