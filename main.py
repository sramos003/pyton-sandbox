from src.driver_utils import DriverUtils


class Xfinity:
    URI = "https://www.xfinity.com/bill-pay"
    USER_NAME = "foo@Gmail.com"
    PASSWORD = "bar1234$"


GOOGLE_URI = "https://www.google.com"

driver = DriverUtils()
driver\
    .navigate(GOOGLE_URI)\
    .navigate(Xfinity.URI)\
    .pay_bill(Xfinity.USER_NAME, Xfinity.PASSWORD, 200.00)\
    .quit()
