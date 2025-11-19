import time
import random

from settings.logging_file import pars_logger
from parser.parse_cars import ParserText
from parser.search_selector import SearchSelector
from texts.saver_text import SaverText


from settings.inputs_settings import BaseInput
from settings.parser_settings import ParserSettings

random_time = random.uniform(1.5, 4)


class ParserAutoRU:
    url: str = "https://auto.ru/moskva/cars/used/"

    def __init__(self):
        """Инициализация после создания объекта"""
        self.settings = ParserSettings(url=self.url)
        self.page = self.settings.setup_browser()
        self.search = SearchSelector(self.page)
        pars_logger.debug("Инициация parser")

    def search_cars(self, auto: str, model: list[str], year_from: int, year_to: int, volume: str, price: int):
        """Поиск автомобилей с фильтрами"""
        pars_logger.debug("Поиск %s автомобилей....", auto)
        # Поиск по локатору role
        search_list_auto = {"auto": auto,
                            "model": model}
        # Поиск по локатору name
        search_input_auto = {"year_from": year_from,
                             "year_to": year_to,
                             "volume": volume}

        # Открываем страницу
        self.search.goto_url(self.url)

        for key, value in search_list_auto.items():
            # Выбираем марку Mini
            self.search.search_placeholder(tag_placeholder=key)
            # Ожидание гармошки
            self.search.wait_element()

            if key == "model":
                for i in range(len(value)):

                    self.search.scroll_and_click_element(role="menuitem", locator=value[i])
                    self.search.wait_element()

            else:
                # Клик по элементу поиска
                self.search.scroll_and_click_element(role="menuitem", locator=value)
            # Нажатие, чтобы гармошка убралась
            self.page.keyboard.press("Escape")

        pars_logger.debug("Выбор дат")
        time.sleep(random_time)
        # Выбор года от и до
        for key_el, val_el in search_input_auto.items():
            pars_logger.debug("key_el %s val_el: %s", key_el, val_el)
            time.sleep(random_time)
            # Находим элемент
            self.search.search_input_place_by_name(key_el)
            # Ожидание гармошки
            self.search.wait_element()
            # Клик по элементу поиска
            self.search.scroll_and_click_element(role="menuitem", locator=val_el)

        pars_logger.debug("Выбор цены")
        time.sleep(random_time)

        price_for_input = self.search.search_input_place_by_name(name="price")
        pars_logger.debug("Цена вставлена")

        BaseInput.input_element(price_for_input, str(price))

        # Клик по кнопке Поиск
        self.search.click_button()

    def save_cars(self):

        pars_logger.debug("Поиск текста в блоках")
        parser_text = ParserText(page=self.page)
        saver = SaverText()

        all_cars = parser_text.parse_cars()
        saver.save_to_excel(all_cars)
        pars_logger.info("Данные сохранены")

    def close(self):
        """Закрытие браузера"""
        self.settings.close()
