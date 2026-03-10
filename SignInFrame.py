import customtkinter as ctk
from TextEntry import TextEntryBar
from Defaults import *

class SignInFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, corner_radius = defaultCornerRadius, border_width = 2, border_color = defaultBorderColour)

        signInLabel = ctk.CTkLabel(self, text = "Sign In", font = defaultBoldFont, text_color = defaultTextColour)
        signInLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "new", padx = defaultPadding, pady = defaultPadding)

        emailLabel = ctk.CTkLabel(self, text = "Email: ", font = defaultFont, text_color = defaultTextColour)
        emailLabel.grid(row = 1, column = 0, padx = defaultPadding, pady = defaultPadding, sticky = "w")

        emailEntry = TextEntryBar(self, height = defaultSmallSize)
        emailEntry.grid(row = 1, column = 1, padx = defaultPadding, pady = defaultPadding)

        passwordLabel = ctk.CTkLabel(self, text = "Password: ", font = defaultFont, text_color = defaultTextColour)
        passwordLabel.grid(row = 2, column = 0, padx = defaultPadding, pady = defaultPadding, sticky = "w")

        passwordEntry = TextEntryBar(self, height = defaultSmallSize)
        passwordEntry.grid(row = 2, column = 1, padx = defaultPadding, pady = defaultPadding)

        self.signUpGrid = ctk.CTkFrame(self, fg_color = "transparent")
        self.signUpGrid.grid(row = 4, column = 0, columnspan = 2, pady = 2)

        signInLabel = ctk.CTkLabel(self.signUpGrid, text = "New Here?", font = defaultFont, text_color = defaultTextColour)
        signInLabel.grid(row = 0, column = 0, padx = defaultPadding, pady = defaultPadding * 3, sticky = "e")

        signUpButton = defaultSecondaryButton(self.signUpGrid, text = "Sign up", isSmall = True)
        signUpButton.grid(row = 0, column = 1, padx = (0, defaultPadding), pady = defaultPadding * 3, sticky = "w")

        loginButton = ctk.CTkButton(self, command = master.signIn,
                                    height = 40, corner_radius = 20,
                                    fg_color = defaultColour, hover_color = defaultHoverColour,
                                    text = "Log in", font = ("Arial", 20, "bold"), text_color = defaultTextColour)
        loginButton.grid(row = 3, column = 1, padx = defaultPadding, pady = defaultPadding)

