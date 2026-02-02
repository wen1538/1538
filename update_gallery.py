import json
import os

def update_photo(photo_id, **kwargs):
    if not os.path.exists('images.json'):
        print("Erreur: images.json absent.")
        return

    with open('images.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        if item['id'] == photo_id:
            for key, value in kwargs.items():
                item[key] = value
            break

    with open('images.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ Mis à jour : {photo_id}")

# Exemple : update_photo("velo", lieu="Nantes Centre")