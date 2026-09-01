import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import uuid

# --- PAGE SETUP ---
st.set_page_config(page_title="SAVYASAACHI PaaS", page_icon="🎯", layout="wide")

st.title("🎯 SAVYASAACHI Enterprise Truth Engine")
st.markdown("### *Multi-Vertical Epistemic Risk & Predictive Isolation Platform*")
st.write("---")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🎛️ Control Panel")
industry = st.sidebar.selectbox(
    "Select Target Vertical", 
    ["ELECTIONS", "MEDIA_MOVIES", "SPORTS_AUCTIONS", "GOVERNMENT_POLICY", "DISASTER_MANAGEMENT", "STARTUP_FINANCIERS"]
)

# --- DYNAMIC CONTEXT FIELDS ---
st.sidebar.write("---")
st.sidebar.header("📝 Target Metadata")

if industry == "ELECTIONS":
    target_name = st.sidebar.text_input("Enter Political Party Name", value="INC")
    party_status = st.sidebar.selectbox("Party Status in Region", ["INCUMBENT (Ruling)", "OPPOSITION / CHALLENGER"])
    demographic_mix = st.sidebar.selectbox("Constituency/State Primary Terrain", ["RURAL-DOMINANT (Agrarian/Tribal)", "URBAN-DOMINANT (Multiplex/Tech-Hubs)"])
    context_focus = st.sidebar.text_input("Enter Election Cycle / Region", value="2028 Karnataka Assembly")
    
elif industry == "MEDIA_MOVIES":
    target_name = st.sidebar.text_input("Enter Movie Title", value="Toxic")
    movie_lang = st.sidebar.text_input("Enter Primary Language(s)", value="Kannada / Multi-Lingual")
    movie_scale = st.sidebar.selectbox("Theatrical Release Scale", ["PAN-WORLD / PAN-INDIA MEGA EPIC", "METRO MULTIPLEX / URBAN TARGETED", "SINGLE-SCREEN MASS / LOCALIZED VENTURE"])
    movie_censor = st.sidebar.selectbox("Thematic / Censor Certification", ["STRICT 'A' CERTIFICATE (Hyper-Violence/Dark Themes)", "U/A or U CERTIFICATE (Family/Clean Entertainment)"])
    context_focus = f"Language: {movie_lang} | Scale: {movie_scale} | Rating: {movie_censor}"

elif industry == "SPORTS_AUCTIONS":
    target_name = st.sidebar.text_input("Enter Athlete / Asset Name", value="Volatile Overseas Star X")
    sport_type = st.sidebar.text_input("Enter Sport & Country Location", value="Cricket / India")
    league_scale = st.sidebar.selectbox("League / Tournament Environment Scale", ["GLOBAL PREMIUM FRANCHISE (High-Purse / Extreme Pressure)", "LOCAL DOMESTIC CIRCUIT (Developmental / Base Valuation)"])
    pitch_profile = st.sidebar.selectbox("Tactical Pitch / Ground Friction Profile", ["SLOW DUSTY TRAPS / HEAVY TURNING SURFACES", "HUMID HIGHWAY PITCHES / FLAT HIGH-SCORE RUNWAYS", "HIGH-ALTITUDE BOUNCE / FAST ACCELERATION GRIDS"])
    context_focus = f"Sport: {sport_type} | League: {league_scale} | Ground: {pitch_profile}"

elif industry == "STARTUP_FINANCIERS":
    target_name = st.sidebar.text_input("Enter Startup Company Name", value="Blinkit")
    startup_market = st.sidebar.text_input("Enter Market Sector & Country", value="Quick-Commerce / India")
    venture_scale = st.sidebar.selectbox("Target Market Scaling Dynamics", ["HYPER-SCALING CONSUMER NETWORK (B2C / High Volatility)", "ENTERPRISE B2B SAAS NICHE (High Contract Value / Low Churn)"])
    burn_trap = st.sidebar.selectbox("Primary Structural Capital Burn Trap", ["HIGH CUSTOMER ACQUISITION COST (CAC Inflation Trap)", "MASSIVE WAREHOUSING / DARK STORE REAL-ESTATE OPERATIONAL LEAKS", "HIGH USER DROP-OFF MATRIX (Weak Retention / Organic Churn)"])
    context_focus = f"Market: {startup_market} | Dynamics: {venture_scale} | Risk: {burn_trap}"
    
elif industry == "GOVERNMENT_POLICY":
    target_name = st.sidebar.text_input("Enter Proposed Policy Scheme", value="No Exam Fee Waiver")
    context_focus = st.sidebar.text_input("Enter Target Demographic Group", value="Rural / Under-30 Youth")
elif industry == "DISASTER_MANAGEMENT":
    target_name = st.sidebar.text_input("Enter Active Disaster Event", value="Nepal Flash Floods")
    context_focus = st.sidebar.text_input("Enter Isolated Topography Node", value="Mountain Ridge Grid-14")

# --- SLIDER TUNING ---
st.sidebar.write("---")
volume = st.sidebar.slider("Incoming Data Volume (Signals)", 1000, 500000, 150000, step=5000)
env_volatility = st.sidebar.slider("Environmental Volatility Index", 0.0, 1.0, 0.75, step=0.05)

st.sidebar.write("---")
st.sidebar.header("🚨 Adversarial Attack Simulator")
noise_score = st.sidebar.slider("Bot / Social Media Manipulation Score", 0.0, 1.0, 0.85, step=0.05)
affirmation_score = st.sidebar.slider("Online Affirmation (Hype / SOS Alerts)", 0.0, 1.0, 0.90, step=0.05)
negation_score = st.sidebar.slider("Online Negation (Review-Bomb / Panic)", 0.0, 1.0, 0.80, step=0.05)

# --- ENGINE PROCESSING CORE ---
dynamic_noise_limit = 0.60 - (env_volatility * 0.15)
is_manipulated = noise_score > dynamic_noise_limit
structural_contradiction = min(affirmation_score, negation_score) * 2.0

# 7-Fold Saptabhaṅgī Decision Routing Logic
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
    if industry == "STARTUP_FINANCIERS":
        st.write(f"**Target Company Asset:** `{target_name.upper()}` | *Market Base:* `{startup_market}`")
        st.write(f"💼 *Context Profile:* `{venture_scale}` | `[{burn_trap}]`")
    elif industry == "SPORTS_AUCTIONS":
        st.write(f"**Target Asset Instance:** `{target_name.upper()}` | *Sport Metric:* `{sport_type}`")
        st.write(f"🏃 *Context Profile:* `{league_scale}` | `[{pitch_profile}]`")
    elif industry == "MEDIA_MOVIES":
        st.write(f"**Target System Instance:** `{target_name.upper()}` | *Language Core:* `{movie_lang}`")
        st.write(f"📊 *Scale Profile:* `{movie_scale}` | `[{movie_censor}]`")
    elif industry == "ELECTIONS":
        st.write(f"**Target System Instance:** `{target_name}` | *Profile:* `{party_status}` | `{demographic_mix}`")
    else:
        st.write(f"**Target System Instance:** `{target_name}` | *Context Profile:* `{context_focus}`")
    
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
        sizes = [5, 95]
        colors = ['#ced4da', '#dc3545']
    elif state == "Syād_Asti_Avaktavyam":
        labels = ['Core Ground Affirmation', 'Unverified Cloud Wrapper']
        sizes = [30, 70]
        colors = ['#28a745', '#dc3545']
    elif state == "Syād_Nasti_Avaktavyam":
        labels = ['Core Ground Negation', 'Unverified Cloud Wrapper']
        sizes = [25, 75]
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

# --- THE STRONGEST AGENDA MODULE ---
st.write("---")
st.subheader("👑 Make the Strongest Agenda with SAVYA SAACHI")
st.markdown("*Let the engine run a multi-dimensional predictive simulation to generate your absolute, un-falsifiable strategy playbook.*")

if st.button("⚡ Generate Strategic Agenda Playbook"):
    st.markdown(f"### 📝 AUTHORITATIVE OPERATIONAL AGENDA FOR: {target_name.upper()}")
    
    if industry == "ELECTIONS":
        st.write(f"*Contextual Focus Area: {context_focus}*")
        if "INCUMBENT" in party_status and "RURAL" in demographic_mix:
            st.success(f"🗳️ **[{target_name.upper()}] Playbook: Rural Incumbency Saturation Blueprint**")
            st.write("1. **Audit the Welfare Inflow Density:** Use the Ground Verification API to cross-reference direct benefit transfers. Your core female cushion must be intensely tracked to block localized male anti-incumbency loops.")
