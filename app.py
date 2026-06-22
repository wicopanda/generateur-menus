import streamlit as st
import random
from collections import defaultdict

st.set_page_config(page_title="Générateur de Menus Complet", page_icon="🍽️", layout="wide")

st.title("🍽️ Générateur de Menus Avancé")
st.markdown("### Menus équilibrés • De saison • Petit budget • 5-6 personnes")

# ==================== SIDEBAR ====================
st.sidebar.header("⚙️ Paramètres")
nb_personnes = st.sidebar.number_input("Nombre de personnes", 1, 15, 5)
mode_vegetarien = st.sidebar.checkbox("Mode Végétarien strict")
exclure = st.sidebar.text_input("Exclure un aliment")
max_temps = st.sidebar.slider("Temps maximum (min)", 10, 40, 30)
max_budget = st.sidebar.slider("Budget max par personne (€)", 2.0, 6.0, 5.0, 0.5)

st.sidebar.divider()

# ==================== BASE DE DONNÉES ====================

# ENTRÉES
entrees = [
    {"nom": "Carpaccio de tomates et mozzarella", "saison": "Été", "temps": 10, "budget": 2.8, "calories": 180, "proteines": 9, 
     "ingredients": ["tomates", "mozzarella", "basilic", "huile d'olive"], 
     "preparation": ["Trancher finement les tomates et la mozzarella.", "Disposer sur une assiette.", "Ajouter du basilic et un filet d'huile d'olive."]},
    
    {"nom": "Salade de concombre et yaourt", "saison": "Été", "temps": 8, "budget": 1.5, "calories": 95, "proteines": 4,
     "ingredients": ["concombre", "yaourt", "ail", "menthe"],
     "preparation": ["Râper le concombre.", "Mélanger avec le yaourt, l'ail et la menthe."]},
]

# PLATS
plats = [
    {"nom": "Omelette aux légumes d'été", "saison": "Été", "temps": 20, "budget": 3.2, "calories": 380, "proteines": 22,
     "ingredients": ["œufs", "courgettes", "tomates", "poivron"],
     "preparation": ["Couper les légumes en petits dés.", "Faire revenir les légumes 5 minutes.", "Verser les œufs battus et laisser cuire."]},
    
    {"nom": "Pâtes aux courgettes et lardons", "saison": "Été", "temps": 25, "budget": 3.7, "calories": 520, "proteines": 24,
     "ingredients": ["pâtes", "courgettes", "lardons", "ail"],
     "preparation": ["Cuire les pâtes.", "Faire revenir les lardons puis les courgettes.", "Mélanger avec les pâtes."]},
    
    {"nom": "Poêlée de légumes et saucisses", "saison": "Été", "temps": 25, "budget": 3.8, "calories": 490, "proteines": 26,
     "ingredients": ["saucisses", "courgettes", "aubergines", "poivrons"],
     "preparation": ["Couper les légumes.", "Faire revenir les légumes 15 min.", "Ajouter les saucisses coupées en rondelles."]},
    
    {"nom": "Riz aux légumes et œufs", "saison": "Printemps", "temps": 25, "budget": 3.3, "calories": 450, "proteines": 18,
     "ingredients": ["riz", "tomates", "courgettes", "œufs"],
     "preparation": ["Cuire le riz.", "Faire revenir les légumes.", "Cuire les œufs brouillés et mélanger."]},
]

# DESSERTS
desserts = [
    {"nom": "Compote de pommes", "saison": "Automne", "temps": 15, "budget": 1.2, "calories": 140, "proteines": 1,
     "ingredients": ["pommes", "sucre", "cannelle"],
     "preparation": ["Éplucher et couper les pommes.", "Cuire à feu doux avec un peu de sucre."]},
]

# PETIT PLAISIR
petit_plaisir = [
    {"nom": "Gratin de pâtes au fromage", "saison": "Hiver", "temps": 25, "budget": 2.5, "calories": 480, "proteines": 18,
     "ingredients": ["pâtes", "fromage râpé", "crème"],
     "preparation": ["Cuire les pâtes.", "Mélanger avec la crème et le fromage.", "Passer au four 10 min."]},
    
    {"nom": "Croque-monsieur", "saison": "Hiver", "temps": 15, "budget": 2.8, "calories": 420, "proteines": 20,
     "ingredients": ["pain de mie", "jambon", "fromage"],
     "preparation": ["Assembler le pain, jambon et fromage.", "Faire cuire à la poêle ou au four."]},
]

# ==================== FONCTIONS ====================

def filtrer(liste):
    result = liste.copy()
    if mode_vegetarien:
        result = [r for r in result if not any(x in r["ingredients"] for x in ["lardons", "saucisses", "thon", "jambon"])]
    if exclure:
        result = [r for r in result if exclure.lower() not in str(r["ingredients"]).lower()]
    result = [r for r in result if r["temps"] <= max_temps and r["budget"] <= max_budget]
    return result

def afficher_recette(recette):
    st.subheader(recette["nom"])
    budget_total = round(recette["budget"] * nb_personnes, 2)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Temps :** {recette['temps']} min")
        st.write(f"**Budget total :** {budget_total}€")
    with col2:
        st.write(f"**Calories :** {recette['calories']} kcal")
        st.write(f"**Protéines :** {recette['proteines']}g")

    st.write("**Ingrédients :**")
    for ing in recette["ingredients"]:
        st.write(f"- {ing}")

    st.write("**Étapes de préparation :**")
    for i, etape in enumerate(recette["preparation"], 1):
        st.write(f"{i}. {etape}")

# ==================== NAVIGATION ====================

menu = st.sidebar.radio("Navigation", [
    "Accueil",
    "Entrées",
    "Plats",
    "Desserts",
    "Petit Plaisir",
    "Recherche",
    "Générer des menus",
    "Générateur personnalisé",
    "Saisons"
])

# ==================== PAGES ====================

if menu == "Accueil":
    st.header("Bienvenue !")
    st.write("Utilise le menu à gauche.")

elif menu == "Entrées":
    st.header("📋 Entrées")
    for r in filtrer(entrees):
        if st.button(r["nom"], key=r["nom"]):
            afficher_recette(r)

elif menu == "Plats":
    st.header("🍽️ Plats")
    for r in filtrer(plats):
        if st.button(r["nom"], key=r["nom"]):
            afficher_recette(r)

elif menu == "Desserts":
    st.header("🍰 Desserts")
    for r in filtrer(desserts):
        if st.button(r["nom"], key=r["nom"]):
            afficher_recette(r)

elif menu == "Petit Plaisir":
    st.header("🍟 Petit Plaisir (Rapide & Pas cher)")
    for r in filtrer(petit_plaisir):
        if st.button(r["nom"], key=r["nom"]):
            afficher_recette(r)

elif menu == "Recherche":
    st.header("🔍 Recherche")
    ingredient = st.text_input("Tape un ingrédient")
    if ingredient:
        resultats = [r for r in entrees + plats + desserts + petit_plaisir 
                     if ingredient.lower() in str(r["ingredients"]).lower()]
        for r in resultats:
            if st.button(r["nom"], key=r["nom"]):
                afficher_recette(r)

elif menu == "Générer des menus":
    st.header("🎲 Générer des menus")
    nb = st.slider("Nombre de menus", 2, 5, 3)
    if st.button("Générer"):
        menus = random.sample(plats, nb)
        for i, m in enumerate(menus, 1):
            if st.button(f"Menu {i} : {m['nom']}", key=f"gen_{i}"):
                afficher_recette(m)

elif menu == "Générateur personnalisé":
    st.header("🛠️ Générateur personnalisé")
    st.write("Exemple : 15 personnes, plat du soir, pas cher et rapide")
    
    personnes = st.number_input("Nombre de personnes", 1, 20, 6)
    type_repas = st.selectbox("Type de repas", ["Soir", "Midi"])
    budget_max = st.slider("Budget max par personne", 2.0, 6.0, 4.0)
    
    if st.button("Trouver des idées"):
        resultats = [r for r in plats if r["budget"] <= budget_max and r["temps"] <= 25]
        if mode_vegetarien:
            resultats = [r for r in resultats if not any(x in r["ingredients"] for x in ["lardons", "saucisses"])]
        
        for r in resultats[:5]:
            if st.button(r["nom"], key=r["nom"]):
                afficher_recette(r)

elif menu == "Saisons":
    st.header("🌱 Menus par saison")
    saison = st.selectbox("Saison", ["Printemps", "Été", "Automne", "Hiver"])
    tous = entrees + plats + desserts
    resultats = [r for r in tous if r["saison"] == saison]
    for r in resultats:
        if st.button(r["nom"], key=r["nom"]):
            afficher_recette(r)
