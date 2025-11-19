import time
from dataclasses import dataclass

from playwright.sync_api import Page

from settings.logging_file import pars_logger
from texts.transformation_text import transform_text


@dataclass
class ParserText:
    page: Page

    def parse_cars(self) -> list[list[str]]:
        # Ждем загрузки результатов
        self.page.wait_for_selector(".ListingItemTitle__link", timeout=10000)
        count = self.page.locator(".ListingItemTitle__link").count()
        pars_logger.debug(f"На странице найдено карточек: {count}")

        # Получаем все названия
        cars = []

        car_blocks = self.page.locator(".ListingItemUniversal__body-VBP9P")
        # Выбор текста в каждом блоке.
        # Создание списка из списков данных о каждой машине
        time.sleep(3)
        for car in range(car_blocks.count()):

            block = car_blocks.nth(car)

            # Обращаемся к тексту из списка, то есть [0] индекс
            all_text_in_block = (block.all_inner_texts()[0].
                                 replace('\xa0', ' ').
                                 replace('•', '').
                                 strip().
                                 split('\n')
                                 )
            # Отдельно выбирается локатор ссылки на страницу с машиной
            link = block.locator(".ListingItemTitle__link").get_attribute("href")

            all_text_in_block.append(link)
            pars_logger.debug("Преобразование текста ")
            result_text = transform_text(all_text_in_block)

            cars.append(result_text)

        pars_logger.debug("Парсинг окончен. Перехожу в сохранение")
        return cars
