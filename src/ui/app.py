import customtkinter as ctk
import shared

from ui.theme import *
from ui.widgets import InfoCard, TextCard

from setup import LANGUAGES

from threads.listener import ListenerThread
from threads.processor import ProcessorThread
from threads.speaker import SpeakerThread

from incoming.incoming_listener import IncomingListener
from incoming.incoming_processor import IncomingProcessor
from incoming.incoming_speaker import IncomingSpeaker


class VoiceTranslatorApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("AI Voice Translator")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.resizable(False, False)

        self.configure(fg_color=BG)

        self.translator_started = False

        # ===================================
        # TITLE
        # ===================================

        title = ctk.CTkLabel(

            self,

            text="🌍 AI Voice Translator",

            font=FONT_TITLE

        )

        title.pack(
            pady=(15, 10)
        )

        # ===================================
        # TOP BAR
        # ===================================

        top = ctk.CTkFrame(

            self,

            fg_color=CARD,

            corner_radius=12

        )

        top.pack(

            fill="x",

            padx=15,

            pady=(0, 10)

        )

        # ---------- My Language ----------

        ctk.CTkLabel(

            top,

            text="My Language",

            font=FONT_SMALL

        ).grid(

            row=0,

            column=0,

            padx=15,

            pady=(10, 0),

            sticky="w"

        )

        self.myLanguage = ctk.CTkOptionMenu(

            top,

            values=list(LANGUAGES.keys()),

            width=140

        )

        self.myLanguage.set("English")

        self.myLanguage.grid(

            row=1,

            column=0,

            padx=15,

            pady=(0, 10)

        )

        # ---------- Other Language ----------

        ctk.CTkLabel(

            top,

            text="Other Person",

            font=FONT_SMALL

        ).grid(

            row=0,

            column=1,

            padx=10,

            pady=(10, 0),

            sticky="w"

        )

        self.otherLanguage = ctk.CTkOptionMenu(

            top,

            values=list(LANGUAGES.keys()),

            width=140

        )

        self.otherLanguage.set("Urdu")

        self.otherLanguage.grid(

            row=1,

            column=1,

            padx=10,

            pady=(0, 10)

        )

        # ---------- Start ----------

        self.startButton = ctk.CTkButton(

            top,

            text="▶ Start",

            width=110,

            command=self.startTranslator

        )

        self.startButton.grid(

            row=1,

            column=2,

            padx=25

        )

        # ---------- Stop ----------

        self.stopButton = ctk.CTkButton(

            top,

            text="■ Stop",

            width=110,

            fg_color=DANGER,

            hover_color="#B91C1C",

            command=self.stopTranslator

        )

        self.stopButton.grid(

            row=1,

            column=3,

            padx=10

        )

        # ===================================
        # STATUS ROW
        # ===================================

        info = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        info.pack(

            fill="x",

            padx=15,

            pady=5

        )

        self.statusCard = InfoCard(

            info,

            "Status"

        )

        self.statusCard.pack(

            side="left",

            expand=True,

            fill="x",

            padx=(0,8)

        )

        self.latencyCard = InfoCard(

            info,

            "Latency"

        )

        self.latencyCard.pack(

            side="left",

            expand=True,

            fill="x",

            padx=(8,0)

        )

        # ===================================
        # TEXT AREA
        # ===================================

        textFrame = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        textFrame.pack(

            fill="both",

            expand=True,

            padx=15,

            pady=10

        )

        # LEFT COLUMN

        left = ctk.CTkFrame(

            textFrame,

            fg_color="transparent"

        )

        left.pack(

            side="left",

            fill="both",

            expand=True,

            padx=(0,6)

        )

        self.mySpeech = TextCard(

            left,

            "You Said"

        )

        self.mySpeech.pack(

            fill="both",

            expand=True,

            pady=(0,6)

        )

        self.otherSpeech = TextCard(

            left,

            "Other Person"

        )

        self.otherSpeech.pack(

            fill="both",

            expand=True
        )

                # ==========================
        # RIGHT COLUMN
        # ==========================

        right = ctk.CTkFrame(
            textFrame,
            fg_color="transparent"
        )

        right.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(6, 0)
        )

        self.myTranslation = TextCard(
            right,
            "Translated"
        )

        self.myTranslation.pack(
            fill="both",
            expand=True,
            pady=(0, 6)
        )

        self.otherTranslation = TextCard(
            right,
            "Incoming Translation"
        )

        self.otherTranslation.pack(
            fill="both",
            expand=True
        )

        self.after(
            200,
            self.refreshUI
        )

    # ==========================================
    # START
    # ==========================================

    def startTranslator(self):

        if self.translator_started:
            return

        self.translator_started = True

        self.startButton.configure(state="disabled")
        self.myLanguage.configure(state="disabled")
        self.otherLanguage.configure(state="disabled")

        shared.running.set()

        shared.my_language = LANGUAGES[
            self.myLanguage.get()
        ]

        shared.other_language = LANGUAGES[
            self.otherLanguage.get()
        ]

        threads = [

            ListenerThread(),
            ProcessorThread(),
            SpeakerThread(),

            IncomingListener(),
            IncomingProcessor(),
            IncomingSpeaker()

        ]

        for thread in threads:

            thread.daemon = True
            thread.start()

        shared.status = "Running"

        print("Translator Started")

    # ==========================================
    # STOP
    # ==========================================

    def stopTranslator(self):

        shared.running.clear()

        self.translator_started = False

        self.startButton.configure(state="normal")

        self.myLanguage.configure(state="normal")
        self.otherLanguage.configure(state="normal")

        shared.status = "Stopped"

        print("Translator Stopped")

    # ==========================================
    # REFRESH UI
    # ==========================================

    def refreshUI(self):

        try:

            self.statusCard.update_value(
                shared.status
            )

            self.latencyCard.update_value(
                f"{shared.latency:.2f} sec"
            )

            self.mySpeech.update_text(
                shared.last_input
            )

            self.myTranslation.update_text(
                shared.last_translation
            )

            self.otherSpeech.update_text(
                shared.last_incoming
            )

            self.otherTranslation.update_text(
                shared.last_incoming_translation
            )

        except Exception:
            pass

        self.after(
            200,
            self.refreshUI
        )


if __name__ == "__main__":

    app = VoiceTranslatorApp()

    app.mainloop()