from datetime import datetime

#create a rental class for renter
class Rental:
    def __init__(self, name, payment_amount, frequency='fortnightly'):
        self.name = name
        self.payment_amount = payment_amount
        self.frequency = frequency
        self.payment_dates = []

    def add_payment_date(self, payment_date):
        self.payment_dates.append(payment_date)

    def get_payment_dates(self):
        return self.payment_dates