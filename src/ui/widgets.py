import customtkinter as ctk

from ui.theme import *


class InfoCard(ctk.CTkFrame):

    def __init__(self, master, title):

        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=12,
            height=70
        )

        self.pack_propagate(False)

        self.title = ctk.CTkLabel(

            self,

            text=title,

            font=FONT_SMALL,

            text_color=TEXT_SECONDARY

        )

        self.title.pack(pady=(8,2))

        self.value = ctk.CTkLabel(

            self,

            text="...",

            font=FONT_HEADER

        )

        self.value.pack()

    def update_value(self,value):

        self.value.configure(
            text=str(value)
        )


class TextCard(ctk.CTkFrame):

    def __init__(self,master,title):

        super().__init__(

            master,

            fg_color=CARD,

            corner_radius=12

        )

        self.title = ctk.CTkLabel(

            self,

            text=title,

            font=FONT_HEADER

        )

        self.title.pack(
            pady=(10,5)
        )

        self.box = ctk.CTkTextbox(

            self,

            height=120,

            font=FONT_TEXT,

            wrap="word"

        )

        self.box.pack(

            fill="both",

            expand=True,

            padx=10,

            pady=(0,10)

        )

        self.box.configure(
            state="disabled"
        )

    def update_text(self,text):

        self.box.configure(
            state="normal"
        )

        self.box.delete(
            "1.0",
            "end"
        )

        self.box.insert(
            "1.0",
            text
        )

        self.box.configure(
            state="disabled"
        )