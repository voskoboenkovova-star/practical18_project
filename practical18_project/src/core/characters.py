import json

class Character:
    def __init__(self, name, element, rarity, image_path, description=""):
        self.name = name
        self.element = element
        self.rarity = rarity
        self.image_path = image_path
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "element": self.element,
            "rarity": self.rarity,
            "image_path": self.image_path,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        return Character(
            name=data["name"],
            element=data["element"],
            rarity=data["rarity"],
            image_path=data["image_path"],
            description=data.get("description", "")
        )
