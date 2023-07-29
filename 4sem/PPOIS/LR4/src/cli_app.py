from argparse import ArgumentParser

from src.base_app import BaseApp


class CliApp:
    def main(self):
        parser = ArgumentParser(prog="lab1", usage="%(prog)s [options]")

        parser.add_argument(
            "--init",
            help="Init simulation",
            action="store_true",
        )

        parser.add_argument(
            "--card",
            help="Card operation group"
        )
        parser.add_argument(
            "--pin",
            help="Card pin code"
        )

        parser.add_argument(
            "--add-card",
            help="Add card to bank",
        )
        parser.add_argument(
            "--show-balance",
            help="Show balance on the card",
            action="store_true"
        )
        parser.add_argument(
            "--replenish",
            help="Replenish card with amount",
            type=int,
        )
        parser.add_argument(
            "--withdraw",
            help="Withdraw the amount from the card",
            type=int,
        )

        parser.add_argument(
            "--from-card"
        )
        parser.add_argument(
            "--to-card"
        )
        parser.add_argument(
            "--transaction",
            help="Money transfer from card to card",
            type=int,
        )

        args = parser.parse_args()

        if args.init:
            BaseApp.init()

        if args.card and args.add_card:
            BaseApp.add_card(args.card, args.add_card)

        if args.card and args.pin and args.show_balance:
            BaseApp.show_balance(args.card, args.pin)

        if args.card and args.pin and args.replenish:
            BaseApp.replenish_card(args.card, args.pin, args.replenish)

        if args.card and args.pin and args.withdraw:
            BaseApp.withdraw_money(args.card, args.pin, args.withdraw)
