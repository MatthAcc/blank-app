import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Saga Engine - Control Center", layout="wide")

st.title("🏛️ Saga Engine : Moteur de Simulation & Jumeau Numérique")
st.markdown("---")

# --- DASHBOARD DES MÉTRIQUES SYSTÉMIQUES ---
# [span_0](start_span)Variables basées sur vos métriques de simulation[span_0](end_span)
st.header("📊 État de la Société (Tour 10)")
col1, col2, col3 = st.columns(3)
with col1:
    [span_1](start_span)st.metric("Performance ($P$)", "50%", "+10%", help="Capacité d'innovation et innovation technologique[span_1](end_span).")
with col2:
    [span_2](start_span)st.metric("Cohésion ($I$)", "20%", "-40%", delta_color="inverse", help="Stabilité du lien social et résilience[span_2](end_span).")
with col3:
    st.metric("Statut", "Singularité", "Alerte")

# --- CONTRÔLE DE LA SIMULATION (Sidebar) ---
# [span_3](start_span)[span_4](start_span)Paramètres et curseurs de gouvernance[span_3](end_span)[span_4](end_span)
st.sidebar.header("🕹️ Configuration du Modèle")
rareté = st.sidebar.slider("Rareté des Ressources (%)", 0, 100, 85)
régime = st.sidebar.selectbox("Stratégie Planétaire Radicale", 
                             ["Léviathan Algorithmique (IA)", "Le Grand Filtre (Décroissance)", "La Symbiose Forcée (Transhumanisme)"])

# --- CONTENU INTERACTIF ---
tab1, tab2, tab3 = st.tabs(["📜 Historique de la Saga", "👤 Lab des Personnages", "📝 Export NotebookLM"])

with tab1:
    [span_5](start_span)st.subheader("Chronologie de la Simulation [cite: 76-82]")
    history_data = {
        "Tour": ["1-3", "4", "5-6", "8", "9-10"],
        "Phase": ["Survie", "Pax Romana", "Fracture", "Synthèse", "Singularité"],
        "Événement": ["Pénurie créatrice", "Pain et Jeux", "Mérite vs Égalité", "Sénat", "Guerre Civile"]
    }
    st.table(pd.DataFrame(history_data))

with tab2:
    [cite_start]st.subheader("État Psychologique des Agents [cite: 71-75]")
    [cite_start]st.write("**Apollon (Le Tyran) :** Épure les 'faibles'[span_5](end_span).")
    [span_6](start_span)st.write("**Hermès (L'Inquisiteur) :** Bureaucratie et surveillance totale[span_6](end_span).")
    [span_7](start_span)st.write("**Dionysos (Le Nihiliste) :** Veut voir le système brûler[span_7](end_span).")

with tab3:
    st.subheader("Synthèse pour la Bible Dynamique")
    [span_8](start_span)st.info("Copiez ce bloc dans NotebookLM pour stabiliser votre saga[span_8](end_span).")
    note = f"**TOUR 10 : ÉTAT DES LIEUX**\n- **Stratégie choisie :** {régime}\n- **Ressources :** {rareté}%\n- **Observation :** Transition vers le Tome 2."
    st.code(note, language="markdown")
