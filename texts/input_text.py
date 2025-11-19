

PAGES = {
    "main_page": "https://auto.ru/",
    "used_page": "https://auto.ru/moskva/cars/used/",
}

MAIN_PAGE = ["легковые", "С пробегом"]

# Кнопка поиска авто. Если искать по классу авто, необходимо искать второе совпадение.
BNT_SHOW = {"class": "Button2__content-eyTVN", "text": ["Показать",  "предложений"]}

# метки для фильтрации авто по полю placeholder
TAGS_PLACEHOLDER = {
    "auto": "Марка",
    "model": "Модель",
    "year_from": "Год от",
    "year_to": "до",
    "volume": "Объем от, л",
    "price": "Цена от, ₽"
}

# метки для фильтрации авто по полю names
TAGS_NAMES = {
    "auto": "mark",
    "model": "model",
    "year_from": "year_from",
    "year_to": "year_to",
    "volume": "displacement_from",
    "price": "price_to"
}

# Маркер всплывающего окна (гармошка)
marker = "div.Popup_visible"
