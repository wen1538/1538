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

def add_photo(id, url, titre, lieu, rubrique, featured=False, description=""):
    db = load_db()
    # On évite les doublons d'ID
    db = [i for i in db if i['id'] != id]
    db.append({
        "id": id, "url": url, "titre": titre, "lieu": lieu, 
        "rubrique": rubrique, "featured": featured, "description": description
    })
    save_db(db)
    print(f"✅ Projet '{titre}' ajouté avec succès.")

def delete_photo(photo_id):
    db = load_db()
    db = [i for i in db if i['id'] != photo_id]
    save_db(db)
    print(f"❌ Photo '{photo_id}' supprimée.")

# --- COMMENT UTILISER ---
# Pour ajouter une photo :
# add_photo("nantes_nuit", "https://i.imgur.com/...", "Nantes Nuit", "Nantes", "Nantes", featured=True)

# Pour supprimer une photo :
# delete_photo("velo")