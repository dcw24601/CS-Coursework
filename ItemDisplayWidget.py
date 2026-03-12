import customtkinter as ctk
from RoundedCornerImage import *
from ItemManager import itemManager
from Gradient import *
from Defaults import *

class ItemDisplayWidget(ctk.CTkFrame):

    hoverColour = "#343434"
    defaultColour = "#303030"

    itemDisplayWidgetHeight = 120
    itemPadding = 8
    imageSize = itemDisplayWidgetHeight - (2 * itemPadding)
    
    def __init__(self, master, itemID = 0):
        
        super().__init__(master, corner_radius = defaultCornerRadius)

        self.itemID = itemID

        itemName = itemManager.getItemName(itemID)
        itemDescription = itemManager.getItemDescription(itemID)
        itemPrice = itemManager.getItemPrice(itemID)
        itemThumbnailPath = itemManager.getItemThumbnail(itemID)

        self.itemNameLabel = ctk.CTkLabel(self, font = defaultBoldFont, text = itemName, text_color = defaultTextColour)
        self.itemNameLabel.grid(row = 0, column = 1, padx = self.itemPadding, pady = self.itemPadding, sticky = "w")

        self.itemDescriptionLabel = ctk.CTkLabel(self, font = defaultFont, text = itemDescription, text_color = defaultTextColour)
        self.itemDescriptionLabel.grid(row = 1, column = 1, columnspan = 2, padx = self.itemPadding, pady = self.itemPadding, sticky = "nw")

        pricetag = self.getPricetag(itemPrice)
        self.priceLabel = ctk.CTkLabel(self, font = defaultBoldFont, text = pricetag, text_color = defaultTextColour)
        self.priceLabel.grid(row = 0, column = 2, padx = defaultCornerRadius, pady = self.itemPadding, sticky = "e")

        self.thumbnail = RoundedCornerImage(self, cornerRadius = defaultCornerRadius - self.itemPadding, imagePath = itemThumbnailPath, width = self.imageSize, height = self.imageSize)   
        self.thumbnail.grid(row = 0, column = 0, rowspan = 2, padx = self.itemPadding, pady = self.itemPadding)

        self.setupEventHandling()
        self.initialConfigure()


    def onHover(self, event):
        self.configure(fg_color = self.hoverColour)
        self.itemNameLabel.configure(fg_color = self.hoverColour)
        self.itemDescriptionLabel.configure(fg_color = self.hoverColour)
        self.priceLabel.configure(fg_color = self.hoverColour)


    def onLeave(self, event):
        self.configure(fg_color = self.defaultColour)
        self.itemNameLabel.configure(fg_color = self.defaultColour)
        self.itemDescriptionLabel.configure(fg_color = self.defaultColour)
        self.priceLabel.configure(fg_color = self.defaultColour)


    def onClick(self, event):
        self.master.clear()
        self.master.displayItemPage(self.itemID)


    def setupEventHandling(self):

        self.bind("<Enter>", self.onHover)
        self.bind("<Leave>", self.onLeave)

        self.itemNameLabel.bind("<Enter>", self.onHover)
        self.itemNameLabel.bind("<Leave>", self.onLeave)

        self.itemDescriptionLabel.bind("<Enter>", self.onHover)
        self.itemDescriptionLabel.bind("<Leave>", self.onLeave)

        self.thumbnail.bind("<Enter>", self.onHover)
        self.thumbnail.bind("<Leave>", self.onLeave)

        self.thumbnail.imageLabel.bind("<Enter>", self.onHover)
        self.thumbnail.imageLabel.bind("<Leave>", self.onLeave)

        self.priceLabel.bind("<Enter>", self.onHover)
        self.priceLabel.bind("<Leave>", self.onLeave)

        self.bind("<Button-1>", self.onClick)
        self.itemNameLabel.bind("<Button-1>", self.onClick)
        self.itemDescriptionLabel.bind("<Button-1>", self.onClick)
        self.thumbnail.bind("<Button-1>", self.onClick)


    def getPricetag(self, price):

        pence = str(price % 100)
        if len(pence) == 1:
            pence = "0" + pence

        pounds = str(price // 100)

        return "£" + pounds + "." + pence
    

    def initialConfigure(self):
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(1, weight=2)

        self.configure(fg_color = self.defaultColour)
        self.itemNameLabel.configure(fg_color = self.defaultColour)
        self.itemDescriptionLabel.configure(fg_color = self.defaultColour)
        self.configure(cursor = "hand2")
