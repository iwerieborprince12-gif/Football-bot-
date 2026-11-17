import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Football Prediction Bot",
    page_icon="⚽",
    layout="wide",
)

# App Header
st.title("⚽ AI Football Prediction & Value Bot")
st.markdown("A personal dashboard tracking match predictions and SportyBet values.")

# --- SIDEBAR: CONTROLS & STATS ---
st.sidebar.header("Bot Controls")
if st.sidebar.button("🔄 Run Fresh Predictions"):
    st.sidebar.success("Model updated successfully with latest fixtures!")

st.sidebar.markdown("---")
st.sidebar.header("Bankroll Status")
st.sidebar.metric(label="Current Bankroll", value="₦125,450", delta="+₦14.2%")
st.sidebar.metric(label="Model Win Rate", value="68.4%", delta="+2.1%")

# --- MOCK DATA FOR MATCHES ---
match_data = {
    "Time": ["15:00", "17:30", "20:00", "21:00"],
    "Match": [
        "Arsenal vs Chelsea",
        "Real Madrid vs Barcelona",
        "Inter Milan vs AC Milan",
        "PSG vs Marseille",
    ],
    "League": ["EPL", "La Liga", "Serie A", "Ligue 1"],
    "Model Pick": ["Arsenal (Home)", "Over 2.5 Goals", "Draw", "PSG (Home)"],
    "Model Prob": ["62%", "74%", "38%", "70%"],
    "SportyBet Odds": [1.65, 1.85, 3.40, 1.45],
    "Value Edge": ["+4.2%", "+7.5%", "-2.1%", "+1.5%"],
}

df_matches = pd.DataFrame(match_data)

# --- TABS ---
tab1, tab2, tab3 = st.tabs(
    ["📊 Today's Predictions", "🎯 Value Scanner", "📈 Betting History"]
)

with tab1:
    st.subheader("Upcoming Fixtures & Model Probabilities")
    st.dataframe(df_matches, use_container_width=True)

with tab2:
    st.subheader("🔥 High-Value Betting Opportunities")
    df_value = df_matches[df_matches["Value Edge"].str.contains(r"\+")]
    st.dataframe(df_value, use_container_width=True)
    st.info("💡 Tip: Only stake on matches with a Value Edge greater than +3.0%.")

with tab3:
    st.subheader("Performance Tracker")
    chart_data = pd.DataFrame(
        {
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Bankroll (₦)": [
                110000,
                112500,
                111000,
                115200,
                118000,
                121500,
                125450,
            ],
        }
    )
    st.line_chart(chart_data, x="Day", y="Bankroll (₦)")
