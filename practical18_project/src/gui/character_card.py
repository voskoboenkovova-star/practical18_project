from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

class CharacterCard(QWidget):
    def __init__(self, character):
        super().__init__()
        self.character = character
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.image_label = QLabel()
        pixmap = QPixmap(self.character.image_path).scaled(120, 120)
        self.image_label.setPixmap(pixmap)
        self.name_label = QLabel(self.character.name)
        self.info_label = QLabel(f"{self.character.element}, {self.character.rarity}-звёздный")
        layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.info_label)
        self.setLayout(layout)
