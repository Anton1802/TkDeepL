en = {
    "translating": "Translating...",
    "error": "Error",
    "error_auto": "You cannot set a translatable language in auto!",
    "error_input": "The input field is empty!",
    "error_valid_lang": "is not valid language. Valid language:",
    "error_limit_maybe": "Maybe Time limit exceeded.",
    "error_limit": "Time limit exceeded",
    "button_translate": "Translate",
    "install": "Install",
    "install_browser": "Installing browser executable. This may take some time",
    "button_switch_lang": "Switch lang"
}

ru = {
    "translating": "Перевод...",
    "error": "Ошибка",
    "error_auto": "Вы не можете установить язык перевода в автоматическом режиме!",
    "error_input": "Поле ввода пустое!",
    "error_valid_lang": "это недопустимый язык. Допустимый язык:",
    "error_limit_maybe": "Возможно, лимит времени превышен.",
    "error_limit": "Лимит времени превышен.",
    "button_translate": "Перевести",
    "install": "Загрузка",
    "install_browser": "Установка исполняемого файла браузера. Это может занять некоторое время",
    "button_switch_lang": "Сменить язык"
}


language_ = "ru"

if language_ == "en":
    language = en
elif language_ == "ru":
    language = ru
else:
    exit("Language is not valid. Set language in config")
