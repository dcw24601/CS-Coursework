import customtkinter as ctk

defaultButtonSize = 50
defaultCornerRadius = defaultButtonSize // 2
defaultPadding = 10
defaultTextEntryWidth = 200

defaultGradColour = (0x3c, 0x69, 0x12)

defaultButtonColour = "#3c6912"
defaultButtonHoverColour = "#335a09"
defaultTextColour = "#A5A5A5"
defaultTextHoverColour = "#898989"
defaultBorderColour = "#565B5E"

defaultFont = ("Arial", 16)
defaultBoldFont = ("Arial", 25, "bold")

def defaultButton(master, text = "", command = None):
    return ctk.CTkButton(
        master,
        height = defaultButtonSize,
        corner_radius = defaultCornerRadius,
        fg_color = defaultButtonColour,
        hover_color = defaultButtonHoverColour,
        text = text,
        text_color = defaultTextColour,
        font = defaultBoldFont,
        command = command)
