import random

class Game:
    def __init__(self, characters):
        self.characters = characters
        self.history = []
        self.current_player = None

    def select_character(self, name):
        for char in self.characters:
            if char.name == name:
                self.current_player = char
                self.history.append(f"Выбрали персонажа {name}")
                return char
        return None

    def perform_action(self, action):
        if not self.current_player:
            raise Exception("Персонаж не выбран")
        result = f"{self.current_player.name} выполняет {action}"
        self.history.append(result)
        return result

    def get_history(self):
        return self.history
