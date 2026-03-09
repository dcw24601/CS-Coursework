from math import sqrt

import customtkinter as ctk
from PIL import Image
from Defaults import defaultGradColour

class Gradient(ctk.CTkLabel):

    def __init__(self, master, width, height, dir, colour = defaultGradColour):
        self.gradient = Image.new("RGBA", (width, height))

        if dir == "up":

            for y in range(height):
                alpha = y / height
                pixelColour = (colour[0], colour[1], colour[2], int(alpha * 256))

                for x in range(width):

                    self.gradient.putpixel((x, y), pixelColour)


        if dir == "down":

            for y in range(height):

                alpha = y / height
                pixelColour = (colour[0], colour[1], colour[2], int(alpha * 256))

                for x in range(width):

                    self.gradient.putpixel((x, height - y - 1), pixelColour)

        if dir == "right":

            for x in range(width):

                alpha = x / width
                pixelColour = (colour[0], colour[1], colour[2], int(alpha * 256))

                for y in range(height):

                    self.gradient.putpixel((x, y), pixelColour)

        if dir == "left":

            for x in range(width):

                alpha = x / width
                pixelColour = (colour[0], colour[1], colour[2], int(alpha * 256))

                for y in range(height):
                    
                    self.gradient.putpixel((width - x - 1, y), pixelColour)

        self.image = ctk.CTkImage(light_image = self.gradient, dark_image = self.gradient, size = (width, height))

        super().__init__(master, text = "", width = width, height = height, image = self.image)    



class CircleGradient(ctk.CTkLabel):

    def __init__(self, master, radius, width, height, centreXOffset = 0, centreYOffset = 0, colour = defaultGradColour):

        self.gradient = Image.new("RGBA", (width, height))

        halfWidth = width // 2
        halfHeight = height // 2

        for x in range(-halfWidth + centreXOffset, halfWidth + centreXOffset):

            for y in range(-halfHeight + centreYOffset, halfHeight + centreYOffset):

                alpha = 1 - ((x*x + y*y) / (radius * radius))

                if alpha < 0:
                    alpha = 0

                alpha *= alpha

                pixelColour = (colour[0], colour[1], colour[2], int(alpha * 256))
    
                self.gradient.putpixel((x + halfWidth - centreXOffset, y + halfHeight - centreYOffset), pixelColour)

        self.image = ctk.CTkImage(light_image = self.gradient, dark_image = self.gradient, size = (width, height))
        
        super().__init__(master, text = "", width = width, height = height, image = self.image)
