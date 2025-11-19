import logging
from pathlib import Path
from typing import Optional

from colorlog import ColoredFormatter

PROJECT_ROOT = Path(__file__).resolve().parent


class LoggerFactory:
    """ Базовый класс"""
    log_folder: Optional[Path] = None

    @classmethod
    def get_folder(cls) -> Path:
        """
        Создаем папку, если ее не существует.
        exist_ok - проверяет на наличие папки
        """
        log_folder = PROJECT_ROOT / 'logs'
        log_folder.mkdir(exist_ok=True)

        cls.log_folder = log_folder
        return cls.log_folder

    @classmethod
    def create_logger(cls, name: str, log_filename: str, level=logging.INFO) -> logging.Logger:
        """Создает и настраивает логгер"""
        logger = logging.getLogger(name)

        if logger.handlers:
            return logger

        logger.setLevel(level)

        # 1. Цветной вывод в консоль
        console_formatter = ColoredFormatter(
            '%(log_color)s%(levelname)-8s%(reset)s %(asctime)s [%(name)s] '
            '(%(filename)s).%(funcName)s(%(lineno)d) %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )
        file_formatter = logging.Formatter(
            '%(levelname)-8s %(asctime)s [%(name)s] '
            '(%(filename)s).%(funcName)s(%(lineno)d) %(message)s'
        )
        # Получаем путь к файлу от папки
        folder = cls.get_folder()
        log_file = folder / log_filename

        # Консольный обработчик
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)

        # Файловый обработчик
        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setFormatter(file_formatter)

        # Добавляем обработчики
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.propagate = False  # чтобы aiogram не перекрывал логи, иначе видно только логи мидлваров

        # Логируем успешную настройку
        logger.info(f"Логирование для '{logger.name}' настроено успешно.")

        return logger


# Инициализация
pars_logger = LoggerFactory.create_logger("pars_logger", "pars.log", logging.INFO)
