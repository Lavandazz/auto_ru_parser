from dataclasses import dataclass

from playwright.sync_api import Page, Browser, sync_playwright


@dataclass
class ParserSettings:
    """
    Класс для настроек браузера
    # Использование:
    settings = ParserSettings(url="https://auto.ru")
    page = settings.setup_browser()
    """
    url: str
    page: Page = None
    browser: Browser = None
    playwright = None

    def setup_browser(self) -> Page:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=False,
            args=[
                "--start-maximized",  # Окно на весь экран
                "--disable-blink-features=AutomationControlled",  # Убираем флаг автоматизации
                "--disable-infobars",  # Убираем сообщение "Chrome is being controlled"
                "--disable-dev-shm-usage",  # Улучшаем работу в контейнерах
                "--no-sandbox",  # Полезно в некоторых окружениях
                "--disable-popup-blocking",
                "--window-size=1920,1080"
            ],
            chromium_sandbox=False,
            ignore_default_args=["--enable-automation"],  # Отключаем automation флаг
        )
        self.page = self.browser.new_page()

        return self.page

    def close(self):
        """Закрытие браузера и playwright"""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
