from .utils import FileUtils

from .bank import Bank


class App:
    @staticmethod
    def init():
        b = Bank()
        FileUtils.save_in_json(b.to_dict(), "./state.json")

    @staticmethod
    def add_card(number, pin):
        b = Bank.from_dict(FileUtils.read_from_json("./state.json"))
        b.add_card(number, pin)
        FileUtils.save_in_json(b.to_dict(), "./state.json")

    @staticmethod
    def show_balance(number, pin):
        b = Bank.from_dict(FileUtils.read_from_json("./state.json"))
        b.show_balance(number, pin)

    @staticmethod
    def replenish_card(number, pin, amount):
        b = Bank.from_dict(FileUtils.read_from_json("./state.json"))
        b.replenish_card(number, pin, amount)
        FileUtils.save_in_json(b.to_dict(), "./state.json")

    @staticmethod
    def withdraw_money(number, pin, amount):
        b = Bank.from_dict(FileUtils.read_from_json("./state.json"))
        b.withdraw_money(number, pin, amount)
        FileUtils.save_in_json(b.to_dict(), "./state.json")

    @staticmethod
    def transaction(from_card, pin, to_card, amount):
        b = Bank.from_dict(FileUtils.read_from_json("./state.json"))
        b.transaction(from_card, pin, to_card, amount)
        FileUtils.save_in_json(b.to_dict(), "./state.json")
