import requests
import os

def download_image(url, save_path):
    """
    Скачивает изображение по URL и сохраняет в save_path.
    Если файл уже существует, повторно не скачивается.
    """
    if not os.path.exists(save_path):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(r.content)
            print(f"Скачано изображение: {save_path}")
        except Exception as e:
            print(f"Ошибка при скачивании {url}: {e}")
    else:
        print(f"Файл уже существует: {save_path}")
