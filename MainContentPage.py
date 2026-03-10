import customtkinter as ctk
from ToolbarFrame import ToolbarFrame
from SearchFrame import SearchFrame
from SidebarFrame import SidebarFrame
from Defaults import *

class MainContentPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color = "transparent")

        self.columnconfigure(1, weight = 1)
        self.rowconfigure(1, weight = 1)

        SearchFrame(self).grid(row = 1, column = 1, padx = defaultPadding, pady = defaultPadding, sticky = "nsew")
        SidebarFrame(self).grid(row = 1, column = 0, padx = (defaultPadding, 0), pady = defaultPadding, sticky = "nsew")
        ToolbarFrame(self).grid(row = 0, column = 0, columnspan = 2, padx = defaultPadding, pady = (defaultPadding, 0), sticky = "nsew")