import customtkinter as ctk
from Defaults import *

class CircleButton(ctk.CTkFrame):
    def __init__(self,
                master,
                text = "",
                command = None,
                size = defaultSize,
                fgColour = defaultColour,
                hoverColour = defaultHoverColour,
                textColour = defaultTextColour,
                textYOffset = 0,
                font = defaultBoldFont):

        super().__init__(master, width = size, height = size, corner_radius = size//2, fg_color = fgColour)

        self.default_color = fgColour
        self.hover_color = hoverColour
        self.command = command

        self.pack_propagate(False)

        self.label = ctk.CTkLabel( self, text = text, text_color = textColour, font = font)
        self.label.place(relx = 0.5, rely = 0.5 - textYOffset, anchor = "center")

        # hover events
        self.bind("<Enter>", self.onHover)
        self.bind("<Leave>", self.onLeave)

        self.label.bind("<Enter>", self.onHover)
        self.label.bind("<Leave>", self.onLeave)

        # click events
        self.bind("<Button-1>", self.onClick)
        self.label.bind("<Button-1>", self.onClick)

        # cursor
        self.configure(cursor = "hand2")

    def onHover(self, event):
        self.configure(fg_color = self.hover_color)

    def onLeave(self, event):
        self.configure(fg_color = self.default_color)

    def onClick(self, event):
        if self.command:
            self.command()