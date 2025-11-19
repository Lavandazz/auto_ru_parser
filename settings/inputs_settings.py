from dataclasses import dataclass

from playwright.sync_api import Locator

from settings.logging_file import pars_logger


@dataclass
class BaseInput:
    """
    Класс для введения данных в поля, такие как Марка, Модель авто
    """
    @staticmethod
    def input_element(item: Locator, element: str):
        """
        Ввод данных в поле
        :param item: Элемент страницы, поле для ввода, куда необходимо вставлять текст
        :param element: Вводимый текст
        """
        item.fill(element)
        pars_logger.debug("Элемент %s вставлен в поле %s", element, item)


@dataclass
class InputYear(BaseInput):
    year: str


@dataclass
class InputPrice(BaseInput):
    price: str

