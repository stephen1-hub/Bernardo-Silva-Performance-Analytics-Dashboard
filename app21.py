import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Player Scouting Dashboard", layout="wide")

col1, col2 = st.columns([1, 3])

with col1:
    st.image("bernardo.jpg", width=150)

with col2:
    st.title("⚽ Bernardo Silva – Scouting & Performance Dashboard")
    st.markdown("Data-driven analysis across 2014/2015 – 2025/26 seasons")

# -----------------------------
# LOAD DATA (FIXED FILE)
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_excel("player-groups (6).xlsx")
    return df

df = load_data()

# -----------------------------
# RENAME COLUMNS
# -----------------------------
df = df.rename(columns={
    "number": "ID",
    "season": "Season",
    "team": "Club",
    "apps": "Matches Played",
    "min": "Minutes Played",
    "goals": "Goals Scored",
    "assists": "Assists Made",
    "sp90m": "Goal Contributions per 90",
    "kp90": "Key Passes per 90",
    "xG": "Expected Goals",
    "xA": "Expected Assists",
    "xG90": "Expected Goals per 90",
    "xA90": "Expected Assists per 90"
})

# sort chronologically
try:
    df["Season"] = pd.Categorical(df["Season"], categories=sorted(df["Season"].unique()), ordered=True)
    df = df.sort_values("Season")
except:
    pass

# -----------------------------
# FILTERS
# -----------------------------
st.sidebar.title("🎛️ Filters")

all_seasons = sorted(df["Season"].unique())

select_all = st.sidebar.checkbox("Select All Seasons", value=True)

if select_all:
    season_filter = all_seasons
else:
    season_filter = st.sidebar.multiselect(
        "Select Season(s)",
        all_seasons,
        default=all_seasons[:1]
    )

filtered_df = df[df["Season"].isin(season_filter)]

# -----------------------------
# KPI SECTION
# -----------------------------
st.subheader("📊 Key Performance Summary")

col1, col2, col3, col4 = st.columns(4)

latest = filtered_df.iloc[-1]
previous = filtered_df.iloc[-2] if len(filtered_df) > 1 else latest

col1.metric("Goals ⚽", latest["Goals Scored"], latest["Goals Scored"] - previous["Goals Scored"])
col2.metric("Assists 🎯", latest["Assists Made"], latest["Assists Made"] - previous["Assists Made"])
col3.metric("Minutes Played ⏱️", latest["Minutes Played"], latest["Minutes Played"] - previous["Minutes Played"])
col4.metric("xA per 90 🧠", latest["Expected Assists per 90"], round(latest["Expected Assists per 90"] - previous["Expected Assists per 90"], 2))

# -----------------------------
# ROLE EVOLUTION
# -----------------------------
st.subheader("📈 Role Evolution (Minutes & Output)")

fig_role = px.bar(
    filtered_df,
    x="Season",
    y=["Minutes Played", "Goals Scored", "Assists Made"],
    barmode="group",
    title="Minutes vs Output by Season"
)
st.plotly_chart(fig_role, use_container_width=True)

# -----------------------------
# EXPECTED VS ACTUAL
# -----------------------------
st.subheader("🎯 Expected vs Actual Performance")

xg_xa = pd.DataFrame({
    "Metric": ["Goals", "Expected Goals", "Assists", "Expected Assists"],
    "Value": [
        latest["Goals Scored"],
        latest["Expected Goals"],
        latest["Assists Made"],
        latest["Expected Assists"]
    ]
})

fig_eff = px.bar(
    xg_xa,
    x="Metric",
    y="Value",
    title="Actual vs Expected Output"
)
st.plotly_chart(fig_eff, use_container_width=True)

# -----------------------------
# PER 90 PROFILE
# -----------------------------
st.subheader("⚡ Per 90 Performance Profile")

per90 = pd.DataFrame({
    "Metric": ["xG90", "xA90", "Key Passes/90", "Goal Contributions/90"],
    "Value": [
        latest["Expected Goals per 90"],
        latest["Expected Assists per 90"],
        latest["Key Passes per 90"],
        latest["Goal Contributions per 90"]
    ]
})

fig_per90 = px.bar(
    per90,
    x="Metric",
    y="Value",
    title="Per 90 Impact Profile"
)
st.plotly_chart(fig_per90, use_container_width=True)

# -----------------------------
# TREND ANALYSIS
# -----------------------------
st.subheader("📉 Multi-Season Performance Trend")

trend = px.line(
    filtered_df,
    x="Season",
    y=["Goals Scored", "Expected Goals", "Assists Made", "Expected Assists"],
    markers=True,
    title="Goals, xG, Assists & xA Trend"
)

st.plotly_chart(trend, use_container_width=True)

# -----------------------------
# INSIGHT SUMMARY
# -----------------------------
st.subheader("🧠 Scouting Insight Summary")

st.markdown("""
**Player Profile:**
- Elite creative midfielder with consistent attacking influence
- Strong alignment between expected and actual output
- High tactical intelligence and role flexibility

**Key Interpretation:**
- Hybrid playmaker with both goal and assist contribution
- Stable performance across multiple seasons
- Able to adapt between creative and advanced midfield roles

**Recruitment Insight:**
- Ideal for possession-based systems
- High reliability in chance creation
- Strong long-term squad asset due to consistency
""")