from .card import Card


class Bank:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []

    def add_card(self, number, pin):
        if self.pin_check(pin):
            c = Card(number=number, pin=pin)
            self.cards.append(c)
        else:
            raise Exception("The pin must be digits and 4 characters long")

    def show_balance(self, number, pin):
        for c in self.cards:
            if c.number == number:
                try:
                    c.show_balance(pin)
                except Exception as exc:
                    print(exc)

    def replenish_card(self, number, pin, amount):
        if self.check_replenish_withdraw(amount):
            for c in self.cards:
                if c.number == number:
                    if c.pin == pin:
                        return c.replenish_balance(amount)
                    else:
                        raise Exception("wrong pin")
        else:
            raise Exception("Enter a positive number")

    def withdraw_money(self, number, pin, amount):
        if self.check_replenish_withdraw(amount):
            for c in self.cards:
                if c.number == number:
                    if c.pin == pin:
                        return c.withdraw_money(amount)
                    else:
                        raise Exception("wrong pin")
        else:
            raise Exception("Enter a positive number")

    def transaction(self, from_card, pin, to_card, amount):
        if self.check_replenish_withdraw(amount):
            card1, card2 = None, None

            for c in self.cards:
                if c.number == from_card:
                    if c.pin == pin:
                        card1 = c
                    else:
                        raise Exception("wrong pin")
                if c.number == to_card:
                    card2 = c

            card1.withdraw_money(amount)
            card2.replenish_balance(amount)
        else:
            raise Exception("Enter a positive number")

    def to_dict(self):
        d = dict()

        d["cards"] = [c.to_dict() for c in self.cards]

        return d

    @staticmethod
    def from_dict(data):
        b = Bank()

        for v in data["cards"]:
            c = Card.from_dict(v)
            b.cards.append(c)

        return b


    def pin_check(self, pin):
        return pin.isnumeric() and len(pin) == 4


    def check_replenish_withdraw(self, amount):
        return amount > 0

