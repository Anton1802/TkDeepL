import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modules.deepl import DeepL
import asyncio
from libs.async_tkinter_loop import async_handler
from languages import language

class TextFieldNull(Exception):
    pass

class App(tk.Tk):
    fr_languages = {
        "Auto":"auto",
        "Bulgarian":"bg",
        "Czech":"cs",
        "Danish": "da",
        "German": "de",
        "Greek": "el",
        "English": "en",
        "Spanish": "es",
        "Estonian": "et",
        "Finnish": "fi",
        "France": "fr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Italian": "it",
        "Japan": "ja",
        "Korean": "ko",
        "Lithuanian": "lt",
        "Latvian": "lv",
        "Dutch": "nl",
        "Polish": "pl",
        "Portuguese": "pt",
        "Romanian": "ro",
        "Russian": "ru",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Swedish": "sv",
        "Turkish": "tr",
        "Ukrainian": "uk",
        "Chinese": "zh",
    }
    to_languages = fr_languages.copy()
    to_languages.pop("Auto")

    def __init__(self):
        super().__init__()
        self.geometry("640x480")

        self.fr_language = tk.StringVar(value="Auto")
        self.to_language = tk.StringVar(value="English")
        self.progress_bar_value = tk.IntVar(value=0)
        self.fr_label = ttk.Combobox(values=list(self.fr_languages.keys()), textvariable=self.fr_language)
        self.to_label = ttk.Combobox(values=list(self.to_languages.keys()), textvariable=self.to_language)
        self.translating_label = tk.Label(text=language['translating'])

        self.btn_language_reverse = tk.Button(
            self, 
            text="<--->",
            command=async_handler(self.reverse_language)
        )
        self.btn_translate = tk.Button(
            self, 
            text=language['button_translate'], 
            command=async_handler(self.translate)
        )
        self.btn_switch_language = tk.Button(
            self,
            text=language['button_switch_lang'],
            command=async_handler(self.switch_language)
        )

        self.fr_text = tk.Text(wrap="word")
        self.to_text = tk.Text(wrap="word")

        self.fr_label.pack(anchor="nw", side="left", padx=20, pady=10)
        self.to_label.pack(anchor="ne", side="right", padx=20, pady=10)
        self.btn_language_reverse.pack(anchor="n", side="top", pady=5, fill="x")
        self.fr_text.place(anchor="w", relx=0.012, rely=0.35, relwidth=0.45, relheight=0.4)
        self.to_text.place(anchor="e", relx=0.989, rely=0.35, relwidth=0.45, relheight=0.4)
        self.btn_translate.pack(anchor="s", side="bottom", expand=True, fill="x", pady=100)
        self.btn_switch_language.place(x=552, y=452)

    async def reverse_language(self):
        temp = self.fr_language.get()
        
        if temp in self.to_languages:
            self.fr_language.set(self.to_language.get())
            self.to_language.set(temp)
        else:
            messagebox.showerror(
                language['error'],
                language['error_valid_lang']
            )

    async def translate(self):
        self.to_text.delete(1.0, "end")

        try:
            input_text_field = self.fr_text.get("1.0", "end")
            if len(input_text_field) <= 1:
                raise TextFieldNull
        except TextFieldNull:
            messagebox.showerror(
                language['error'], 
                language['error_input']
                )
            return

        fr_language = self.fr_languages[self.fr_language.get()]
        to_language = self.to_languages[self.to_language.get()]

        t = DeepL(fr_lang=fr_language, to_lang=to_language)
        timeout_ms = t.timeout

        self.progress_bar_translate = ttk.Progressbar(
            orient="horizontal", 
            variable=self.progress_bar_value,
            maximum=float(timeout_ms)
        )

        self.progress_bar_translate.place(anchor="center", relx=0.5, rely=0.6)
        self.translating_label.place(anchor="center", relx=0.5, rely=0.65)

        task = asyncio.create_task(self.activate_progress_bar(timeout_ms))
        translate_text = await t.translate(input_text_field)
        self.to_text.insert(1.0, translate_text)

        self.translating_label.place_forget()
        self.progress_bar_translate.place_forget()
        self.progress_bar_value.set(0)
        task.cancel()

    async def activate_progress_bar(self, timeout_ms: int):
        for _ in range(timeout_ms//1000):
            value = self.progress_bar_value.get()
            value += 1000
            self.progress_bar_value.set(value)
            await asyncio.sleep(1)

    async def switch_language(self):
        messagebox.showinfo(
            "Info",
            "Function is not work"
        )