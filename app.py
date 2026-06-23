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
    st.rerun()

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

    st.divider()
    
    # === NOUVEAUX BOUTONS SPÉCIAUX ===
    st.subheader("Sections spéciales :")
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        if st.button("❄️ Plat froid spéciale Été", use_container_width=True):
            aller_a("Ete_Froid")
    
    with col5:
        if st.button("🔥 Grand chaud spéciale Hiver", use_container_width=True):
            aller_a("Hiver_Chaud")
    
    with col6:
        if st.button("🥬 Végétarien", use_container_width=True):
            aller_a("Vegetarien")

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
    st.write("Les entrées adaptées pour le midi apparaîtront ici.")
    if st.button("← Retour"):
        aller_a("Entrées_Choix")

elif st.session_state.page == "Entrées_Soir":
    st.header("📋 Entrées - Soir")
    st.write("Les entrées adaptées pour le soir apparaîtront ici.")
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
    st.write("Les plats adaptés pour le midi apparaîtront ici.")
    if st.button("← Retour"):
        aller_a("Plats_Choix")

elif st.session_state.page == "Plats_Soir":
    st.header("🍽️ Plats - Soir")
    st.write("Les plats adaptés pour le soir apparaîtront ici.")
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
    st.write("Les desserts adaptés pour le midi apparaîtront ici.")
    if st.button("← Retour"):
        aller_a("Desserts_Choix")

elif st.session_state.page == "Desserts_Soir":
    st.header("🍰 Desserts - Soir")
    st.write("Les desserts adaptés pour le soir apparaîtront ici.")
    if st.button("← Retour"):
        aller_a("Desserts_Choix")

# ==================== NOUVELLES PAGES SPÉCIALES ====================
elif st.session_state.page == "Ete_Froid":
    st.header("❄️ Plat froid spéciale Été")
    st.write("Ici apparaîtront les plats froids pour l'été.")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Hiver_Chaud":
    st.header("🔥 Grand chaud spéciale Hiver")
    st.write("Ici apparaîtront les plats chauds pour l'hiver.")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

elif st.session_state.page == "Vegetarien":
    st.header("🥬 Mode Végétarien")
    st.write("Ici apparaîtront uniquement les recettes végétariennes.")
    if st.button("← Retour à l'accueil"):
        aller_a("Accueil")

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
