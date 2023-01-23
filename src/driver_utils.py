from src.driver import Driver
from src.sites.xfinity import XfinityPayment


def get_service(current_uri: str, user_name: str, password: str, amount_to_pay: float):
    service_dict = {
        'xfinity': XfinityPayment(user_name, password, amount_to_pay)
    }
    for key in service_dict:
        # refactor to array of services and if 'current_uri' is in dict then return model for service.
        if key in current_uri:
            print(f'{key} :: {service_dict.get(key)}')
            return service_dict.get(key)


class DriverUtils:

    def __init__(self):
        self.driver = Driver().get_driver()
        self.current_service = None

    def navigate(self, uri: str):
        self.driver.get(uri)
        self.is_valid(uri)
        return self

    def is_valid(self, uri: str):
        assert (self.driver.current_url.__contains__(uri))
        print(f"URL = {uri}")
        return self

    def quit(self):
        print(f"closing driver {self.driver.name}")
        self.driver.quit()

    def pay_bill(self, user_name: str, password: str, amount_to_pay: float):
        service = get_service(self.driver.current_url, user_name, password, amount_to_pay)
        service.pay_bill(self.driver)
        return self

