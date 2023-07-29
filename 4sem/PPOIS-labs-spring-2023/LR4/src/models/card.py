class Card:
    def __init__(self, number, pin, balance=0):
        self.number = number
        self.balance = balance 
        self.pin = pin

    def show_balance(self, pin):
        if self.pin != pin:
            raise Exception("wrong pin code")

        print(self.balance)

    def replenish_balance(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise Exception("insufficient funds on the card")

    def to_dict(self):
        d = dict()

        d["number"] = self.number
        d["pin"] = self.pin
        d["balance"] = self.balance

        return d

    @staticmethod
    def from_dict(data):
        c = Card(number=data["number"], pin=data["pin"])
        c.balance = data["balance"]

        return c
