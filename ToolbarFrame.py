import customtkinter as ctk
from Defaults import *
from CircleButton import CircleButton
from ClickableLabel import ClickableLabel
from Gradient import CircleGradient

class ToolbarFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=defaultCornerRadius + defaultPadding)
        self.columnconfigure(3, weight = 1)

        # test username, would normally come from an SQL query.
        accountUsername = "Daniel W"

        self.bgGrad = CircleGradient(self, 250, 600, defaultButtonSize + (2 * defaultPadding), centreXOffset = -35)
        self.bgGrad.grid(row = 0, column = 2, sticky = "w")

        self.accountButton = CircleButton(self, text = accountUsername[0])
        self.accountButton.grid(row = 0, column = 0, padx = (defaultPadding, 0), pady = defaultPadding)

        self.accountLabel = ClickableLabel(self, text = accountUsername, font = defaultBoldFont)
        self.accountLabel.grid(row = 0, column = 1, padx = (defaultPadding, 0), pady = defaultPadding, sticky = "w")
        self.accountLabel.lift()

        self.sellButton = defaultButton(self, "Sell")
        self.sellButton.grid(row = 0, column = 3, padx = defaultPadding, pady = defaultPadding, sticky = "e")


        