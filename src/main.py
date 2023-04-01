from modules.app import App
from libs.async_tkinter_loop import async_mainloop


if __name__ == "__main__":
    async_mainloop(App(), title="TkDeepL")
