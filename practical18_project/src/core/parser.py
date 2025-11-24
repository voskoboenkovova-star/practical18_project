import requests
import os
from core.characters import Character
from utils.downloader import download_image

API_URL = "https://genshin.jmp.blue/"

def fetch_characters():
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception("Не удалось получить данные с API")
    
    characters_data = response.json()
    characters = []
    for char in characters_data:
        image_path = os.path.join("resources/characters", f"{char['name']}.png")
        download_image(char['image'], image_path)
        character = Character(
            name=char['name'],
            element=char['element'],
            rarity=char['rarity'],
            image_path=image_path,
            description=char.get("description", "")
        )
        characters.append(character)
    return characters
