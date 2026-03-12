import customtkinter as ctk
from Defaults import *
from ItemManager import itemManager
from RoundedCornerImage import RoundedCornerImage
from CircleButton import CircleButton

class ItemPageFrame(ctk.CTkFrame):

    def __init__(self, master, itemID):

        super().__init__(master, corner_radius = defaultCornerRadius)

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)

        imageSize = 250

        self.backButton = CircleButton(self, "\u2B8C", command = self.onBackClicked)
        self.backButton.grid(row = 0, column = 0, sticky = "nw")

        self.itemThumbnail = RoundedCornerImage(self, itemManager.getItemThumbnail(itemID), width = imageSize, height = imageSize)
        self.itemThumbnail.grid(row = 1, column = 0, rowspan = 2, padx = defaultPadding, pady = defaultPadding)

        self.itemLabel = ctk.CTkLabel(self, text = itemManager.getItemName(itemID), text_color = defaultTextColour, font = defaultBoldFont)
        self.itemLabel.grid(row = 1, column = 1, padx = defaultPadding, pady = defaultPadding)

        riskLabel = ctk.CTkLabel(self, text = self.displayItemRiskScore(itemManager.getItemRiskScore(itemID)), font = defaultBoldFont, text_color = defaultTextColour)
        riskLabel.grid(row = 2, column = 1, padx = defaultPadding, pady = defaultPadding)

        self.descriptionLabel = ctk.CTkLabel(self, text = itemManager.getItemDescription(itemID), font = defaultFont, text_color = defaultTextColour, wraplength = int(imageSize * 1.3), width = int(imageSize * 1.3), height = imageSize)
        self.descriptionLabel.grid(row = 3, column = 0, padx = defaultPadding, pady = defaultPadding)

        self.purchaseButton = defaultButton(self, text = "Buy")
        self.purchaseButton.grid(row = 3, column = 1, padx = defaultPadding, pady = defaultPadding)


    def displayItemRiskScore(self, riskScore):
        rating = "Legitimacy: "

        for star in range(int(riskScore)):
            rating += "\u2605"

            # limit to 5 stars, just a safety check
            if star > 4:
                break

        return rating
    

    def onBackClicked(self):
        self.master.clear()
        self.master.displayItems()

