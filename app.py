import streamlit as st
import random
from collections import defaultdict

st.set_page_config(page_title="Générateur de Menus Complet", page_icon="🍽️", layout="wide")

st.title("🍽️ Générateur de Menus Avancé - Version Complète")
st.markdown("### Menus équilibrés • De saison • Petit budget • 5-6 personnes")

# ==================== SIDEBAR ====================
st.sidebar.header("⚙️ Paramètres")
nb_personnes = st.sidebar.number_input("Nombre de personnes", 1, 10, 5)
mode_vegetarien = st.sidebar.checkbox("Mode Végétarien strict")
exclure = st.sidebar.text_input("Exclure un aliment")
max_temps = st.sidebar.slider("Temps max (minutes)", 10, 40, 30)
max_budget = st.sidebar.slider("Budget max par personne", 2.0, 6.0, 5.0, 0.5)

st.sidebar.divider()
st.sidebar.info("Version très avancée")

# ==================== BASE DE DONNÉES ====================

entrees = [
    {"nom": "Carpaccio de tomates et mozzarella", "saison": "Été", "temps": 10, "budget": 2.8, "calories": 180, "proteines": 9, "ingredients": ["tomates", "mozzarella", "basilic"], "type": "entrée"},
    {"nom": "Salade de concombre et yaourt", "saison": "Été", "temps": 8, "budget": 1.5, "calories": 95, "proteines": 4, "ingredients": ["concombre", "yaourt", "ail"], "type": "entrée"},
    {"nom": "Velouté de carottes", "saison": "Automne", "temps": 25, "budget": 2.2, "calories": 140, "proteines": 3, "ingredients": ["carottes", "oignon"], "type": "entrée"},
    {"nom": "Salade de lentilles", "saison": "Printemps", "temps": 15, "budget": 2.5, "calories": 220, "proteines": 12, "ingredients": ["lentilles", "oignon rouge"], "type": "entrée"},
    {"nom": "Tomates cerises et feta", "saison": "Été", "temps": 10, "budget": 2.6, "calories": 160, "proteines": 7, "ingredients": ["tomates cerises", "feta"], "type": "entrée"},
    {"nom": "Soupe de courgettes", "saison": "Été", "temps": 20, "budget": 2.0, "calories": 110, "proteines": 4, "ingredients": ["courgettes", "oignon"], "type": "entrée"},
    {"nom": "Salade de pois chiches", "saison": "Printemps", "temps": 12, "budget": 2.3, "calories": 210, "proteines": 11, "ingredients": ["pois chiches", "tomates"], "type": "entrée"},
    {"nom": "Radis et beurre", "saison": "Printemps", "temps": 5, "budget": 1.8, "calories": 120, "proteines": 3, "ingredients": ["radis", "beurre"], "type": "entrée"},
]

plats = [
    {"nom": "Omelette aux légumes d'été", "saison": "Été", "temps": 20, "budget": 3.2, "calories": 380, "proteines": 22, "ingredients": ["œufs", "courgettes", "tomates"], "type": "plat"},
    {"nom": "Pâtes aux courgettes et lardons", "saison": "Été", "temps": 25, "budget": 3.7, "calories": 520, "proteines": 24, "ingredients": ["pâtes", "courgettes", "lardons"], "type": "plat"},
    {"nom": "Poêlée de légumes et saucisses", "saison": "Été", "temps": 25, "budget": 3.8, "calories": 490, "proteines": 26, "ingredients": ["saucisses", "courgettes", "aubergines"], "type": "plat"},
    {"nom": "Riz aux légumes et œufs", "saison": "Printemps", "temps": 25, "budget": 3.3, "calories": 450, "proteines": 18, "ingredients": ["riz", "tomates", "courgettes"], "type": "plat"},
    {"nom": "Soupe de légumes hivernale", "saison": "Hiver", "temps": 30, "budget": 3.0, "calories": 320, "proteines": 12, "ingredients": ["carottes", "poireaux", "pommes de terre"], "type": "plat"},
    {"nom": "Pâtes à la tomate et aubergines", "saison": "Été", "temps": 28, "budget": 3.4, "calories": 480, "proteines": 16, "ingredients": ["pâtes", "aubergines", "tomates"], "type": "plat"},
    {"nom": "Salade composée thon et haricots verts", "saison": "Été", "temps": 20, "budget": 4.0, "calories": 420, "proteines": 28, "ingredients": ["thon", "haricots verts", "tomates"], "type": "plat"},
    {"nom": "Quiche aux poireaux", "saison": "Hiver", "temps": 35, "budget": 3.5, "calories": 410, "proteines": 16, "ingredients": ["pâte brisée", "poireaux", "œufs"], "type": "plat"},
    {"nom": "Curry de pois chiches", "saison": "Automne", "temps": 25, "budget": 3.1, "calories": 390, "proteines": 15, "ingredients": ["pois chiches", "tomates", "épices"], "type": "plat"},
    {"nom": "Gratin de courgettes", "saison": "Été", "temps": 30, "budget": 3.6, "calories": 380, "proteines": 14, "ingredients": ["courgettes", "fromage", "crème"], "type": "plat"},
]

desserts = [
    {"nom": "Compote de pommes", "saison": "Automne", "temps": 15, "budget": 1.2, "calories": 140, "proteines": 1, "ingredients": ["pommes"], "type": "dessert"},
    {"nom": "Fromage blanc aux fraises", "saison": "Été", "temps": 5, "budget": 1.8, "calories": 160, "proteines": 8, "ingredients": ["fromage blanc", "fraises"], "type": "dessert"},
    {"nom": "Yaourt aux fraises", "saison": "Été", "temps": 3, "budget": 1.5, "calories": 130, "proteines": 6, "ingredients": ["yaourt", "fraises"], "type": "dessert"},
    {"nom": "Pomme au four", "saison": "Automne", "temps": 20, "budget": 1.4, "calories": 150, "proteines": 1, "ingredients": ["pommes"], "type": "dessert"},
    {"nom": "Yaourt nature aux noix", "saison": "Hiver", "temps": 3, "budget": 1.6, "calories": 170, "proteines": 7, "ingredients": ["yaourt", "noix"], "type": "dessert"},
    {"nom": "Clémentines", "saison": "Hiver", "temps": 2, "budget": 1.3, "calories": 90, "proteines": 1, "ingredients": ["clémentines"], "type": "dessert"},
]

# ==================== FONCTIONS ====================

def filtrer_recettes(liste):
    result = liste.copy()
    
    if mode_vegetarien:
        result = [r for r in result if not any(x in r["ingredients"] for x in ["lardons", "saucisses", "thon", "jambon"])]
    
    if exclure:
        result = [r for r in result if exclure.lower() not in str(r["ingredients"]).lower()]
    
    result = [r for r in result if r["temps"] <= max_temps]
    result = [r for r in result if r["budget"] <= max_budget]
    
    return result

def afficher_recettes(liste, titre):
    st.header(titre)
    for r in sorted(liste, key=lambda x: x["nom"]):
        budget_total = round(r["budget"] * nb_personnes, 2)
        st.write(f"**{r['nom']}** ({r['saison']})")
        st.write(f"⏱ {r['temps']} min | 💰 {budget_total}€ | 🔥 {r['calories']} kcal | 💪 {r['proteines']}g")
        st.caption(f"Ingrédients : {', '.join(r['ingredients'])}")
        st.write("---")

def generer_liste_courses(menus):
    courses = defaultdict(int)
    for menu in menus:
        for ing in menu["ingredients"]:
            courses[ing] += 1
    return courses

# ==================== NAVIGATION ====================

menu = st.sidebar.radio("Navigation", [
    "Accueil",
    "Entrées",
    "Plats",
    "Desserts",
    "Recherche",
    "Générer des menus",
    "Saisons",
    "Été grosse chaleur",
    "Hiver grand froid",
    "Liste de courses",
    "Planification semaine"
])

# ==================== PAGES ====================

if menu == "Accueil":
    st.header("Bienvenue !")
    st.write("Utilise le menu à gauche pour naviguer.")

elif menu == "Entrées":
    afficher_recettes(filtrer_recettes(entrees), "📋 Entrées")

elif menu == "Plats":
    afficher_recettes(filtrer_recettes(plats), "🍽️ Plats")

elif menu == "Desserts":
    afficher_recettes(filtrer_recettes(desserts), "🍰 Desserts")

elif menu == "Recherche":
    st.header("🔍 Recherche par ingrédient")
    ingredient = st.text_input("Tape un ingrédient")
    if ingredient:
        resultats = [r for r in entrees + plats + desserts if ingredient.lower() in str(r["ingredients"]).lower()]
        for r in resultats:
            st.write(f"- {r['nom']}")

elif menu == "Générer des menus":
    st.header("🎲 Générer des menus")
    nb = st.slider("Nombre de menus", 2, 5, 3)
    if st.button("Générer des menus"):
        menus = random.sample(plats, nb)
        for i, m in enumerate(menus, 1):
            budget = round(m["budget"] * nb_personnes, 2)
            st.success(f"**Menu {i} : {m['nom']}**")
            st.write(f"Temps: {m['temps']} min | Budget: {budget}€ | {m['calories']} kcal")

elif menu == "Saisons":
    st.header("🌱 Menus par saison")
    saison = st.selectbox("Choisis une saison", ["Printemps", "Été", "Automne", "Hiver"])
    tous = entrees + plats + desserts
    resultats = [r for r in tous if r["saison"] == saison]
    for r in resultats:
        st.write(f"- {r['nom']} ({r['type']})")

elif menu == "Été grosse chaleur":
    st.header("☀️ Menus froids d'été")
    froids = [r for r in plats + entrees if r["saison"] == "Été"]
    for r in froids:
        st.write(f"- {r['nom']} ({r['temps']} min)")

elif menu == "Hiver grand froid":
    st.header("❄️ Menus chauds d'hiver")
    chauds = [r for r in plats if r["saison"] == "Hiver"]
    for r in chauds:
        st.write(f"- {r['nom']} ({r['temps']} min)")

elif menu == "Liste de courses":
    st.header("🛒 Liste de courses")
    st.write("Sélectionne des menus pour générer une liste de courses")
    selected = st.multiselect("Choisis des plats", [p["nom"] for p in plats])
    if selected:
        menus_selectionnes = [p for p in plats if p["nom"] in selected]
        courses = generer_liste_courses(menus_selectionnes)
        st.write("**Liste de courses :**")
        for ing, qty in courses.items():
            st.write(f"- {ing} : {qty}")

elif menu == "Planification semaine":
    st.header("📅 Planification sur plusieurs jours")
    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    planning = {}
    for jour in jours:
        planning[jour] = st.selectbox(f"{jour}", ["Aucun"] + [p["nom"] for p in plats], key=jour)
    if st.button("Afficher le planning"):
        for jour, plat in planning.items():
            if plat != "Aucun":
                st.write(f"**{jour}** : {plat}")

st.sidebar.write("---")
st.sidebar.caption("Version très avancée")
