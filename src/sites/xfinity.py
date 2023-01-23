from src.account_model import AccountModel
from src.driver import Driver


class XfinityPayment(AccountModel):
    def __init__(self, user_name: str, password: str, amount_to_pay: float):
        super().__init__(user_name, password)
        self.driver = Driver().get_driver()
        self.amount_to_pay = amount_to_pay

    def pay_bill(self, foo):
        print(f'Amount to pay::self {self.amount_to_pay}')
        self.pay_bill_steps1()

    def pay_bill_steps1(self):
        list_of_elements = self.driver.find_elements_by_xpath("//*[contains(text(), 'Pay Your Bill')]")
        print(f'List of elements {list_of_elements}')
