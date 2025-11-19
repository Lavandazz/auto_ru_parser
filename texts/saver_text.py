from dataclasses import dataclass

import pandas as pd

from settings.logging_file import pars_logger


@dataclass
class SaverText:

    def save_to_excel(self, cars_list: list[list[str]]):
        """
        Функция сохраняет данные по всем автомобилям в excel файл.
        Принимает список со списками по всем машинам.
        :param cars_list:

        """
        # Создаем список словарей, где ключи - это номера колонок
        all_cars_data = []

        pars_logger.debug("Принято для сохранения текста %s объектов", len(cars_list))

        for cars in cars_list:
            dict_car = {}
            for i, car in enumerate(cars):
                dict_car[i] = car

            all_cars_data.append(dict_car)

        # С помощью pandas преобразуем в колонки.
        # Берем 0 индекс из списка (список состоит из 1 строки).
        try:
            cars_df = pd.DataFrame(all_cars_data)
            cars_df.to_excel("cars.xlsx", index=False)
            pars_logger.info("Сохранил")
        except Exception as e:
            pars_logger.warning("данные не сохранены: %s", e)
