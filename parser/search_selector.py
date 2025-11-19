import time
from dataclasses import dataclass

from playwright.sync_api import Page, Locator

from logging_file import pars_logger
from texts.input_text import TAGS_PLACEHOLDER, TAGS_NAMES


@dataclass
class SearchSelector:
    page: Page

    def goto_url(self, url: str):
        """Открытие страницы"""
        self.page.goto(url)
        pars_logger.debug("Страница %s", url)

    def search_placeholder(self, tag_placeholder: str):
        """
        Поиск локатора и клик по полю (например, поле Марка, Модель).
        Клик необходим для того, чтобы раскрылась гармошка выбора поля.
        :param tag_placeholder: Значение из placeholder для фильтрации
        """
        # Поиск элемента (Марка, модель... и клик)
        placeholder = TAGS_PLACEHOLDER.get(tag_placeholder)

        pars_logger.debug("Поиск по placeholder %s", placeholder)
        search_el = self.page.get_by_placeholder(placeholder)

        search_el.click()

        time.sleep(1.3)

    def search_input_place_by_name(self, name: str | int) -> Locator:
        """
        Нахождение поля для ввода на странице.
        Поиск осуществляется по названию поля name.
        Например, "input[name='...']"
        :return name - возвращает найденное поле для дальнейшего взаимодействия с ним.
        """
        input_name = TAGS_NAMES.get(name)
        item = self.page.locator(f"input[name={input_name}]")
        pars_logger.debug("Найден элемент и кликнут %s", input_name)

        item.click()
        return item

    def wait_element(self, marker="div.Popup_visible"):
        """
        Ожидание появления элемента (раскрывающейся гармошки) со списком выбора.
        Пример: гармошка в поле Марки авто
        :param marker: маркер для поиска гармошки (раскрывающегося окна)
        """
        pars_logger.debug("Ожидание появления маркера %s", marker)
        # Ждем появления раскрывающегося меню
        self.page.wait_for_selector(marker)

    def scroll_and_click_element(self, role: str, locator: str):
        """
        Нахождение элемента на странице и прокрутка до него.
        Поиск осуществляется по роли и тексту.
        :param locator: Элемент для поиска и взаимодействия, это Mini, Hatch или объем.
        Все, что имеет текст, до которого необходима прокрутить.
        Например, div[role="menuitem"]:has-text("Mini")
        :param role: Роль для поиска элемента.
        :return:
        """
        pars_logger.debug("Прокрутка к элементу %s", locator)

        item = self.page.locator(f'div[role="{role}"]:has-text("{locator}")').first
        try:
            item.scroll_into_view_if_needed()
            time.sleep(1)
            item.click()
            pars_logger.debug("Клик %s", locator)
            time.sleep(0.6)
        except Exception as e:
            pars_logger.error(e)
            item.click()

    def click_button(self):
        """
        Клик по кнопке.
        По умолчанию используется кнопка поиска авто "Показать...предложений"
        Поиск по роли селектора "button"
        """
        try:
            button = self.page.locator('.Button2_themeType_primary-bnQga')
            pars_logger.debug(f"Первая попытка {button}")
            button.click()
        except Exception as e:
            pars_logger.error("Не найдено кнопки Показать: %s", e)
            button = self.page.locator('button[class*="Button2_themeType_primary"]')
            pars_logger.debug(f"последняя попытка {button}")

            button.click()
