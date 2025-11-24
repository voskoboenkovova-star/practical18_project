import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QWidget, QHBoxLayout, QVBoxLayout
from gui.character_card import CharacterCard
from gui.game_ui import GameUI

class MainWindow(QMainWindow):
    def __init__(self, characters, game):
        super().__init__()
        self.characters = characters
        self.game = game
        self.setWindowTitle("Genshin Game Project")
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QHBoxLayout()

        # Список персонажей
        self.list_widget = QListWidget()
        for char in self.characters:
            self.list_widget.addItem(char.name)
        self.list_widget.currentTextChanged.connect(self.select_character)

        # Панель карточек
        self.card_widget = CharacterCard(self.characters[0]) if self.characters else QWidget()

        # Панель игры
        self.game_ui = GameUI(self.game)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.list_widget)
        left_layout.addWidget(self.card_widget)

        layout.addLayout(left_layout)
        layout.addWidget(self.game_ui)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_character(self, name):
        character = next((c for c in self.characters if c.name == name), None)
        if character:
            self.card_widget.character = character
            self.card_widget.init_ui()
            self.game.select_character(name)

if __name__ == "__main__":
    from core.parser import fetch_characters
    from core.game import Game
    from utils.save_load import load_game

    characters, game_state = load_game()
    if not characters:
        characters = fetch_characters()
    game = Game(characters)

    app = QApplication(sys.argv)
    window = MainWindow(characters, game)
    window.show()
    sys.exit(app.exec_())
