from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

class GameUI(QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.button_next = QPushButton("Следующий ход")
        self.button_next.clicked.connect(self.next_action)
        layout.addWidget(self.text_area)
        layout.addWidget(self.button_next)
        self.setLayout(layout)

    def next_action(self):
        if self.game.current_player:
            action_result = self.game.perform_action("атака")
            self.text_area.append(action_result)
        else:
            self.text_area.append("Сначала выберите персонажа")
