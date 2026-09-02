import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import uuid
from datetime import datetime, time

# --- STYLISH ENTERPRISE UI BRANDING ENHANCEMENTS ---
st.set_page_config(page_title="SAVYASAACHI Executive Engine", page_icon="🏛️", layout="wide")

# Custom CSS injector to give it a polished, high-fidelity dark-terminal aesthetic
st.markdown("""
    <style>
        .main { background-color: #0d1117; color: #c9d1d9; }
        div.stButton > button:first-child {
            background-color: #238636; color: white; border-radius: 6px; 
            border: 1px solid rgba(240,240,240,0.2); width: 100%; height: 3em; font-weight: bold;
        }
        .metric-card {
            background-color: #161b22; border: 1px solid #30363d; 
            padding: 15px; border-radius: 8px; margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ SAVYASAACHI Enterprise Truth Engine")
st.markdown("🔒 *PaaS Level-1.0 Production Instance | Multi-Vertical Epistemic Risk & Saptabhaṅgī Matrix Matrix*")
st.write("---")

# --- CONTROL SIDEBAR CONFIGURATIONS ---
st.sidebar.header("🎛️ Master Control Panel")
industry = st.sidebar.selectbox(
    "Select Target Industry Vertical", 
    ["ELECTIONS", "MEDIA_MOVIES", "SPORTS_AUCTIONS", "GOVERNMENT_POLICY", "DISASTER_MANAGEMENT", "STARTUP_FINANCIERS"]
)

st.sidebar.write("---")
st.sidebar.subheader("📡 Real-Time Telemetry Signals")
volume = st.sidebar.slider("Incoming Data Volume Ingest Registry", 1000, 500000, 150000, step=5000)
noise_slider = st.sidebar.slider("Ambient Cyber / Cloud Distortion Score", 0.0, 1.0, 0.35, step=0.05)


# ==============================================================================
#                 📥 CENTER MAIN CORE STATE STAGE: METADATA & PROVENANCE
# ==============================================================================

# Organize the setup metadata neatly on screen into visual tabs
setup_tab1, setup_tab2 = st.tabs(["📝 Industry Variant Attributes", "🔍 Ground Observation Provenance"])

with setup_tab1:
    st.markdown("#### Configure Asset DNA Parameters")
    if industry == "ELECTIONS":
        meta_col1, meta_col2, meta_col3 = st.columns(3)
        with meta_col1:
            target_name = st.text_input("State / Region Node Name", value="Andhra Pradesh")
            party_selected = st.text_input("Target Political Party String", value="TVK")
        with meta_col2:
            election_type = st.selectbox("Election Classification Type", ["Assembly Elections", "Lok Sabha Elections", "Bypoll Matrix"])
            number_of_seats = st.slider("Total Number of Seats in State Landscape", 10, 545, 175, step=1)
        with meta_col3:
            election_year = st.text_input("Election Cycle Target Year", value="2026")
            constituency_name = st.text_input("Target Focus Constituency Name", value="Visakhapatnam South")
            
        inner_col1, inner_col2 = st.columns(2)
        with inner_col1:
            const_profile = st.selectbox("Constituency Demographic Core Profile", ["URBAN", "RURAL", "SEMI RURAL", "BC POPULATED", "SC POPULATED", "TRIBAL"])
        with inner_col2:
            state_profile = st.selectbox("Overall State Geographical Dominance Profile", ["urban", "rural", "semi rural", "bc populated", "sc populated", "tribal"])
        context_focus = f"State: {target_name} | Party: {party_selected} | Year: {election_year} | Const Profile: {const_profile}"

    elif industry == "MEDIA_MOVIES":
        meta_col1, meta_col2, meta_col3 = st.columns(3)
        with meta_col1:
            target_name = st.text_input("Movie Production Title String", value="Varanasi")
            production_house = st.text_input("Production Banner Identity", value="Vyjayanthi Movies")
        with meta_col2:
            director_name = st.text_input("Director Core String Name", value="Nag Ashwin")
            movie_budget = st.slider("Allocated Production Budget (₹ Crore)", 10, 600, 250, step=5)
        with meta_col3:
            hero_name = st.text_input("Lead Hero Identity Name Asset", value="Mahesh Babu")
            number_of_screens = st.slider("Number of Screens Deployed Globally", 100, 15000, 4500, step=50)
            
        inner_col1, inner_col2 = st.columns(2)
        with inner_col1:
            movie_lang = st.selectbox("Primary Audio Language Deployment", ["TELUGU", "TAMIL", "KANNADA", "MALAYALAM", "HINDI", "ENGLISH", "MULTI LINGUAL"])
        with inner_col2:
            movie_scale = st.selectbox("Release Scale Strategy Footprint", ["REGIONAL", "PAN INDIA", "GLOBAL"])
        context_focus = f"Lang: {movie_lang} | Scale: {movie_scale} | Screens: {number_of_screens}"

    elif industry == "SPORTS_AUCTIONS":
        meta_col1, meta_col2 = st.columns(2)
        with meta_col1:
            target_name = st.text_input("Country Node Hub Geography", value="India")
            sport_type = st.text_input("Sport Classification Node", value="Cricket")
            match_versus = st.text_input("Match Billing Entry (X vs Y Matrix)", value="India vs Australia")
        with meta_col2:
            arena_stadium = st.text_input("Stadium / Ground Arena Infrastructure Name", value="Narendra Modi Stadium, Ahmedabad")
            weather_month = st.selectbox("Target Month (Weather Calibration Loop)", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            region_geography = st.selectbox("Atmosphere Terrain Geography (Air/Humidity/Temp)", ["HIGH HUMIDITY COASTAL GRID", "DRY ARID DUST PLAINS", "HIGH-ALTITUDE THIN AIR SECTOR"])
        context_focus = f"Match: {match_versus} | Month: {weather_month} | Geography: {region_geography}"

    elif industry == "GOVERNMENT_POLICY":
        target_name = st.text_input("Enter Competitive Exam Name", value="NEET-UG")
        exam_year = st.text_input("Exam Year", value="2026")
        context_focus = f"Exam Matrix: {target_name} | Target Cycle Year: {exam_year}"
    elif industry == "DISASTER_MANAGEMENT":
        target_name = st.text_input("Enter Disaster Type Node", value="Flash Floods")
        state_selected = st.text_input("State Zone Registry Location", value="Bagmati Province")
        context_focus = f"Disaster Variant: {target_name} | Base Zone: {state_selected}"
    elif industry == "STARTUP_FINANCIERS":
        target_name = st.text_input("Enter Startup Profile Name", value="Blinkit")
        startup_market = st.text_input("Market Sector Footprint", value="Quick-Commerce / India")
        burn_trap = st.selectbox("Capital Burn Instability Trap", ["CAC Inflation Trap", "Dark Store Overheads", "Organic User Churn"])
        context_focus = f"Market Venture: {startup_market} | Risk Vector: {burn_trap}"

with setup_tab2:
    st.markdown("#### Ingest Chain of Custody Provenance Data")
    prov_col1, prov_col2 = st.columns(2)
    with prov_col1:
        who_collected = st.selectbox("1. WHO COLLECTED THE FIELD INTEL?", ["Internal Intelligence Cells", "Decentralized Field Workers", "Automated Node Registry", "Third-Party Secondary Audit"])
        how_collected = st.selectbox("2. HOW WAS IT COLLECTED BY CORE NODES?", ["Cryptographic Digital Ledger", "Physical In-Person Manifest", "Encrypted SAT-Phone Terminal", "Mesh-Network Packet Ingest"])
        who_observed = st.text_input("3. SPECIFIC SUBJECT / TARGET DEMOGRAPHIC OBSERVED", value="Target Constituency Demographics Grid-4")
    with prov_col2:
        where_coordinates = st.text_input("4. SPATIAL GEOGRAPHIC COORDINATES (WHERE)", value="Visakhapatnam, Andhra Pradesh")
        when_date = st.date_input("5. TEMPORAL TARGET DATE ANCHOR (WHEN)", value=datetime(1980, 7, 14))
        tob_frame = st.time_input("6. TEMPORAL CLOCK ANCHOR FRAME (TOB)", value=time(0, 30, 45))
        under_conditions = st.selectbox("7. ENVIRONMENTAL AMBIENT CONDITIONS SHIELD", ["High Environmental Volatility", "Normal Parameters", "Adversarial Infiltration Environment", "Sensor/Communication Friction Grid"])


# ==============================================================================
#           🛡️ CENTER MAIN MIDDLE STAGE: PANELS FOR TAXONOMICAL COGNITIVE ERRORS
# ==============================================================================
st.write("---")
st.subheader("🛡️ Integrated 7-Level Ground Reality Error Taxonomy Panels")
st.markdown("*Expand specific layers to simulate tactical ground infrastructure disruptions during the demonstration.*")

# Clear visual layout panels to avoid an overwhelming vertical scrolling experience
with st.expander("📂 Levels 1 & 2: Respondent Bias & Field-Worker Distortion Matrix", expanded=False):
    exp_col1, exp_col2 = st.columns(2)
    with exp_col1:
        st.markdown("**Level-1 Respondent Errors:**")
        r1 = st.checkbox("Intentionally gives false information")
        r2 = st.checkbox("Hides actual preference", value=True)
        r3 = st.checkbox("Gives socially acceptable answer")
        r4 = st.checkbox("Fear of local political consequences")
        r5 = st.checkbox("Doesn't want to reveal voting intention")
        r6 = st.checkbox("Doesn't understand the question")
        r7 = st.checkbox("Changes answer depending on who asks")
    with exp_col2:
        st.markdown("**Level-2 Field-Worker Errors:**")
        f1 = st.checkbox("Interviewer bias")
        f2 = st.checkbox("Leading questions")
        f3 = st.checkbox("Selective respondent choice")
        f4 = st.checkbox("Recording mistakes")
        f5 = st.checkbox("Interpretation mistakes", value=True)
        f6 = st.checkbox("Translation mistakes")
        f7 = st.checkbox("Deliberately reporting preferred narrative")

with st.expander("📂 Levels 3 & 4: Sampling Deficits & Political Environmental Pressures", expanded=False):
    exp_col3, exp_col4 = st.columns(2)
    with exp_col3:
        st.markdown("**Level-3 Sampling Errors:**")
        s1 = st.checkbox("Wrong village/ward selected")
