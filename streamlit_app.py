import streamlit as st
import pandas as pd

st.set_page_config(page_title="Saga Engine", layout="wide")

st.title("🏛️ Saga Engine : Contrôle de Simulation")

# --- PARAMÈTRES (Sidebar) ---
st.sidebar.header("🕹️ Configuration")
rareté = st.sidebar.slider("Rareté des Ressources (%)", 0, 100, 85)
regime = st.sidebar.selectbox("Régime", ["Léviathan Algorithmique", "Grand Filtre", "Symbiose Forcée"])

# --- DASHBOARD ---
c1, c2 = st.columns(2)
with c1:
    st.metric("Performance ($P$)", "50%", "+10%")
with c2:
    st.metric("Cohésion ($I$)", "20%", "-40%")

# --- ONGLETS ---
t1, t2, t3 = st.tabs(["📜 Histoire", "👤 Agents", "📝 NotebookLM"])

with t1:
    st.subheader("Chronologie de la Saga")
    hist = {"Tour": ["1-3", "4", "5-6", "8", "9-10"], 
            "Phase": ["Survie", "Pax Romana", "Fracture", "Synthèse", "Singularité"]}
    st.table(pd.DataFrame(hist))

with t2:
    st.subheader("Profils des Agents")
    [span_1](start_span)st.write("**Apollon :** Le Tyran[span_1](end_span)")
    [span_2](start_span)st.write("**Hermès :** L'Inquisiteur[span_2](end_span)")

with t3:
    st.subheader("Export NotebookLM")
    st.code(f"TOUR 10\nRegime: {regime}\nRareté: {rareté}%")
    
