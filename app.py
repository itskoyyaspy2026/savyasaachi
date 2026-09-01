import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import uuid

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

if industry == "ELECTIONS":
    target_name = st.sidebar.text_input("Enter Party Name (e.g., BRS, TVK, BJP)", value="BRS")
    country = st.sidebar.text_input("Country", value="India")
    state_selected = st.sidebar.selectbox("State", ["Telangana", "Tamil Nadu", "West Bengal", "Karnataka", "Andhra Pradesh", "Maharashtra", "Other"])
    election_year = st.sidebar.text_input("Election Year", value="2028")
    region_type = st.sidebar.selectbox("Primary Region Profile", ["RURAL-DOMINANT (Agrarian)", "URBAN-DOMINANT (Multiplex/IT)"])
    party_status = st.sidebar.selectbox("Status", ["INCUMBENT (Ruling)", "OPPOSITION / CHALLENGER"])
    context_focus = f"{election_year} Assembly | {region_type} | {state_selected}, {country}"
    
elif industry == "MEDIA_MOVIES":
    target_name = st.sidebar.text_input("Enter Movie Title", value="Varanasi")
    movie_lang = st.sidebar.text_input("Primary Language", value="Telugu / Multi-Lingual")
    movie_distribution = st.sidebar.selectbox("Release Scale Strategy", ["GLOBAL EPIC", "PAN-INDIA COMMERCIAL", "REGIONAL SPECIFIC"])
    movie_censor = st.sidebar.selectbox("Censor Certificate", ["STRICT 'A' CERTIFICATE (Adult Noir)", "U/A or U CERTIFICATE (Clean Family)"])
    context_focus = f"Language: {movie_lang} | Scale: {movie_distribution} | Censor: {movie_censor}"

elif industry == "SPORTS_AUCTIONS":
    target_name = st.sidebar.text_input("Enter Athlete / Team Name", value="Indian Cricket Team")
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

# Saptabhaṅgī Decision Routing Logic
if is_manipulated and structural_contradiction > 0.5:
    state = "Syād_Avaktavyam"
    action = f"🚨 QUARANTINE ACTIVE: LOCK PREDICTION FOR [{target_name.upper()}] & DEPLOY GROUND API"
    weight_modifier = 0.02
elif affirmation_score >= 0.5 and is_manipulated:
    state = "Syād_Asti_Avaktavyam"
    action = f"⚠️ ISOLATE CORE TRUTH FOR [{target_name.upper()}]: EMBED HIGH UNCERTAINTY ENVELOPE"
    weight_modifier = 0.20
elif negation_score >= 0.5 and is_manipulated:
    state = "Syād_Nasti_Avaktavyam"
    action = f"⚠️ ISOLATE REVERSAL CORE FOR [{target_name.upper()}]: EMBED HIGH UNCERTAINTY ENVELOPE"
    weight_modifier = 0.15
elif affirmation_score >= 0.5 and negation_score >= 0.5:
    state = "Syād_Asti_Nasti"
    action = f"🌗 SPLIT CURRENT SPECTRUM: BIFURCATE TACTICAL STRATEGY CHANNELS FOR [{target_name.upper()}]"
    weight_modifier = 0.50
elif negation_score >= 0.5:
    state = "Syād_Nasti"
    action = f"📉 DOWNWARD WAVE: EXECUTE STRATEGIC DEFENSIVE RESPONSE PROFILE FOR [{target_name.upper()}]"
    weight_modifier = 1.00
else:
    state = "Syād_Asti"
    action = f"📈 UPWARD WAVE: CONSOLIDATE PRIMARY BULLISH VECTOR / STABLE BASE FOR [{target_name.upper()}]"
    weight_modifier = 1.00

computed_mass = volume * weight_modifier

# --- LAYOUT TILES ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔮 Epistemological Status Monitor")
    st.write(f"**Target System Instance:** `{target_name.upper()}`")
    st.write(f"📊 *Matrix Track:* `{context_focus}`")
    
    if state == "Syād_Avaktavyam" or state == "Syād_Nasti":
        st.error(f"Current Standpoint: {state}")
    elif "Avaktavyam" in state:
        st.warning(f"Current Standpoint: {state}")
    else:
        st.success(f"Current Standpoint: {state}")
        
    st.info(f"**Engine Protocol Directives:**\n{action}")
    st.metric(label="Computed Epistemic Data Weight (Clean Mass)", value=f"{int(computed_mass)} units")
    st.metric(label="System Integrity Rating", value="100% Secure" if not is_manipulated else "🚨 ATTACK UNDER QUARANTINE")

with col2:
    st.subheader("📊 Live Bounded Risk Envelope")
    
    fig, ax = plt.subplots(figsize=(5, 3))
    if state == "Syād_Avaktavyam":
        labels = ['Trusted Ground Data', 'Unquantifiable Noise Chaos']
        sizes = [15, 85]
        colors = ['#ced4da', '#dc3545']
    elif state == "Syād_Asti_Avaktavyam":
        labels = ['Core Ground Affirmation', 'Unverified Cloud Wrapper']
        sizes = [65, 35]
        colors = ['#28a745', '#dc3545']
    elif state == "Syād_Nasti_Avaktavyam":
        labels = ['Core Ground Negation', 'Unverified Cloud Wrapper']
        sizes = [60, 40]
        colors = ['#dc3545', '#ced4da']
    elif state == "Syād_Asti_Nasti":
        labels = ['Affirmation (Asti)', 'Negation (Nasti)', 'Residual Noise']
        sizes = [45, 45, 10]
        colors = ['#28a745', '#dc3545', '#ffc107']
    elif state == "Syād_Asti":
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
st.subheader("👑 Execute SAVYASAACHI Predictive Architecture")

if st.button("⚡ Calculate Quantitative Outputs & Strategic Directives"):
    st.markdown(f"## 📝 AUTHORITATIVE ARCHITECTURE REPORT FOR: {target_name.upper()}")
    
    if industry == "ELECTIONS":
        # Dynamic calculation of margins based on simulator variables
        base_margin = 12.5 if state == "Syād_Asti" else (5.2 if state == "Syād_Asti_Nasti" else 2.1)
        calculated_margin = max(0.8, base_margin - (noise_score * 4.0) + (affirmation_score * 3.0))
        
        st.info(f"🧭 **Electoral Matrix Mapping:** Country: `{country}` | State: `{state_selected}` | Party: `{target_name}` | Year: `{election_year}` | Region: `{region_type}`")
        
        st.markdown("### 📊 QUANTITATIVE ENGINE PROJECTIONS:")
        st.metric(label="🎯 Predicted Winning Margin Percentage", value=f"{round(calculated_margin, 2)}% Vote Share Gap")
        
        st.markdown("### 📌 AUTHORITATIVE CAMPAIGN AGENDA:")
        if "TELANGANA" in state_selected.upper() or "BRS" in target_name.upper():
            st.write("• **Map the Regional Welfare vs. Fiscal Deficit Continuum:** Deploy the Ground Verification API to monitor local Rythu Bharosa or water delivery metrics directly at booth levels, bypassing online noise leaks.")
            st.write("• **Isolate the Urban Hyderabad Tech Matrix:** Separate municipal development arguments from rural anti-incumbency layers to lock down middle-class segments.")
        elif "TAMIL" in state_selected.upper() or "TVK" in target_name.upper() or "DMK" in target_name.upper() or "AIADMK" in target_name.upper():
            st.write("• **Isolate the Youth-Aspirational Trend Arc:** Frame core strategic messaging around transparent employment infrastructure and economic mobility to override legacy Dravidian binary constraints.")
