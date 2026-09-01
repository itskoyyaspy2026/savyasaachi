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

# --- VERTICAL METADATA EXTRA ATTRIBUTES PROFILE ---
st.sidebar.write("---")
st.sidebar.header("📝 Vertical Specific Metadata")
if industry == "ELECTIONS":
    state_selected = st.sidebar.selectbox("State Region", ["Telangana", "Tamil Nadu", "West Bengal", "Karnataka", "Andhra Pradesh", "Maharashtra", "Other"])
    election_year = st.sidebar.text_input("Election Year", value="2026")
    region_type = st.sidebar.selectbox("Constituency Terrain Profile", ["RURAL-DOMINANT (Agrarian)", "URBAN-DOMINANT (Multiplex/IT)"])
elif industry == "MEDIA_MOVIES":
    movie_lang = st.sidebar.text_input("Primary Audio Language", value="Telugu / Multi-Lingual")
    movie_distribution = st.sidebar.selectbox("Release Footprint Scale", ["GLOBAL EPIC", "PAN-INDIA COMMERCIAL", "REGIONAL SPECIFIC"])
    movie_censor = st.sidebar.selectbox("Censor Certification Profile", ["STRICT 'A' CERTIFICATE (Adult Noir)", "U/A or U FAMILY CERTIFICATE"])
elif industry == "SPORTS_AUCTIONS":
    sport_type = st.sidebar.text_input("Sport Node Type", value="Cricket")
    pitch_profile = st.sidebar.selectbox("Tactical Ground Surface Friction", ["SLOW DUSTY TRAPS", "HUMID FLAT RUNWAYS", "HIGH-ALTITUDE BOUNCE"])
elif industry == "GOVERNMENT_POLICY":
    exam_year = st.sidebar.text_input("Examination Targeted Year", value="2026")
elif industry == "DISASTER_MANAGEMENT":
    state_selected = st.sidebar.text_input("State Zone Registry Location", value="Bagmati Province")
elif industry == "STARTUP_FINANCIERS":
    startup_market = st.sidebar.text_input("Market Sector Footprint Niche", value="Quick-Commerce / India")
    burn_trap = st.sidebar.selectbox("Capital Burn Instability Trap Profile", ["CAC Inflation Trap", "Dark Store Overheads", "Organic User Churn"])

st.sidebar.write("---")
st.sidebar.header("🗣️ Raw Behavioral Object Ingest")
actual_observation = st.sidebar.text_area("OBJECT A: What did the subject ACTUALLY say/do?", value="Subject quietly pocketed candidate leaflet, refused to join the public shouting circle, and walked straight back to an un-mapped agrarian block corridor.")
worker_interpretation = st.sidebar.text_area("OBJECT B: What did the field worker INTERPRET?", value="Everyone is praising Candidate A with high voter enthusiasm across the entire village setup.")

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
resp_score = sum([resp_false_info, resp_hides_pref, resp_social_ans, resp_fear_conseq, resp_no_reveal, resp_no_understand, resp_fluid_ans]) * 0.1428
# Level 2: Field-Worker Error Multiplier Calculation Loop
fw_score = sum([fw_bias, fw_leading_q, fw_selective_choice, fw_recording_mistake, fw_interpretation_mistake, fw_translation_mistake, fw_deliberate_report]) * 0.1428
# Level 3: Sampling Error Multiplier Calculation Loop
samp_score = sum([samp_wrong_unit, samp_wrong_home, samp_overrep, samp_underrep, samp_low_size, samp_repeat, samp_excluded]) * 0.1428
# Level 4: Political/Environmental Error Multiplier Calculation Loop
env_score = sum([env_voter_fear, env_local_pressure, env_intimidation, env_temp_events, env_crowd_mirage, env_party_influence, env_leader_influence]) * 0.1428
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

quarantine_threshold = 0.45
is_system_compromised = cumulative_taxonomical_corruption > quarantine_threshold

if is_system_compromised:
    engine_state = "Syad_Avaktavyam"  # Indescribable / High Corruption / Block Projections
