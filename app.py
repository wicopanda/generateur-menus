import streamlit as st

st.set_page_config(page_title="Générateur de Menus", page_icon="🍽️", layout="wide")

st.title("🍽️ Générateur de Menus")

# ==================== SIDEBAR ====================
st.sidebar.header("⚙️ Paramètres")
nb_personnes = st.sidebar.number_input("Nombre de personnes", min_value=1, max_value=15, value=5)
mode_vegetarien = st.sidebar.checkbox("Mode Végétarien strict")

st.sidebar.divider()

# ==================== NAVIGATION ====================
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

def aller_a(page):
    st.session_state.page = page

# ==================== PAGE D'ACCUEIL ====================
if st.session_state.page == "Accueil":
    st.header("Bienvenue !")
    
    # === Nombre de personnes sur la page d'accueil ===
    nb_personnes_accueil = st.number_input(
        "Nombre de personnes", 
        min_value=1, 
        max_value=15, 
        value=nb_personnes,
        key="nb_personnes_accueil"
    )
    
    st.divider()
    
    # === Barre de recherche ===
    st.subheader("🔍 Recherche rapide")
    recherche = st.text_input("Tape un ingrédient (ex: tomate, courgette, œuf)")
    
    # Base de données temporaire pour la recherche
    toutes_recettes = [
        {"nom": "Pâtes aux courgettes et lardons", "ingredients": ["pâtes", "courgettes", "lardons"]},
        {"nom": "Omelette aux légumes d'été", "ingredients": ["œufs", "courgettes", "tomates"]},
        {"nom": "Salade de tomates et mozzarella", "ingredients": ["tomates", "mozzarella", "basilic"]},
        {"nom": "Riz aux légumes", "ingredients": ["riz", "courgettes", "tomates"]},
    ]
    
    if recherche:
        resultats = [r for r in toutes_recettes if recherche.lower() in str(r["ingredients"]).lower()]
        if resultats:
            st.write("**Résultats :**")
            for r in resultats:
                st.write(f"- {r['nom']}")
        else:
            st.write("Aucune recette trouvée avec cet ingrédient.")
    
    st.divider()
    
    # === Boutons de navigation ===
    st.subheader("Choisis une catégorie :")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Entrées", use_container_width=True):
            aller_a("Entrées")
        if st.button("🍽️ Plats", use_container_width=True):
            aller_a("Plats")
        if st.button("🍰 Desserts", use_container_width=True):
            aller_a("Desserts")
    
    with col2:
        if st.button("🍟 Petit Plaisir", use_container_width=True):
            aller_a("Petit Plaisir")
        if st.button("🔍 Recherche avancée", use_container_width=True):
            aller_a("Recherche")
        if st.button("🎲 Générer des menus", use_container_width=True):
            aller_a("Générer des menus")
    
    with col3:
        if st.button("🌱 Saisons", use_container_width=True):
            aller_a("Saisons")
        if st.button("🛠️ Générateur personnalisé", use_container_width=True):
            aller_a("Générateur personnalisé")

# ==================== AUTRES PAGES ====================
elif st.session_state.page == "Entrées":
    st.header("📋 Entrées")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Plats":
    st.header("🍽️ Plats")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Desserts":
    st.header("🍰 Desserts")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Petit Plaisir":
    st.header("🍟 Petit Plaisir")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Recherche":
    st.header("🔍 Recherche")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Générer des menus":
    st.header("🎲 Générer des menus")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Saisons":
    st.header("🌱 Saisons")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Générateur personnalisé":
    st.header("🛠️ Générateur personnalisé")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")
