class Bill:
    """
    object that contains data about a bill, such as total amount and period of bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a faltmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return round(to_pay, 2)