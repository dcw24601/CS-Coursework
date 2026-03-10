import customtkinter as ctk

defaultSize = 50
defaultCornerRadius = defaultSize // 2
defaultSmallSize = 30
defaultSmallCornerRadius = defaultSmallSize // 2
defaultPadding = 10
defaultTextEntryWidth = 200

defaultGradColour = (0x3c, 0x69, 0x12)

defaultColour = "#3c6912"
defaultHoverColour = "#335a09"
defaultTextColour = "#A5A5A5"
defaultTextHoverColour = "#898989"
defaultBorderColour = "#565B5E"

defaultFont = ("Arial", 16)
defaultBoldFont = ("Arial", 25, "bold")

def defaultButton(master, text = "", command = None, isSmall = False):

    size = defaultSize
    cornerRadius = defaultCornerRadius
    font = defaultBoldFont

    if isSmall:
        size = defaultSmallSize
        cornerRadius = defaultCornerRadius
        font = defaultFont

    return ctk.CTkButton(
        master,
        height = size,
        corner_radius = cornerRadius,
        fg_color = defaultColour,
        hover_color = defaultHoverColour,
        text = text,
        text_color = defaultTextColour,
        font = font,
        command = command)

def defaultSecondaryButton(master, text = "", command = None, isSmall = False):

    size = defaultSize
    cornerRadius = defaultCornerRadius
    font = defaultBoldFont

    if isSmall:
        size = defaultSmallSize
        cornerRadius = defaultCornerRadius
        font = defaultFont

    return ctk.CTkButton(
        master,
        height = size,
        corner_radius = cornerRadius,
        fg_color = "transparent",
        border_color = defaultBorderColour,
        border_width = 2,
        hover_color = "#353535",
        text = text,
        command = command,
        font = font
    )