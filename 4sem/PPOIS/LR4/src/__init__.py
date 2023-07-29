from src.gui_app import GuiApp
from src.cli_app import CliApp


class App:
    def __init__(self, console: bool = False) -> None:
        self.app = CliApp() if console else GuiApp()