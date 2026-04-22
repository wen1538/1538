import json
import os

DB_FILE = 'images.json'

def load_db():
    if not os.path.exists(DB_FILE): return []
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_photo(id, url, titre, lieu, rubrique="Pomme", iso="ISO 100", focale="35mm", ouverture="f/2.8"):
    """
    Rubriques valides : 'Journal', 'View On', 'Eponyme', 'Pomme'
    """
    db = load_db()
    db = [i for i in db if i['id'] != id]
    db.append({
        "id": id, "url": url, "titre": titre, "lieu": lieu, 
        "rubrique": rubrique, "iso": iso, "focale": focale, 
        "ouverture": ouverture
    })
    save_db(db)
    print(f"✅ Élément '{titre}' ajouté avec succès.")