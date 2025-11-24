import requests
import os

def download_image(url, save_path):
    if not os.path.exists(save_path):
        r = requests.get(url)
        with open(save_path, "wb") as f:
            f.write(r.content)
