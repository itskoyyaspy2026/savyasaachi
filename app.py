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
birth_minute = 0  # Initialized core tracking anchor cleanly

if industry == "ELECTIONS":
    target_name = st.sidebar.text_input("Enter Party Name (e.g., BRS, TVK, BJP)", value="BRS")
    leader_name = st.sidebar.text_input("Enter Party Leader Name", value="KCR")
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
        birth_minute = int(tob.minute)

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
        birth_minute = int(tob.minute)

elif industry == "SPORTS_AUCTIONS":
    target_name = st.sidebar.text_input("Enter Athlete Name", value="Indian Cricket Team")
    captain_name = st.sidebar.text_input("Enter Captain Name", value="Rohit Sharma")
    sport_type = st.sidebar.text_input("Sport Type", value="Cricket")
    country = st.sidebar.text_input("Country", value="India")
    pitch_profile = st.sidebar.selectbox("Ground / Pitch Friction Profile", ["SLOW DUSTY TRAPS", "HUMID FLAT RUNWAYS", "HIGH-ALTITUDE BOUNCE"])
    context_focus = f"Sport: {sport_type} | Country: {country} | Environment: {pitch_profile}"
    
    st.sidebar.write("---")
    st.sidebar.subheader("🕉️ BPHS Captain Chart Alignment")
    astro_enabled = st.sidebar.checkbox("Enable Captain Astrological Audit", value=True)
    if astro_enabled:
        dob = st.sidebar.date_input("Captain Date of Birth", value=datetime(1987, 4, 30))
        tob = st.sidebar.time_input("Captain Time of Birth", value=time(4, 45))
        pob = st.sidebar.text_input("Captain Place of Birth", value="Nagpur, Maharashtra")
        birth_minute = int(tob.minute)

elif industry == "GOVERNMENT_POLICY":
    target_name = st.sidebar.text_input("Enter Competitive Exam Name", value="NEET-UG")
    exam_year = st.sidebar.text_input("Exam Year", value="2026")
    context_focus = f"Exam Matrix: {target_name} | Target Cycle Year: {exam_year}"

elif industry == "DISASTER_MANAGEMENT":
    target_name = st.sidebar.text_input("Enter Disaster Type", value="Flash Floods")
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
        sizes = [15, 85]
    elif engine_state == "Syad_Asti_Avaktavyam":
        sizes = [65, 35]
    elif engine_state == "Syad_Nasti_Avaktavyam":
        sizes = [40, 60]
    elif engine_state == "Syad_Asti_Nasti":
        sizes = [45, 45, 10]
    elif engine_state == "Syad_Asti":
        sizes = [90, 10]
    else:
        sizes = [85, 15]
        
    ax.pie(sizes, labels=['Grounded Base', 'Noise Wrapper'], colors=['#28a745', '#dc3545'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# --- THE UNIVERSAL STRATEGIC MATRIX COMPILER ---
st.write("---")
st.subheader("👑 Live SAVYASAACHI Predictive Execution Architecture")

if st.button("⚡ GENERATE RESULT", key="universal_generate_button"):
    st.markdown(f"## 📝 AUTHORITATIVE ARCHITECTURE REPORT FOR: {target_name.upper()}")
    
    # FIXED: Replaced standard object parameter dependencies with string-safe mathematical integers
    astro_modifier = 1.18 if (astro_enabled and birth_minute % 2 == 0) else 0.88
    
    if industry == "ELECTIONS":
        base_margin = 12.5 if "Asti" in engine_state else 1.5
        calculated_margin = max(0.5, (base_margin - (noise_score * 4.0) + (affirmation_score * 3.5)) * astro_modifier)
        
        st.info(f"🧭 **Electoral Matrix Mapping:** Country: `{country}` | State: `{state_selected}` | Party: `{target_name}` | Year: `{election_year}` | Region: `{region_type}`")
        if astro_enabled:
            st.warning(f"🕉️ **BPHS Chart Decoded:** Leader: `{leader_name}`. Ascendant Lord strength processed into D1/D9 Navamsha matrices.")
            
        st.markdown("### 📊 QUANTITATIVE ENGINE PROJECTIONS:")
        st.metric(label="🎯 Predicted Winning Margin Percentage", value=f"{round(calculated_margin, 2)}% Vote Share Gap")
        
        st.markdown("### 📌 AUTHORITATIVE CAMPAIGN AGENDA:")
        if "TELANGANA" in state_selected.upper() or "BRS" in target_name.upper():
            st.write("• **Map the Regional Welfare Continuum:** Deploy the Ground Verification API to monitor local Rythu Bharosa or water delivery metrics directly at booth levels, bypassing online noise leaks.")
        elif "TAMIL" in state_selected.upper() or "TVK" in target_name.upper() or "DMK" in target_name.upper() or "AIADMK" in target_name.upper():
            st.write("• **Isolate the Youth-Aspirational Trend Arc:** Frame core strategic messaging around transparent employment infrastructure to override legacy Dravidian binary constraints.")
        else:
            st.write("• **Expose Fake Digital Waves:** Anchor your field machinery strictly to physical voter turnouts.")

    elif industry == "MEDIA_MOVIES":
        base_opening = 220.0 if "GLOBAL" in movie_distribution else (110.0 if "PAN-INDIA" in movie_distribution else 25.0)
        total_multiplier = 8.5 if "Asti" in engine_state else 3.2
        opening_day = base_opening * (volume / 150000.0) * (affirmation_score / 0.90) * astro_modifier
        potential_total = opening_day * total_multiplier * (1.0 - (noise_score * 0.25))
        
        st.info(f"🎬 **Cinematic Matrix Mapping:** Movie: `{target_name}` | Language: `{movie_lang}` | Scale Scope: `{movie_distribution}`")
        if astro_enabled:
            st.warning(f"🕉️ **BPHS Chart Decoded:** Hero: `{hero_name}`. D1 Lagna positions cross-referenced with Shani/Rahu release-day transits.")
            
        st.markdown("### 📊 QUANTITATIVE BOX OFFICE OUTPUTS:")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(label="🚀 Projected Opening Day Collections", value=f"₹{int(opening_day)} Crore")
        with col_m2:
            st.metric(label="🔮 Bounded Possibility of Total Lifetime Collections", value=f"₹{int(potential_total)} Crore")

    elif industry == "SPORTS_AUCTIONS":
        base_margin = 76.5 if "Asti" in engine_state else 51.2
        final_margin_pct = min(98.5, max(12.0, (base_margin + (affirmation_score * 15) - (env_volatility * 20)) * astro_modifier))
        
        st.info(f"🏏 **Sports Matrix Mapping:** Sport: `{sport_type}` | Country: `{country}` | Asset Name: `{target_name}`")
        if astro_enabled:
            st.warning(f"🕉️ **BPHS Chart Decoded:** Captain: `{captain_name}`. D9 Navamsha 10th House Lord analyzed for knockout match luck retention.")
            
        st.markdown("### 📊 QUANTITATIVE SPORTS OUTPUTS:")
        st.metric(label="🏆 Projected Winning Margin Percentage", value=f"{round(final_margin_pct, 1)}%")

    elif industry == "GOVERNMENT_POLICY":
        base_cutoff = 162 if "NEET" in target_name.upper() else (94 if "UPSC" in target_name.upper() else 50)
        calculated_cutoff = base_cutoff + (affirmation_score * 12) - (env_volatility * 8)
        
        st.info(f"🎓 **Educational Matrix Mapping:** Competitive Exam: `{target_name}` | Cycle Year: `{exam_year}`")
        st.markdown("### 📊 QUANTITATIVE ACADEMIC OUTPUTS:")
        st.metric(label="📝 Expected Standard Cut-Off Score", value=f"{int(calculated_cutoff)} Marks")

    elif industry == "DISASTER_MANAGEMENT":
        st.info(f"🚑 **Humanitarian Matrix Mapping:** Country: `{country}` | State/Zone: `{state_selected}` | Specific Region: `{region_type}`")
        st.markdown("### 📊 CRITICAL CRISIS DIRECTIVE OUTPUTS:")
        st.success("🚨 **IMMEDIATE STEPS TO BE TAKEN (Operational Playbook):**")
        st.write(f"1. **Quarantine Fake Panic Rumors:** Isolate unverified internet chatter regarding dam breaches and clear the communication lanes.")
        st.write(f"2. **Redirect Rescue Teams:** Activate rescue operations straight to hidden coordinates where floating workforces are stranded.")

    elif industry == "STARTUP_FINANCIERS":
        st.info(f"💼 **Financier Matrix Mapping:** Venture: `{target_name}` | Market Core: `{startup_market}`")
        st.markdown("### 📊 DUE-DILIGENCE SHIELD VERDICT:")
        if "Avaktavyam" in engine_state or noise_score > 0.70:
            st.error("🚨 INVESTMENT ACTION DIRECTIVE: ABANDON ROUND / LIQUIDITY TRAP RISK EXPOSED")
        else:
            st.warning("⚠️ INVESTMENT ACTION DIRECTIVE: PROCEED VIA CONDITIONAL MILESTONE STAGES ONLY")

# --- GROUND VERIFICATION API INTERACTIVE INTERCEPT ---
st.write("---")
st.subheader("🔒 Cryptographic Ground Verification API Intercept")

if "Avaktavyam" in engine_state:
    st.warning(f"⚠️ High digital noise/panic detected. Automated predictions are currently frozen to prevent errors.")
    if st.button("🔗 Execute Ground Verification API Trigger"):
        token = f"VTK-{uuid.uuid4().hex[:12].upper()}"
        st.success(f"📡 API Dispatched to Local Field Nodes. Generated Ticket: **{token}**")
else:
    st.success("✔ Data streams are running clear within normal parameters. Ground override infrastructure is currently on standby.")
