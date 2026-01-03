import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Saga Engine - Console de Direction", layout="wide")

# --- INITIALISATION DES DONNÉES PAR DÉFAUT ---
if 'state' not in st.session_state:
    st.session_state.state = {
        "P": 92, "I": 100, "Phase": "An 50 : Providence",
        "Regime": "Léviathan Algorithmique",
        "Agents": {"Astraea": "Architecte", "Logos-7": "Médiateur", "Spectre": "Anomalie"},
        "Log": [{"Tour": "10", "Event": "Singularité"}]
    }

# --- ZONE DE MISE À JOUR AUTOMATIQUE ---
with st.sidebar:
    st.header("🔌 Injection de Données")
    raw_input = st.text_area("Collez le rapport de Gemini ici :", height=200)
    if st.button("Actualiser la Simulation"):
        try:
            # L'IA va générer un format JSON caché dans ses réponses
            new_data = json.loads(raw_input)
            st.session_state.state.update(new_data)
            st.success("Système mis à jour !")
        except:
            st.error("Format de rapport non reconnu.")

# --- AFFICHAGE DU DASHBOARD ---
st.title(f"🏛️ {st.session_state.state['Phase']}")
st.markdown(f"**Régime actuel :** {st.session_state.state['Regime']}")

c1, c2 = st.columns(2)
with c1:
    st.metric("Performance ($P$)", f"{st.session_state.state['P']}%")
with c2:
    st.metric("Cohésion ($I$)", f"{st.session_state.state['I']}%")

t1, t2, t3 = st.tabs(["📜 Historique", "👥 Agents", "📝 NotebookLM"])
with t1:
    st.table(pd.DataFrame(st.session_state.state['Log']))
with t2:
    for name, role in st.session_state.state['Agents'].items():
        st.write(f"**{name}** : {role}")
with t3:
    st.code(f"CONCEPT : {st.session_state.state['Phase']}\nImpact P: {st.session_state.state['P']}", language="markdown")
    
