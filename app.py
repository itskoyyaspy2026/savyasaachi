import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, time

# --- INITIAL APP SETUP & THEME PROFILE ---
st.set_page_config(page_title="SAVYASAACHI Core Engine", page_icon="🏛️", layout="wide")

st.markdown("""
    <style>
        .reportview-container .main .block-container { padding-top: 0.2rem !important; padding-bottom: 0.2rem !important; }
        .block-container { padding-top: 0.5rem !important; }
        h1 { margin-top: -1.5rem !important; margin-bottom: 0.1rem !important; font-size: 30px !important; }
        .main { background-color: #0d1117; color: #c9d1d9; }
        div.stButton > button:first-child {
            background-color: #238636; color: white; border-radius: 6px; 
            border: 1px solid rgba(240,240,240,0.2); width: 100%; height: 3em; font-weight: bold; font-size: 16px;
        }
        .metric-card {
            background-color: #161b22; border: 1px solid #30363d; 
            padding: 15px; border-radius: 8px; margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ SAVYASAACHI Enterprise Truth Engine")
st.markdown("🔒 *PaaS Level-1.0 Production Instance | Multi-Vertical Epistemic Risk & Saptabhaṅgī Matrix Engine*")
st.write("---")

# --- CONTROL PANEL SIDEBAR ---
st.sidebar.header("⚙️ Master Control Panel")
industry = st.sidebar.selectbox(
    "Select Target Industry Vertical", 
    ["ELECTIONS", "MEDIA_MOVIES", "SPORTS_AUCTIONS", "GOVERNMENT_POLICY", "DISASTER_MANAGEMENT", "STARTUP_FINANCIERS"]
)

st.sidebar.write("---")
st.sidebar.subheader("📡 Real-Time Telemetry Signals")
volume = st.sidebar.slider("Incoming Data Volume Ingest Registry", 1000, 500000, 150000, step=5000)
noise_slider = st.sidebar.slider("Ambient Cyber / Cloud Distortion Score", 0.0, 1.0, 0.35, step=0.05)

# ==============================================================================
#                 📥 LAYER 1: METADATA EXTRA ATTRIBUTES & PROVENANCE
# ==============================================================================

setup_tab1, setup_tab2 = st.tabs(["📝 Industry Variant Attributes", "🔍 Ground Observation Provenance"])

target_name = "Andhra Pradesh"
party_selected = "YSRCP"

with setup_tab1:
    st.markdown("#### Configure Asset DNA Parameters")
    if industry == "ELECTIONS":
        meta_col1, meta_col2, meta_col3 = st.columns(3)
        with meta_col1:
            target_name = st.text_input("State / Region Node Name", value="Andhra Pradesh")
            party_selected = st.text_input("Target Political Party String", value="YSRCP")
            charismatic_anchor = st.selectbox("Leadership Core Anchor Profile", [
                "Legacy of the Party Founder", "New Mass Hero", "Legacy of Active Leader", "Standard Bureaucratic Alignment"
            ])
        with meta_col2:
            election_type = st.selectbox("Election Classification Type", ["Assembly Elections", "Lok Sabha Elections", "Bypoll Matrix"])
            number_of_seats = st.slider("Total Number of Seats in State Landscape", 10, 545, 175, step=1)
            ideology_shift = st.selectbox("Socio-Ideological Core Paradigm Shift", [
                "Active Search for New Ideology & New Party Birth", "Stable Retention of Legacy Status-Quo", "Fragmented Binary Chaos State"
            ])
        with meta_col3:
            election_year = st.text_input("Election Cycle Target Year", value="2029")
            constituency_name = st.text_input("Target Focus Constituency Name", value="Nuzvid")
            migrant_friction = st.slider("Migrant Labour vs Local Friction Index", 0.0, 1.0, 0.65, step=0.05)

    elif industry == "MEDIA_MOVIES":
        meta_col1, meta_col2, meta_col3 = st.columns(3)
        with meta_col1:
            target_name = st.text_input("Movie Name String", value="Varanasi")
            production_house = st.text_input("Production Banner Identity", value="Vyjayanthi Movies")
        with meta_col2:
            director_name = st.text_input("Director Core String Name", value="Nag Ashwin")
            movie_budget = st.slider("Allocated Production Budget (₹ Crore)", 10, 600, 250, step=5)
        with meta_col3:
            hero_name = st.text_input("Lead Hero Identity Name Asset", value="Mahesh Babu")
            number_of_screens = st.slider("Number of Screens Deployed Globally", 100, 15000, 4500, step=50)

    else:
        target_name = st.text_input("Target Profile / Operation Unit", value="Default Operational Unit")

with setup_tab2:
    st.markdown("#### Ingest Chain of Custody Provenance Data")
    prov_col1, prov_col2 = st.columns(2)
    with prov_col1:
        who_collected = st.selectbox("1. WHO COLLECTED THE FIELD INTEL?", ["Internal Intelligence Cells", "Decentralized Field Workers", "Automated Node Registry", "Third-Party Secondary Audit"])
        how_collected = st.selectbox("2. HOW WAS IT COLLECTED BY CORE NODES?", ["Cryptographic Digital Ledger", "Physical In-Person Manifest", "Encrypted SAT-Phone Terminal", "Mesh-Network Packet Ingest"])
    with prov_col2:
        where_coordinates = st.text_input("4. SPATIAL GEOGRAPHIC COORDINATES (WHERE)", value="Visakhapatnam, Andhra Pradesh")
        when_date = st.date_input("5. TEMPORAL TARGET DATE ANCHOR (WHEN)", value=datetime(2026, 9, 2))

# ==============================================================================
#       🛡️ LAYER 2: CHANNELS FOR THE 7-LEVEL RE-WEIGHTING TAXONOMY
# ==============================================================================
st.write("---")
st.subheader("🛡️ Integrated 7-Level Ground Reality Error Taxonomy Panels")

with st.expander("📂 Levels 1 & 2: Respondent Bias & Field-Worker Distortion Matrix", expanded=True):
    exp_col1, exp_col2 = st.columns(2)
    with exp_col1:
        st.markdown("**Level-1 Respondent Errors:**")
        r1 = st.checkbox("Intentionally gives false information")
        r2 = st.checkbox("Hides actual preference", value=True)
        r3 = st.checkbox("Gives socially acceptable answer")
        r4 = st.checkbox("Fear of local political consequences")
    with exp_col2:
        st.markdown("**Level-2 Field-Worker Errors:**")
        w1 = st.checkbox("Fakes samples / Armchair filling")
        w2 = st.checkbox("Selects convenient easily accessible respondents")
        w3 = st.checkbox("Asks leading / biased questions")

# ==============================================================================
#        ⚡ ENGINE ENGINE CALCULATION & OUTPUT GENERATION (ADDED LOGIC)
# ==============================================================================
st.write("---")

if st.button("🚀 EXECUTE SAPTABHAṄGĪ EPISTEMIC RISK EVALUATION"):
    # Calculate simple distortion index based on error panel selections + sidebar sliders
    resp_distortion = sum([r1, r2, r3, r4]) * 0.12
    worker_distortion = sum([w1, w2, w3]) * 0.15
    total_distortion = min(1.0, resp_distortion + worker_distortion + noise_slider)
    
    confidence_score = max(0.0, 1.0 - total_distortion)
    
    # 7-Fold Jain Epistemic Logic Matrix (Saptabhaṅgī) Calculation
    base_val = 100 - (total_distortion * 100)
    
    saptabhangi_states = {
        "1. Syād-Asti (May be, it is)": round(base_val * 0.85, 2),
        "2. Syād-Nāsti (May be, it is not)": round((100 - base_val) * 0.70, 2),
        "3. Syād-Asti-Nāsti (May be, it is & is not)": round(base_val * 0.40, 2),
        "4. Syād-Avaktavya (May be, it is indescribable)": round(total_distortion * 100, 2),
        "5. Syād-Asti-Avaktavya (May be, it is & indescribable)": round((base_val * 0.3), 2),
        "6. Syād-Nāsti-Avaktavya (May be, it is not & indescribable)": round(((100 - base_val) * 0.3), 2),
        "7. Syād-Asti-Nāsti-Avaktavya (May be, it is, is not & indescribable)": round((total_distortion * 50), 2)
    }
    
    # Render High Level Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Target Asset", target_name)
    with m2:
        st.metric("Raw Ingest Volume", f"{volume:,}")
    with m3:
        st.metric("Taxonomy Distortion Score", f"{total_distortion * 100:.1f}%")
    with m4:
        st.metric("Epistemic Confidence", f"{confidence_score * 100:.1f}%")

    st.write("---")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("### 📊 Saptabhaṅgī Truth Probability Matrix")
        df_matrix = pd.DataFrame(list(saptabhangi_states.items()), columns=["Epistemic Predicate", "Probability Weight Score (%)"])
        st.dataframe(df_matrix, use_container_width=True, hide_index=True)

    with col_right:
        st.markdown("### 📈 Predicate Vector Visualization")
        fig, ax = plt.subplots(figsize=(8, 4.5))
        fig.patch.set_facecolor('#0d1117')
        ax.set_facecolor('#161b22')
        
        y_pos = np.arange(len(saptabhangi_states))
        bars = ax.barh(y_pos, list(saptabhangi_states.values()), color='#238636', edgecolor='#30363d')
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels([k.split(' ')[0] + ' ' + k.split(' ')[1] for k in saptabhangi_states.keys()], color='#c9d1d9')
        ax.invert_yaxis()  
        ax.set_xlabel('Probability Index', color='#c9d1d9')
        ax.tick_params(colors='#c9d1d9')
        
        for spine in ax.spines.values():
            spine.set_color('#30363d')
            
        st.pyplot(fig)
