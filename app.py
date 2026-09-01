import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import uuid
from datetime import datetime, time

# --- PAGE SETUP ---
st.set_page_config(page_title="SAVYASAACHI PaaS", page_icon="🎯", layout="wide")

st.title("🎯 SAVYASAACHI Enterprise Truth Engine")
st.markdown("### *Multi-Vertical Epistemic Risk & Quantitative Projections Platform*")
st.write("---")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🎛️ Control Panel")
industry = st.sidebar.selectbox(
    "Select Target Vertical", 
    ["ELECTIONS", "MEDIA_MOVIES", "SPORTS_AUCTIONS", "GOVERNMENT_POLICY", "DISASTER_MANAGEMENT", "STARTUP_FINANCIERS"]
)

# --- DYNAMIC MATRIX INPUT FIELDS ---
st.sidebar.write("---")
st.sidebar.header("📝 Target Metadata Inputs")

astro_enabled = False

if industry == "ELECTIONS":
    target_name = st.sidebar.text_input("Enter Party Name (e.g., BRS, TVK, BJP)", value="BRS")
    leader_name = st.sidebar.text_input("Enter Leader Name", value="KCR")
    country = st.sidebar.text_input("Country", value="India")
    state_selected = st.sidebar.selectbox("State", ["Telangana", "Tamil Nadu", "West Bengal", "Karnataka", "Andhra Pradesh", "Maharashtra", "Other"])
    election_year = st.sidebar.text_input("Election Year", value="2028")
    region_type = st.sidebar.selectbox("Primary Region Profile", ["RURAL-DOMINANT (Agrarian)", "URBAN-DOMINANT (Multiplex/IT)"])
    party_status = st.sidebar.selectbox("Status", ["INCUMBENT (Ruling)", "OPPOSITION / CHALLENGER"])
    context_focus = f"{election_year} Assembly | {region_type} | {state_selected}, {country}"
    
    st.sidebar.write("---")
    st.sidebar.subheader("🕉️ BPHS Leader Chart Alignment")
    astro_enabled = st.sidebar.checkbox("Enable Leader Astrological Audit", value=True)
    if astro_enabled:
        dob = st.sidebar.date_input("Leader Date of Birth", value=datetime(1954, 2, 17))
        tob = st.sidebar.time_input("Leader Time of Birth", value=time(10, 30))
        pob = st.sidebar.text_input("Leader Place of Birth", value="Chintamadaka, Telangana")
    
elif industry == "MEDIA_MOVIES":
    target_name = st.sidebar.text_input("Enter Movie Title", value="Varanasi")
    hero_name = st.sidebar.text_input("Enter Lead Hero Name", value="Mahesh Babu")
    movie_lang = st.sidebar.text_input("Primary Language", value="Telugu / Multi-Lingual")
    movie_distribution = st.sidebar.selectbox("Release Scale Strategy", ["GLOBAL EPIC", "PAN-INDIA COMMERCIAL", "REGIONAL SPECIFIC"])
    movie_censor = st.sidebar.selectbox("Censor Certificate", ["STRICT 'A' CERTIFICATE (Adult Noir)", "U/A or U CERTIFICATE (Clean Family)"])
    context_focus = f"Language: {movie_lang} | Scale: {movie_distribution} | Censor: {movie_censor}"

    st.sidebar.write("---")
    st.sidebar.subheader("🕉️ BPHS Hero Chart Alignment")
    astro_enabled = st.sidebar.checkbox("Enable Hero Astrological Audit", value=True)
    if astro_enabled:
        dob = st.sidebar.date_input("Hero Date of Birth", value=datetime(1975, 8, 9))
        tob = st.sidebar.time_input("Hero Time of Birth", value=time(18, 22))
        pob = st.sidebar.text_input("Hero Place of Birth", value="Chennai, Tamil Nadu")

elif industry == "SPORTS_AUCTIONS":
    target_name = st.sidebar.text_input("Enter Athlete / Team Name", value="Indian Cricket Team")
    captain_name = st.sidebar.text_input("Enter Captain Name", value="Rohit Sharma")
    sport_type = st.sidebar.text_input("Sport Type", value="Cricket")
    country = st.sidebar.text_input("Country Hub", value="India")
    pitch_profile = st.sidebar.selectbox("Ground / Pitch Friction Profile", ["SLOW DUSTY TRAPS", "HUMID FLAT RUNWAYS", "HIGH-ALTITUDE BOUNCE"])
    context_focus = f"Sport: {sport_type} | Country: {country} | Environment: {pitch_profile}"

elif industry == "GOVERNMENT_POLICY":
    target_name = st.sidebar.text_input("Enter Competitive Exam Name (e.g., NEET, UPSC)", value="NEET-UG")
    exam_year = st.sidebar.text_input("Exam Year", value="2026")
    context_focus = f"Exam Matrix: {target_name} | Target Cycle Year: {exam_year}"

elif industry == "DISASTER_MANAGEMENT":
    target_name = st.sidebar.text_input("Enter Disaster Type (e.g., Flash Floods, Cyclone)", value="Flash Floods")
    country = st.sidebar.text_input("Country", value="Nepal")
    state_selected = st.sidebar.text_input("State / Zone", value="Bagmati Province")
    region_type = st.sidebar.text_input("Specific Region Coordinates", value="Kavre Mountainside Grid-14")
    context_focus = f"Disaster: {target_name} | Location: {region_type}, {state_selected}, {country}"

elif industry == "STARTUP_FINANCIERS":
    target_name = st.sidebar.text_input("Enter Startup Name", value="Blinkit")
    startup_market = st.sidebar.text_input("Market Sector & Country", value="Quick-Commerce / India")
    burn_trap = st.sidebar.selectbox("Primary Capital Burn Trap", ["CAC Inflation Trap", "Dark Store Real-Estate Overhead", "Organic User Churn"])
    context_focus = f"Market: {startup_market} | Primary Core Risk: {burn_trap}"

# --- SLIDER TUNING ---
st.sidebar.write("---")
volume = st.sidebar.slider("Incoming Data Volume (Signals)", 1000, 500000, 150000, step=5000)
env_volatility = st.sidebar.slider("Environmental Volatility Index", 0.0, 1.0, 0.75, step=0.05)

st.sidebar.write("---")
st.sidebar.header("🚨 Adversarial Attack Simulator")
noise_score = st.sidebar.slider("Bot / Social Media Manipulation Score", 0.0, 1.0, 0.85, step=0.05)
affirmation_score = st.sidebar.slider("Online Affirmation (Hype / SOS)", 0.0, 1.0, 0.90, step=0.05)
negation_score = st.sidebar.slider("Online Negation (Review-Bomb / Panic)", 0.0, 1.0, 0.80, step=0.05)

# --- ENGINE PROCESSING CORE ---
dynamic_noise_limit = 0.60 - (env_volatility * 0.15)
is_manipulated = noise_score > dynamic_noise_limit
structural_contradiction = min(affirmation_score, negation_score) * 2.0

# 7-Fold Saptabhangi Decision Routing Logic (Cleaned of special characters to fix routing breaks)
if is_manipulated and structural_contradiction > 0.5:
    engine_state = "Syad_Avaktavyam"
    action = f"🚨 QUARANTINE ACTIVE: LOCK PREDICTION FOR [{target_name.upper()}] & DEPLOY GROUND API"
    weight_modifier = 0.02
elif affirmation_score >= 0.5 and is_manipulated:
    engine_state = "Syad_Asti_Avaktavyam"
    action = f"⚠️ ISOLATE CORE TRUTH FOR [{target_name.upper()}]: EMBED HIGH UNCERTAINTY ENVELOPE"
    weight_modifier = 0.20
elif negation_score >= 0.5 and is_manipulated:
    engine_state = "Syad_Nasti_Avaktavyam"
    action = f"⚠️ ISOLATE REVERSAL CORE FOR [{target_name.upper()}]: EMBED HIGH UNCERTAINTY ENVELOPE"
    weight_modifier = 0.15
elif affirmation_score >= 0.5 and negation_score >= 0.5:
    engine_state = "Syad_Asti_Nasti"
    action = f"🌗 SPLIT CURRENT SPECTRUM: BIFURCATE TACTICAL STRATEGY CHANNELS FOR [{target_name.upper()}]"
    weight_modifier = 0.50
elif negation_score >= 0.5:
    engine_state = "Syad_Nasti"
    action = f"📉 DOWNWARD WAVE: EXECUTE STRATEGIC DEFENSIVE RESPONSE PROFILE FOR [{target_name.upper()}]"
    weight_modifier = 1.00
else:
    engine_state = "Syad_Asti"
    action = f"📈 UPWARD WAVE: CONSOLIDATE PRIMARY BULLISH VECTOR / STABLE BASE FOR [{target_name.upper()}]"
    weight_modifier = 1.00

computed_mass = volume * weight_modifier

# --- LAYOUT TILES ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔮 Epistemological Status Monitor")
    st.write(f"**Target System Instance:** `{target_name.upper()}`")
    st.write(f"📊 *Matrix Track:* `{context_focus}`")
    
    if engine_state == "Syad_Avaktavyam" or engine_state == "Syad_Nasti":
        st.error(f"Current Standpoint: {engine_state}")
    elif "Avaktavyam" in engine_state:
        st.warning(f"Current Standpoint: {engine_state}")
    else:
        st.success(f"Current Standpoint: {engine_state}")
        
    st.info(f"**Engine Protocol Directives:**\n{action}")
    st.metric(label="Computed Epistemic Data Weight (Clean Mass)", value=f"{int(computed_mass)} units")
    st.metric(label="System Integrity Rating", value="100% Secure" if not is_manipulated else "🚨 ATTACK UNDER QUARANTINE")

with col2:
    st.subheader("📊 Live Bounded Risk Envelope")
    
    fig, ax = plt.subplots(figsize=(5, 3))
    if engine_state == "Syad_Avaktavyam":
        labels = ['Trusted Ground Data', 'Unquantifiable Noise Chaos']
        sizes = [15, 85]
        colors = ['#ced4da', '#dc3545']
    elif engine_state == "Syad_Asti_Avaktavyam":
        labels = ['Core Ground Affirmation', 'Unverified Cloud Wrapper']
        sizes = [65, 35]
        colors = ['#28a745', '#dc3545']
    elif engine_state == "Syad_Nasti_Avaktavyam":
        labels = ['Core Ground Negation', 'Unverified Cloud Wrapper']
        sizes = [60, 40]
        colors = ['#dc3545', '#ced4da']
    elif engine_state == "Syad_Asti_Nasti":
        labels = ['Affirmation (Asti)', 'Negation (Nasti)', 'Residual Noise']
        sizes = [45, 45, 10]
        colors = ['#28a745', '#dc3545', '#ffc107']
    elif engine_state == "Syad_Asti":
        labels = ['Grounded Affirmation Base', 'System Noise Floor']
        sizes = [90, 10]
        colors = ['#28a745', '#ced4da']
    else:
        labels = ['Grounded Negation Base', 'System Noise Floor']
        sizes = [85, 15]
        colors = ['#dc3545', '#ced4da']
        
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# --- THE UNIVERSAL STRATEGIC MATRIX COMPILER ---
st.write("---")
st.subheader("👑 Live SAVYASAACHI Predictive Execution Architecture")
st.markdown(f"## 📝 AUTHORITATIVE ARCHITECTURE REPORT FOR: {target_name.upper()}")

# Calculate simulated Astrological modifier based on birth hour/minute parity
astro_modifier = 1.18 if (astro_enabled and int(tob.minute) % 2 == 0) else 0.88

if industry == "ELECTIONS":
    base_margin = 12.5 if "Asti" in engine_state else 1.5
    calculated_margin = max(0.5, (base_margin - (noise_score * 4.0) + (affirmation_score * 3.5)) * astro_modifier)
    
