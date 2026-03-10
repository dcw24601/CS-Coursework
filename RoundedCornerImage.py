from Defaults import *
import customtkinter as ctk
from PIL import Image, ImageDraw

class RoundedCornerImage(ctk.CTkFrame):

    def __init__(self, master, imagePath, cornerRadius = defaultCornerRadius, width = defaultSize, height = defaultSize):

        super().__init__(master, corner_radius = cornerRadius, width = width, height = height, fg_color = "transparent")

        image = Image.open(imagePath).resize((width, height)).convert("RGBA")

        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, width, height), radius = cornerRadius, fill = 255)
        image.putalpha(mask)

        self.image = ctk.CTkImage(light_image = image, dark_image = image, size = (width, height))

        self.imageLabel = ctk.CTkLabel(self, text = "", image = self.image)

        self.imageLabel.place(relx = 0.5, rely = 0.5, anchor = "center")
        