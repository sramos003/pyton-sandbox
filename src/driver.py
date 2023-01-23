from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DriverConstants:
    DRIVER_PATH = "driver/chromedriver.exe"
    START_MAXIMIZED = "--start-maximized"
    HEADLESS = "--headless"
    DISABLE_GPU = "--disable-gpu"


class DriverServiceOptions:
    CONSTANTS = DriverConstants()
    ARGUMENTS = [
        CONSTANTS.START_MAXIMIZED,
        CONSTANTS.DISABLE_GPU,
    ]

    def get_driver_options(self):
        _options = webdriver.ChromeOptions()
        for argument in self.ARGUMENTS:
            _options.add_argument(argument)
        return _options

    def get_driver_service(self):
        return Service(self.CONSTANTS.DRIVER_PATH)


class Driver:
    def __init__(self):
        driver_info = DriverServiceOptions()
        self.driver = webdriver.Chrome(service=driver_info.get_driver_service(),
                                       options=driver_info.get_driver_options()
                                       )

    def get_driver(self):
        print(f"returning driver:: {self.driver.name}")
        return self.driver
