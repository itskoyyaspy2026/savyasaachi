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
st.markdown("🔒 *PaaS Level-1.0 Production Instance | Multi-Vertical Epistemic Risk Matrix Engine*")
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

target_name = ""
party_selected = ""
election_year = "2029"
const_profile = "RURAL"
state_profile = "rural"
constituency_name = "Nuzvid"
number_of_seats = 175
charismatic_anchor = ""
ideology_shift = ""
migrant_friction = 0.5
election_type = "Assembly Elections"

movie_budget = 250
production_house = ""
director_name = ""
hero_name = ""
number_of_screens = 4500
movie_lang = "TELUGU"
movie_scale = "PAN INDIA"

country_name = "India"
sport_type = "Cricket"
match_versus = "India vs Australia"
arena_stadium = "Narendra Modi Stadium, Ahmedabad"
weather_month = "January"
region_geography = "DRY ARID DUST PLAINS"

with setup_tab1:
    st.markdown("#### Configure Asset DNA Parameters")
    
    if industry == "ELECTIONS":
        meta_col1, meta_col2, meta_col3 = st.columns(3)
        with meta_col1:
            target_name = st.text_input("State Node Name", value="Andhra Pradesh")
            party_selected = st.text_input("Target Political Party String", value="YSRCP")
            charismatic_anchor = st.selectbox("Leadership Core Anchor Profile", [
                "Legacy of the Party Founder", "New Mass Hero", "Legacy of Active Leader", "Standard Bureaucratic Alignment"
            ])
        with meta_col2:
            election_type = st.selectbox("Election Classification Type", ["Assembly Elections", "Lok Sabha Elections", "Bypoll Matrix"])
            number_of_seats = st.slider("Total Number of Seats in State Landscape", 10, 545, 175, step=1)
            ideology_shift = st.selectbox("Socio-Ideological Core Shift", [
                "Active Search for New Party Birth", "Stable Retention of Legacy Status-Quo", "Fragmented Binary Chaos State"
            ])
        with meta_col3:
            election_year = st.text_input("Election Target Year", value="2029")
            constituency_name = st.text_input("Target Focus Constituency Name", value="Nuzvid")
            migrant_friction = st.slider("Migrant Labour vs Local Friction Index", 0.0, 1.0, 0.65, step=0.05)

        inner_col1, inner_col2 = st.columns(2)
        with inner_col1:
            const_profile = st.selectbox(
                "Constituency Demographic Profile", 
                ["URBAN", "RURAL", "SEMI RURAL", "BC POPULATED", "SC POPULATED", "TRIBAL"]
            )
        with inner_col2:
            state_profile = st.selectbox(
                "All-State Geographic Dominance Profile", 
                ["urban", "rural", "semi rural", "bc populated", "sc populated", "tribal"]
            )

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
            number_of_screens = st.slider("Number of Screens Deployed Globally", 100, 25000, 4500, step=250)
            
        inner_col1, inner_col2 = st.columns(2)
        with inner_col1:
            movie_lang = st.selectbox("Primary Language Deployment", ["TELUGU", "TAMIL", "KANNADA", "MALAYALAM", "HINDI", "ENGLISH", "MULTI LINGUAL"])
        with inner_col2:
            movie_scale = st.selectbox("Release Scale Strategy Footprint", ["REGIONAL", "PAN INDIA", "GLOBAL"])

    elif industry == "SPORTS_AUCTIONS":
        meta_col1, meta_col2 = st.columns(2)
        with meta_col1:
            country_name = st.text_input("Country Geography", value="India")
            sport_type = st.text_input("Sport Classification", value="Cricket")
            match_versus = st.text_input("Match Billing Entry (X vs Y Matrix)", value="India vs Australia")
        with meta_col2:
            arena_stadium = st.text_input("Ground / Arena / Stadium Name", value="Narendra Modi Stadium, Ahmedabad")
            weather_month = st.selectbox("Target Month (Weather Calibration)", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            region_geography = st.selectbox("Atmosphere Region Profile (Air / Temp / Humidity)", ["HIGH HUMIDITY COASTAL GRID", "DRY ARID DUST PLAINS", "HIGH-ALTITUDE THIN AIR SECTOR"])

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

with st.expander("📂 Levels 1 & 2: Respondent Bias & Field-Worker Distortion Matrix", expanded=False):
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
#        ⚡ OUTPUT ENGINE & DYNAMIC VERTICAL TARGET COMPUTATIONS
# ==============================================================================
st.write("---")

if st.button("🚀 EXECUTE EPISTEMIC PREDICTIVE TRUTH ENGINE"):
    resp_distortion = sum([r1, r2, r3, r4]) * 0.10
    worker_distortion = sum([w1, w2, w3]) * 0.12
    total_distortion = min(0.95, resp_distortion + worker_distortion + noise_slider)
    confidence_score = max(0.05, 1.0 - total_distortion)

    st.markdown(f"## 🎯 Output Intelligence Brief: `{industry}`")
    
    # -------------------------------------------------------------------------
    # VERTICAL 1: ELECTIONS ENGINE OUTPUT
    # -------------------------------------------------------------------------
    if industry == "ELECTIONS":
        winner_party = party_selected if party_selected else "TDP-JSP Alliance"
        runner_party = "YSRCP" if winner_party != "YSRCP" else "TDP Alliance"
        
        winner_seats = int(number_of_seats * (0.55 + (confidence_score * 0.15)))
        runner_seats = number_of_seats - winner_seats
        winner_margin_votes = int(1250000 * confidence_score)
        runner_margin_votes = int(winner_margin_votes * 0.72)
        
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("🏆 Majority Winning Party", winner_party, f"+{winner_margin_votes:,} Vote Margin")
        with m2:
            st.metric("🥈 Second Party (Runner-Up)", runner_party, f"Margin: {runner_margin_votes:,} Votes")
        with m3:
            st.metric("Seats Won by Winner", f"{winner_seats} / {number_of_seats}")
        with m4:
            st.metric("Seats Won by Runner-Up", f"{runner_seats} / {number_of_seats}")

        st.markdown(f"""
        <div class="metric-card">
            <h4>🗺️ Constituency vs. All-State Calculation Summary</h4>
            <ul>
                <li><b>Target State:</b> {target_name} ({election_year} {election_type})</li>
                <li><b>State Demographic Profile:</b> <code>{state_profile}</code></li>
                <li><b>Focus Constituency:</b> {constituency_name} (Demographic: <code>{const_profile}</code>)</li>
                <li><b>Constituency Seat Prediction:</b> {winner_party} leads in <b>{constituency_name}</b> by a projected margin of ~14,200 votes.</li>
                <li><b>All-State Calculation:</b> Overall swing is favoring the majority coalition across <b>{state_profile}</b> belts with high turnout weight.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # VERTICAL 2: MEDIA & MOVIES ENGINE OUTPUT
    # -------------------------------------------------------------------------
    elif industry == "MEDIA_MOVIES":
        day_1 = round(movie_budget * 0.38 * (1 + confidence_score), 2)
        south_15 = round(day_1 * 4.2, 2)
        north_15 = round(day_1 * 3.1 if movie_scale != "REGIONAL" else day_1 * 0.4, 2)
        overseas_15 = round(day_1 * 2.8 if movie_scale == "GLOBAL" else day_1 * 1.2, 2)
        
        total_gross = round(south_15 + north_15 + overseas_15, 2)
        total_net = round(total_gross * 0.54, 2)
        
        roi = total_gross / movie_budget
        if roi > 3.0: verdict = "🔥 ALL TIME INDUSTRY HIT"
        elif roi > 2.2: verdict = "🚀 BLOCKBUSTER"
        elif roi > 1.5: verdict = "⭐ HIT"
        elif roi > 1.1: verdict = "👍 ABOVE AVERAGE"
        elif roi > 0.8: verdict = "😐 AVERAGE"
        else: verdict = "❌ FLOP"
        
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("🎬 First Day Collection", f"₹ {day_1} Cr")
        with m2:
            st.metric("💰 Total Gross Collection", f"₹ {total_gross} Cr")
        with m3:
            st.metric("💵 Total Net Share", f"₹ {total_net} Cr")
        with m4:
            st.metric("📊 Commercial Verdict", verdict)

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"""
            <div class="metric-card">
                <h4>🌍 15-Day Regional Breakdown</h4>
                <ul>
                    <li><b>South India (First 15 Days):</b> ₹ {south_15} Cr</li>
                    <li><b>North India (First 15 Days):</b> ₹ {north_15} Cr</li>
                    <li><b>Overseas (First 15 Days):</b> ₹ {overseas_15} Cr</li>
                    <li><b>Release Footprint:</b> {number_of_screens:,} Screens | Language: {movie_lang}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col_b:
            st.markdown(f"""
            <div class="metric-card">
                <h4>🏆 Records Created & Milestones</h4>
                <ul>
                    <li>Highest Day 1 collection for <b>{hero_name}</b> in regional territory.</li>
                    <li>Fastest ₹100 Cr entry for production house <b>{production_house}</b>.</li>
                    <li>Record opening screen count for scale type: <code>{movie_scale}</code>.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        # --- NEW: 15-DAY TIME-SERIES COLLECTION CHART ---
        st.markdown("### 📈 15-Day Daily Box Office Trajectory (₹ Crore)")
        
        # Modeling standard theatrical decay curves over 15 days
        days = [f"Day {i}" for i in range(1, 16)]
        decay_factors = [1.0, 0.75, 0.85, 0.45, 0.38, 0.35, 0.30, 0.50, 0.60, 0.28, 0.22, 0.20, 0.18, 0.25, 0.30]
        
        daily_south = [round((south_15 / sum(decay_factors)) * f, 2) for f in decay_factors]
        daily_north = [round((north_15 / sum(decay_factors)) * f, 2) for f in decay_factors]
        daily_overseas = [round((overseas_15 / sum(decay_factors)) * f, 2) for f in decay_factors]
        daily_total = [round(s + n + o, 2) for s, n, o in zip(daily_south, daily_north, daily_overseas)]

        df_trend = pd.DataFrame({
            "Day": days,
            "South India": daily_south,
            "North India": daily_north,
            "Overseas": daily_overseas,
            "Total Daily Gross": daily_total
        }).set_index("Day")

        st.line_chart(df_trend)

    # -------------------------------------------------------------------------
    # VERTICAL 3: SPORTS AUCTIONS & MATCH ENGINE OUTPUT
    # -------------------------------------------------------------------------
    elif industry == "SPORTS_AUCTIONS":
        teams = match_versus.split("vs")
        team_a = teams[0].strip() if len(teams) > 0 else "Team A"
        team_b = teams[1].strip() if len(teams) > 1 else "Team B"
        
        winner_team = team_a if confidence_score > 0.45 else team_b
        runner_team = team_b if winner_team == team_a else team_a
        winning_margin = "4 Wicked Gates / 34 Runs" if "Cricket" in sport_type else "2 Goals"
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("🏆 Projected Winner", winner_team)
        with m2:
            st.metric("📐 Projected Winning Margin", winning_margin)
        with m3:
            st.metric("🥈 Runner-Up Squad", runner_team)

        st.markdown(f"""
        <div class="metric-card">
            <h4>🧠 Match Root-Cause Analysis (Ground & Atmospheric Calibration)</h4>
            <p><b>Event Node:</b> {match_versus} at <b>{arena_stadium}</b> ({weather_month})</p>
            <ul>
                <li><b>WHAT CAUSED THE WIN ({winner_team}):</b> Optimal adaptation to the <code>{region_geography}</code> terrain profile. Superior heavy ball control during second innings under high dew point index.</li>
                <li><b>WHAT CAUSED THE LOSS ({runner_team}):</b> Misread of seam movement during powerplay overs due to rapid drop in air density during late evening hours in {weather_month}.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info(f"Target vertical profile `{industry}` successfully processed under strict risk parameters.")

    # Shared Saptabhaṅgī Matrix Visualizer
    st.write("---")
    st.markdown("### 📊 Saptabhaṅgī Truth Probability Vector Matrix")
    
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

    fig, ax = plt.subplots(figsize=(10, 3.5))
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#161b22')
    
    y_pos = np.arange(len(saptabhangi_states))
    ax.barh(y_pos, list(saptabhangi_states.values()), color='#238636', edgecolor='#30363d')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(list(saptabhangi_states.keys()), color='#c9d1d9')
    ax.invert_yaxis()  
    ax.set_xlabel('Probability Weight Score (%)', color='#c9d1d9')
    ax.tick_params(colors='#c9d1d9')
    
    for spine in ax.spines.values():
        spine.set_color('#30363d')
        
    st.pyplot(fig)
