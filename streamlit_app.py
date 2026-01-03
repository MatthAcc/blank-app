import streamlit as st
import pandas as pd

st.set_page_config(page_title="Saga Engine v1.0", layout="wide")

# --- INTERFACE DE PILOTAGE ---
st.title("🏛️ Saga Engine : Atelier de Simulation Sociale")
st.sidebar.header("🕹️ Configuration du Modèle")

# [span_4](start_span)[span_5](start_span)Curseurs de variables[span_4](end_span)[span_5](end_span)
rareté = st.sidebar.slider("Rareté des Ressources (%)", 0, 100, 85)
gouvernance = st.sidebar.selectbox("Régime Politique", ["Technocratie", "Léviathan Algorithmique", "Le Grand Filtre"])

# -[span_6](start_span)-- DASHBOARD DES INDICATEURS[span_6](end_span) ---
st.header("📊 Dashboard du Jumeau Numérique (Tour 10)")
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Performance ($P$)", "50%", "+10%", help="Capacité d'innovation et efficacité.")
with c2:
    st.metric("Cohésion ($I$)", "20%", "-40%", delta_color="inverse", help="Stabilité du lien social.")
with c3:
    st.metric("État du Système", "Singularité", "Alerte")

# --- ONGLETS DE GESTION ---
t1, t2, t3 = st.tabs(["📜 Historique", "👤 Agents", "📝 Export NotebookLM"])

with t1:
    [span_7](start_span)[span_8](start_span)st.subheader("Action Log (Chronologie de la Saga) [cite: 76-82]")
    hist = {"Tour": ["1-3", "4", "5-7", "9-10"], "Phase": ["Survie", "Pax Romana", "Fracture", "Singularité"]}
    st.table(pd.DataFrame(hist))

with t2:
    [cite_start]st.subheader("Matrice des Agents [cite: 71-75]")
    st.write("**Apollon :** Le Tyran (Épure les faibles).")
    st.write("**Hermès :** L'Inquisiteur (Bureaucratie totale).")

with t3:
    [cite_start]st.subheader("Synthèse pour la Bible Dynamique[span_7](end_span)[span_8](end_span)")
    st.info("Copiez ce bloc dans NotebookLM.")
    st.code(f"TOUR 10\nGouvernance: {gouvernance}\nRessources: {rareté}%", language="markdown")
    
