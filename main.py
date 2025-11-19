from input_car import AUTO, MODEL, YEAR_FROM, YEAR_TO, VOLUME, PRICE
from settings.choosing_car import CarChooise
from parser.full_process_parsing import ParserAutoRU


def start_parser():
    # Использование:
    parser = ParserAutoRU()
    car = CarChooise(
        AUTO=AUTO, MODEL=MODEL, YEAR_FROM=YEAR_FROM, YEAR_TO=YEAR_TO, VOLUME=VOLUME, PRICE=PRICE
    )
    try:
        parser.search_cars(auto=car.AUTO,
                           model=car.MODEL,
                           year_from=car.YEAR_FROM,
                           year_to=car.YEAR_TO,
                           volume=car.VOLUME,
                           price=car.PRICE)

        parser.save_cars()

        parser.close()

        # Удалить, если не нужна открытая странциа
        input('Нажми Enter чтобы закрыть браузер...')
        parser.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start_parser()
