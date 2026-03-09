import customtkinter as ctk
from Defaults import *

class ClickableLabel(ctk.CTkLabel):

    def __init__(self, master, text = "", font = defaultFont, command = None, textColour = defaultTextColour, hoverColour = defaultTextHoverColour):
        super().__init__(master, text = text, font = font, text_color = textColour)

        self.command = command

        self.textColour = textColour
        self.hoverColour = hoverColour

        self.bind("<Button-1>", self.onClick)
        self.bind("<Enter>", self.onHover)
        self.bind("<Leave>", self.onLeave)

    def onClick(self, event):
        if self.command is not None:
            self.command()

    def onHover(self, event):
        self.configure(text_color = self.hoverColour)

    def onLeave(self, event):
        self.configure(text_color = self.textColour)