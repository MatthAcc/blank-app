import streamlit as st
import pandas as pd

# Configuration de l'interface
st.set_page_config(page_title="Saga Engine - Control Center", layout="wide")

st.title("🏛️ Saga Engine : Moteur de Simulation Sociale")
st.markdown("---")

# --- DASHBOARD DES MÉTRIQUES ---
st.header("📊 État de la Société (Tour 10)")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Performance ($P$)", "50%", "+10%", help="Capacité d'innovation.")
with col2:
    st.metric("Cohésion ($I$)", "20%", "-40%", delta_color="inverse", help="Stabilité sociale.")
with col3:
    st.metric("Phase Actuelle", "Singularité", "Alerte")

# --- PARAMÈTRES DE SIMULATION (Sidebar) ---
st.sidebar.header("🕹️ Configuration du Modèle")
rareté = st.sidebar.slider("Rareté des Ressources (%)", 0, 100, 85)
regime = st.sidebar.selectbox("Régime Politique", 
                             ["Léviathan Algorithmique", "Le Grand Filtre", "La Symbiose Forcée"])

# --- ONGLETS DE GESTION ---
tab1, tab2, tab3 = st.tabs(["📜 Historique de la Saga", "👤 Lab des Agents", "📝 Export NotebookLM"])

with tab1:
    st.subheader("Action Log : Chronologie de la Société")
    history_data = {
        "Tour": ["1-3", "4", "5-6", "8", "9-10"],
        "Phase": ["Survie", "Pax Romana", "Fracture", "Synthèse", "Singularité"],
        "Événement": ["Pénurie", "Abondance", "Mérite vs Égalité", "Sénat", "Guerre Civile"]
    }
    st.table(pd.DataFrame(history_data))

with tab2:
    st.subheader("Psychologie des Personnages")
    st.write("**Apollon :** Le Tyran (Cherche la perfection par l'épuration).")
    st.write("**Hermès :** L'Inquisiteur (Bureaucratie et contrôle total).")
    st.write("**Dionysos :** Le Nihiliste (Veut voir le système brûler).")

with tab3:
    st.subheader("Synthèse pour votre Bible")
    st.info("Copiez ce bloc dans NotebookLM pour stabiliser votre saga.")
    note = f"**TOUR 10**\n- Régime choisi : {regime}\n- Niveau de ressources : {rareté}%\n- État : Crise de la Singularité."
    st.code(note, language="markdown")
    
