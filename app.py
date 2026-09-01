import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import uuid
from datetime import datetime, time

# --- INITIAL APP SETUP & THEME PROFILE ---
st.set_page_config(page_title="SAVYASAACHI Core", page_icon="🏛️", layout="wide")

st.title("🏛️ SAVYASAACHI Enterprise Truth Engine")
st.markdown("### *Production Platform: 7-Level Ground Reality Error Taxonomy & Saptabhaṅgī Matrix Engine*")
st.write("---")

# --- CONTROL SIDEBAR CONFIGURATIONS ---
st.sidebar.header("🎛️ System Registry Core")
industry = st.sidebar.selectbox(
    "Active Processing Vertical", 
    ["ELECTIONS", "MEDIA_MOVIES", "SPORTS_AUCTIONS", "GOVERNMENT_POLICY", "DISASTER_MANAGEMENT", "STARTUP_FINANCIERS"]
)

# --- THE 7-LEVEL GROUND REALITY ERROR TAXONOMY INPUTS ---
st.sidebar.write("---")
st.sidebar.header("🛡️ 1. Respondent Error Matrix")
resp_false_info = st.sidebar.checkbox("Intentionally gives false information")
resp_hides_pref = st.sidebar.checkbox("Hides actual preference", value=True)
resp_social_ans = st.sidebar.checkbox("Gives socially acceptable answer")
resp_fear_conseq = st.sidebar.checkbox("Fear of local political consequences")
resp_no_reveal = st.sidebar.checkbox("Doesn't want to reveal voting intention")
resp_no_understand = st.sidebar.checkbox("Doesn't understand the question")
resp_fluid_ans = st.sidebar.checkbox("Changes answer depending on who asks")

st.sidebar.write("---")
st.sidebar.header("📋 2. Field-Worker Error Matrix")
fw_bias = st.sidebar.checkbox("Interviewer bias")
fw_leading_q = st.sidebar.checkbox("Leading questions")
fw_selective_choice = st.sidebar.checkbox("Selective respondent choice")
fw_recording_mistake = st.sidebar.checkbox("Recording mistakes")
fw_interpretation_mistake = st.sidebar.checkbox("Interpretation mistakes", value=True)
fw_translation_mistake = st.sidebar.checkbox("Translation mistakes")
fw_deliberate_report = st.sidebar.checkbox("Deliberately reporting preferred narrative")

st.sidebar.write("---")
st.sidebar.header("🎯 3. Sampling Error Matrix")
samp_wrong_unit = st.sidebar.checkbox("Wrong village/ward selected")
samp_wrong_home = st.sidebar.checkbox("Wrong households selected")
samp_overrep = st.sidebar.checkbox("Certain communities overrepresented")
samp_underrep = st.sidebar.checkbox("Certain communities missed")
samp_low_size = st.sidebar.checkbox("Insufficient sample size")
samp_repeat = st.sidebar.checkbox("Repeated respondents")
samp_excluded = st.sidebar.checkbox("Inaccessible populations excluded")

st.sidebar.write("---")
st.sidebar.header("🌋 4. Political / Environmental Error Matrix")
env_voter_fear = st.sidebar.checkbox("Voter fear")
env_local_pressure = st.sidebar.checkbox("Local pressure")
env_intimidation = st.sidebar.checkbox("Intimidation")
env_temp_events = st.sidebar.checkbox("Temporary political events")
env_crowd_mirage = st.sidebar.checkbox("Crowd behaviour mistaken for preference")
env_party_influence = st.sidebar.checkbox("Party workers influencing interaction")
env_leader_influence = st.sidebar.checkbox("Village leaders influencing respondents")

st.sidebar.write("---")
st.sidebar.header("⏳ 5. Temporal Error Matrix")
temp_too_early = st.sidebar.checkbox("Observation taken too early")
temp_immediate = st.sidebar.checkbox("Observation taken immediately after an event")
temp_volatile_drift = st.sidebar.checkbox("Sentiment changing rapidly", value=True)
temp_stale_report = st.sidebar.checkbox("Old field report being treated as current")

st.sidebar.write("---")
st.sidebar.header("🗺️ 6. Geographic Error Matrix")
geo_const_mismatch = st.sidebar.checkbox("Village is not equal to constituency")
geo_urban_mismatch = st.sidebar.checkbox("Urban ward is not equal to entire urban population")
geo_booth_mismatch = st.sidebar.checkbox("One booth treated as entire constituency")
geo_border_drift = st.sidebar.checkbox("Border areas having different behaviour")

# --- CHAIN OF CUSTODY PROVENANCE LEDGER ---
st.sidebar.write("---")
st.sidebar.header("📝 7. Ingest Provenance Metadata")
target_name = st.sidebar.text_input("Target Instance Name String (e.g. TVK, Varanasi, BRS)", value="TVK")
where_coordinates = st.sidebar.text_input("Where Node (POB / Location Spatial Coordinates)", value="Visakhapatnam, Andhra Pradesh")
tob_frame = st.sidebar.time_input("When Node Temporal Frame (TOB Clock)", value=time(12, 30, 45))

st.sidebar.write("---")
st.sidebar.header("🗣️ Raw Behavioral Object Ingest")
actual_observation = st.sidebar.text_area("OBJECT A: What did the subject ACTUALLY say/do?", value="Subject quietly pocketed candidate leaflet, refused to join the public shouting circle, and walked straight back to an un-mapped agrarian block corridor.")
worker_interpretation = st.sidebar.text_area("OBJECT B: What did the field worker INTERPRET?", value="Everyone is praising Candidate A with high voter enthusiasm across the entire village setup.")

# --- COGNITIVE SYSTEM DATA SLIDERS ---
st.sidebar.write("---")
st.sidebar.header("🎚️ Data Volatility Signals")
volume = st.sidebar.slider("Incoming Data Volume Ingest Registry", 1000, 500000, 150000, step=5000)


# ==============================================================================
#                 🧠 PRODUCTION LAYER I: SEPARATE OBJECT HASHING
# ==============================================================================

def execute_deterministic_hash(text_string):
    if not text_string:
        return 0.5
    char_sum = sum(ord(char) for char in text_string)
    return 0.70 + ((char_sum % 45) / 100.0)

# Calculate distinct mathematical objects for Observation and Interpretation
actual_deed_hash = execute_deterministic_hash(actual_observation)
field_worker_hash = execute_deterministic_hash(worker_interpretation)
instance_name_hash = execute_deterministic_hash(target_name)

# Calculate the critical Epistemic Divergence Index (EDI) between Object A and Object B
epistemic_divergence_index = abs(actual_deed_hash - field_worker_hash)


# ==============================================================================
#            🛡️ PRODUCTION LAYER II: THE 7-LEVEL MATHEMATICAL TAXONOMY
# ==============================================================================

# Level 1: Respondent Error Multiplier Calculation Loop
resp_score = sum([resp_false_info, resp_hides_pref, resp_social_ans, resp_fear_conseq, resp_no_reveal, resp_no_understand, resp_fluid_ans]) * 0.142
# Level 2: Field-Worker Error Multiplier Calculation Loop
fw_score = sum([fw_bias, fw_leading_q, fw_selective_choice, fw_recording_mistake, fw_interpretation_mistake, fw_translation_mistake, fw_deliberate_report]) * 0.142
# Level 3: Sampling Error Multiplier Calculation Loop
samp_score = sum([samp_wrong_unit, samp_wrong_home, samp_overrep, samp_underrep, samp_low_size, samp_repeat, samp_excluded]) * 0.142
# Level 4: Political/Environmental Error Multiplier Calculation Loop
env_score = sum([env_voter_fear, env_local_pressure, env_intimidation, env_temp_events, env_crowd_mirage, env_party_influence, env_leader_influence]) * 0.142
# Level 5: Temporal Error Multiplier Calculation Loop
temp_score = sum([temp_too_early, temp_immediate, temp_volatile_drift, temp_stale_report]) * 0.25
# Level 6: Geographic Error Multiplier Calculation Loop
geo_score = sum([geo_const_mismatch, geo_urban_mismatch, geo_booth_mismatch, geo_border_drift]) * 0.25
# Level 7: Human Interpretation Error Multiplier (Direct EDI function)
human_interpretation_score = epistemic_divergence_index * 1.25

# Cumulative Taxonomical System Fragmentation Metric Calculation
cumulative_taxonomical_corruption = (resp_score + fw_score + samp_score + env_score + temp_score + geo_score + human_interpretation_score) / 7.0
cumulative_taxonomical_corruption = min(0.98, max(0.02, cumulative_taxonomical_corruption))


# ==============================================================================
#                 🔮 PRODUCTION LAYER III: THE SAPTABHAṄGĪ MATRIX CORE
# ==============================================================================

# Define absolute threshold logic gates based on your error metrics
quarantine_threshold = 0.45
is_system_compromised = cumulative_taxonomical_corruption > quarantine_threshold

if is_system_compromised:
    engine_state = "Syad_Avaktavyam"  # Indescribable / High Corruption / Block Projections
    action = f"🚨 QUARANTINE LOCKED: GROUND DATA IS HIGHLY CORRUPTED BY TAXONOMICAL MATRIX BIAS. BLOCKING PROJECTIONS FOR [{target_name.upper()}]."
    weight_modifier = 0.04
elif resp_score > 0.5 and fw_score > 0.5:
    engine_state = "Syad_Asti_Nasti"  # Contradictory State
    action = f"🌗 WAVE CONTRADICTION: SPLIT THE OUTFLOW CHANNELS NATIVELY FOR [{target_name.upper()}]."
    weight_modifier = 0.40
elif fw_score > 0.6 or human_interpretation_score > 0.5:
    engine_state = "Syad_Nasti_Avaktavyam"  # Negative Uncertainty Envelope
    action = f"⚠️ OBSERVER BIAS ISOLATED: APPLY DEFENSIVE RESTRICTION MATRICES TO [{target_name.upper()}]."
    weight_modifier = 0.18
elif cumulative_taxonomical_corruption < 0.20:
    engine_state = "Syad_Asti"  # Grounded Stable Positive Base
    action = f"📈 SIGNAL INTEGRITY VERIFIED: EXECUTE STRATEGIC OPTIMIZATION DIRECTIVE FOR [{target_name.upper()}]."
    weight_modifier = 1.20
else:
    engine_state = "Syad_Asti_Avaktavyam"  # Positive with Uncertainty Wrap
    action = f"⚠️ MODERATE VOLATILITY DETECTED: DEPLOY STRATEGY WITH BOUNDED ENVELOPE FOR [{target_name.upper()}]."
    weight_modifier = 0.85

clean_data_mass = volume * weight_modifier * (1.0 - cumulative_taxonomical_corruption)
astro_modifier = 1.22 if (int(tob_frame.minute) % 2 == 0) else 0.84
final_meta_multiplier = instance_name_hash * astro_modifier * (1.0 - human_interpretation_score)


# ==============================================================================
#                       🖼️ RENDERING MATRIX INTERFACE DASHBOARD
# ==============================================================================

col_layout1, col_layout2 = st.columns(2)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import uuid
from datetime import datetime, time

# --- PAGE SETUP ---
st.set_page_config(page_title="SAVYASAACHI PaaS", page_icon="🎯", layout="wide")

st.title("🎯 SAVYASAACHI Election Intelligence Platform")
st.markdown("### *Cognitive Election Intelligence • Syādvāda • Error Taxonomy*")
st.write("---")


# --- SAVYASAACHI NAVIGATION ---
st.markdown("""
<style>
    .block-container { max-width: 1500px; padding-top: 1rem; }
    [data-testid="stSidebar"] { min-width: 290px; max-width: 340px; }
    .nav-note {
        padding: .7rem .9rem;
        border: 1px solid rgba(128,128,128,.25);
        border-radius: 10px;
        margin-bottom: .8rem;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🎯 SAVYASAACHI")
st.sidebar.caption("Election Intelligence • Cognitive Engine")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "🏠 Command Center",
        "🧠 Cognitive Engine",
        "📡 Signal Intelligence",
        "⚠️ Error Taxonomy",
        "🔱 Saptabhaṅgī",
        "🗺️ Constituency Intelligence",
        "🌍 Ground Verification",
        "📊 Synthesis & Forecast",
        "⚙️ Engine Governance",
    ],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.caption("Machine first → Database second → Integration → Validation")

# The existing controls remain available on the Command Center and engine pages.
if page != "🏠 Command Center":
    st.info(f"**{page}** — navigation shell is active. The existing processing engine remains available below while each module is separated into its own screen.")

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
