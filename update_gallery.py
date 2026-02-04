import json
import os

def update_photo(photo_id, **kwargs):
    file = 'images.json'
    if not os.path.exists(file): 
        return print("Fichier images.json introuvable.")
        
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        if item['id'] == photo_id:
            for key, value in kwargs.items():
                if key in item: 
                    item[key] = value
            break
            
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print(f"✅ Photo {photo_id} mise à jour.")

# Exemple : update_photo("velo", titre="NOUVEAU TITRE", iso="ISO 100")