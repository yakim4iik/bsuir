import PySimpleGUI as sg

from typing import List, Optional, Tuple

from src.base_app import BaseApp


class GuiApp():
    def __init__(self) -> None:
        BaseApp.init()

    def main(self) -> None:
        button_add_card = sg.Button(button_text="Add card", key="-ADD_CARD-")
        button_withdraw_money = sg.Button(button_text="Withdraw money", key="-WITHDRAW_MONEY-")
        button_replenish_card = sg.Button(button_text="Replenish card", key="-REPLENISH_CARD-")

        layout: List[List[sg.Input]] = [
            [button_add_card],
            [button_withdraw_money],
            [button_replenish_card]
        ]

        window = sg.Window("GUI", layout=layout, size=(250, 90), resizable=True)

        while True:
            try:
                event, values = window.read()

                match event:
                    case "-ADD_CARD-":
                        card_number, pin = self._add_card_window()
                        BaseApp.add_card(card_number, pin)
                    case "-WITHDRAW_MONEY-":
                        card_number, pin = self._verify_card_window()
                        money = self._withdraw_money_window()
                        BaseApp.withdraw_money(card_number, pin, int(money))
                    case "-REPLENISH_CARD-":
                        card_number, pin = self._verify_card_window()
                        money = self._replenish_card_window()
                        BaseApp.replenish_card(card_number, pin, int(money))
                    case sg.WIN_CLOSED:
                        break
            except Exception as exc:
                sg.popup_error_with_traceback("", exc)


    def _verify_card_window(self) -> Optional[Tuple[int, int]]:
        card_number = sg.Input('card_number', enable_events=True, key="-CARD_NUMBER-", expand_x=True)
        pin_code = sg.Input("pin_code", enable_events=True, key="-PIN_CODE-", expand_x=True)
        button = sg.Button(button_text="Enter", key="-ENTER-")

        layout: List[List[sg.Input]] = [
            [card_number],
            [pin_code],
            [button]
        ]

        window = sg.Window("Verify card", layout=layout, size=(500, 210), resizable=True)

        while True:
            event, values = window.read()

            match event:
                case "-ENTER-":
                    window.close()
                    return (values["-CARD_NUMBER-"], values["-PIN_CODE-"])
                case sg.WINDOW_CLOSED:
                    break


    def _add_card_window(self) -> Optional[Tuple[int, int]]:
        card_number = sg.Input('card_number', enable_events=True, key="-CARD_NUMBER-", expand_x=True)
        pin_code = sg.Input("pin_code", enable_events=True, key="-PIN_CODE-", expand_x=True)
        button = sg.Button(button_text="Enter", key="-ENTER-")

        layout: List[List[sg.Input]] = [
            [card_number],
            [pin_code],
            [button]
        ]

        window = sg.Window("Add card", layout=layout, size=(500, 210), resizable=True)

        while True:
            event, values = window.read()

            match event:
                case "-ENTER-":
                    window.close()
                    return (values["-CARD_NUMBER-"], values["-PIN_CODE-"])
                case sg.WINDOW_CLOSED:
                    break

    def _withdraw_money_window(self) -> Optional[int]:
        money = sg.Input('money', enable_events=True, key='-MONEY-', expand_x=True)
        button = sg.Button(button_text="Enter", key="-ENTER-")

        layout: List[List[sg.Input]] = [
            [money],
            [button]
        ]

        window = sg.Window("Get money", layout=layout, size=(500, 210), resizable=True)

        while True:
            event, values = window.read()

            match event:
                case "-ENTER-":
                    window.close()
                    return values["-MONEY-"]
                case sg.WINDOW_CLOSED:
                    break
            
    def _replenish_card_window(self) -> Optional[int]:
        money = sg.Input('money', enable_events=True, key='-MONEY-', expand_x=True)
        button = sg.Button(button_text="Enter", key="-ENTER-")

        layout: List[List[sg.Input]] = [
            [money],
            [button]
        ]

        window = sg.Window("Replenish card", layout=layout, size=(500, 210), resizable=True)

        while True:
            event, values = window.read()

            match event:
                case "-ENTER-":
                    window.close()
                    return values["-MONEY-"]
                case sg.WINDOW_CLOSED:
                    break
