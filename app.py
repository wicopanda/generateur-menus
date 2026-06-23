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
    
    nb_personnes_accueil = st.number_input("Nombre de personnes", min_value=1, max_value=15, value=nb_personnes, key="nb_personnes_accueil")
    
    st.divider()
    
    st.subheader("🔍 Recherche rapide")
    recherche = st.text_input("Tape un ingrédient (ex: tomate)")
    
    if recherche:
        st.write("Fonction recherche à développer plus tard...")
    
    st.divider()
    
    st.subheader("Choisis une catégorie :")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Entrées", use_container_width=True):
            aller_a("Entrées_Choix")
        if st.button("🍽️ Plats", use_container_width=True):
            aller_a("Plats_Choix")
        if st.button("🍰 Desserts", use_container_width=True):
            aller_a("Desserts_Choix")
    
    with col2:
        if st.button("🍟 Petit Plaisir", use_container_width=True):
            aller_a("Petit Plaisir")
        if st.button("🔍 Recherche", use_container_width=True):
            aller_a("Recherche")
        if st.button("🎲 Générer des menus", use_container_width=True):
            aller_a("Générer des menus")
    
    with col3:
        if st.button("🌱 Saisons", use_container_width=True):
            aller_a("Saisons")
        if st.button("🛠️ Générateur personnalisé", use_container_width=True):
            aller_a("Générateur personnalisé")
        if st.button("🛒 Liste de courses", use_container_width=True):
            aller_a("Liste de courses")

# ==================== ENTRÉES ====================
elif st.session_state.page == "Entrées_Choix":
    st.header("📋 Entrées")
    st.write("Choisis le moment du repas :")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("☀️ Midi", use_container_width=True):
            aller_a("Entrées_Midi")
    with col2:
        if st.button("🌙 Soir", use_container_width=True):
            aller_a("Entrées_Soir")
    
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Entrées_Midi":
    st.header("📋 Entrées - Midi")
    st.write("Entrées plus consistantes pour le midi :")
    st.write("- Salade de lentilles")
    st.write("- Velouté de carottes")
    st.write("- Salade de pois chiches")
    if st.button("← Retour"):
        aller_a("Entrées_Choix")

elif st.session_state.page == "Entrées_Soir":
    st.header("📋 Entrées - Soir")
    st.write("Entrées plus légères pour le soir :")
    st.write("- Salade de concombre et yaourt")
    st.write("- Carpaccio de tomates et mozzarella")
    st.write("- Radis et beurre")
    if st.button("← Retour"):
        aller_a("Entrées_Choix")

# ==================== PLATS ====================
elif st.session_state.page == "Plats_Choix":
    st.header("🍽️ Plats")
    st.write("Choisis le moment du repas :")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("☀️ Midi", use_container_width=True):
            aller_a("Plats_Midi")
    with col2:
        if st.button("🌙 Soir", use_container_width=True):
            aller_a("Plats_Soir")
    
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Plats_Midi":
    st.header("🍽️ Plats - Midi")
    st.write("Plats plus consistants pour le midi :")
    st.write("- Pâtes aux courgettes et lardons")
    st.write("- Riz aux légumes et œufs")
    if st.button("← Retour"):
        aller_a("Plats_Choix")

elif st.session_state.page == "Plats_Soir":
    st.header("🍽️ Plats - Soir")
    st.write("Plats plus légers pour le soir :")
    st.write("- Omelette aux légumes d'été")
    st.write("- Poêlée de légumes et saucisses (petite quantité)")
    if st.button("← Retour"):
        aller_a("Plats_Choix")

# ==================== DESSERTS ====================
elif st.session_state.page == "Desserts_Choix":
    st.header("🍰 Desserts")
    st.write("Choisis le moment du repas :")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("☀️ Midi", use_container_width=True):
            aller_a("Desserts_Midi")
    with col2:
        if st.button("🌙 Soir", use_container_width=True):
            aller_a("Desserts_Soir")
    
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Desserts_Midi":
    st.header("🍰 Desserts - Midi")
    st.write("Desserts pour le midi :")
    st.write("- Compote de pommes")
    st.write("- Yaourt aux fraises")
    if st.button("← Retour"):
        aller_a("Desserts_Choix")

elif st.session_state.page == "Desserts_Soir":
    st.header("🍰 Desserts - Soir")
    st.write("Desserts plus légers pour le soir :")
    st.write("- Fromage blanc aux fruits")
    st.write("- Yaourt nature")
    if st.button("← Retour"):
        aller_a("Desserts_Choix")

# ==================== AUTRES PAGES ====================
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

elif st.session_state.page == "Liste de courses":
    st.header("🛒 Liste de courses")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")
