import customtkinter as ctk
from RoundedCornerImage import *
from Gradient import *
from Defaults import *
from PIL import Image

class ItemDisplayWidget(ctk.CTkFrame):

    command = None
    
    def __init__(self, master, itemName = "", itemDescription = "", itemThumbnailPath = "", itemPrice = 0):
        
        super().__init__(master, corner_radius = defaultCornerRadius)

        self.columnconfigure(2, weight = 1)

        itemDisplayWidgetHeight = 120
        itemPadding = 8
        imageSize = itemDisplayWidgetHeight - (2 * itemPadding)

        pence = str(itemPrice % 100)
        if len(pence) == 1:
            pence = "0" + pence

        pounds = str(itemPrice // 100)

        pricetag = "£" + pounds + "." + pence

        self.pack_propagate(False)

        self.columnconfigure(1, weight=2)

        self.itemNameLabel = ctk.CTkLabel(self, font = defaultBoldFont, text = itemName, text_color = defaultTextColour)
        self.itemDescriptionLabel = ctk.CTkLabel(self, font = defaultFont, text = itemDescription, text_color = defaultTextColour)
        self.priceLabel = ctk.CTkLabel(self, font = defaultBoldFont, text = pricetag, text_color = defaultTextColour)
        self.thumbnail = RoundedCornerImage(self, cornerRadius = defaultCornerRadius - itemPadding, imagePath = itemThumbnailPath, width = imageSize, height = imageSize)

        self.itemNameLabel.grid(row = 0, column = 1, padx = itemPadding, pady = itemPadding, sticky = "w")
        self.itemDescriptionLabel.grid(row = 1, column = 1, columnspan = 2, padx = itemPadding, pady = itemPadding, sticky = "nw")
        self.priceLabel.grid(row = 0, column = 2, padx = defaultCornerRadius, pady = itemPadding, sticky = "e")
        self.thumbnail.grid(row = 0, column = 0, rowspan = 2, padx = itemPadding, pady = itemPadding)

        self.hoverColour = "#343434"
        self.defaultColour = "#303030"

        self.configure(fg_color = self.defaultColour)
        self.itemNameLabel.configure(fg_color = self.defaultColour)
        self.itemDescriptionLabel.configure(fg_color = self.defaultColour)

        # hover events
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

        # click events
        self.bind("<Button-1>", self.onClick)
        self.itemNameLabel.bind("<Button-1>", self.onClick)
        self.itemDescriptionLabel.bind("<Button-1>", self.onClick)
        self.thumbnail.bind("<Button-1>", self.onClick)

        # cursor
        self.configure(cursor = "hand2")


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
        if self.command:
            self.command()


