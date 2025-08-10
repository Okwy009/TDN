import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Investor Insights Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    file_path = r'C:\Users\user\Desktop\Data_Analyst\TDN_Network\TDN_Alpha_and_Access\AI_Showcase_Virtual_Conf_Full_attendee_list.xlsx'
    all_sheets = pd.read_excel(file_path, sheet_name=None)
    return all_sheets

# Load all sheets
all_sheets = load_data()
df_investors = all_sheets['AI investors'].copy()

# Rename necessary columns (update if not already done in preprocessing)
df_investors = df_investors.rename(columns={
    'Looking to invest in Pre-seed Startups\n(198)': 'invest_pre_seed',
    'Looking to invest in Seed Startups\n(226)': 'invest_seed',
    'Looking to invest in Series A Startups\n(115)': 'invest_series_a',
    'Looking to invest in Series B Startups\n(51)': 'invest_series_b',
    'Looking to invest in Series C+ Startups\n(5)': 'invest_series_c_plus',
    'Globally – everywhere\n(94)': 'region_global',
    'Interested in AI automation services for the company\n(102)': 'AI Services',
    'Interested in educating their team on using AI in their job\n(83)': 'Team AI Training',
    'Interested in taking an AI automation course themselves\n(109)': 'Personal AI Course'
})

# Sidebar filters
st.sidebar.title("Filter Investors")
if 'region_global' in df_investors.columns:
    regions = st.sidebar.multiselect("Select Regions", options=['region_global'])  # or add more regions
    if regions:
        df_investors = df_investors[df_investors[regions].any(axis=1)]

# Title
st.title("📊 AI Investor Insights Dashboard")
st.markdown("This dashboard visualizes AI investment interest across startup stages and AI-related training or service needs.")

# --- Chart 1: Startup Stages ---
st.subheader("Startup Stages Investors Are Interested In")
stage_cols = ['invest_pre_seed', 'invest_seed', 'invest_series_a', 'invest_series_b', 'invest_series_c_plus']
stage_data = df_investors[stage_cols].sum().sort_values(ascending=True)

fig1, ax1 = plt.subplots()
stage_data.plot(kind='barh', color='skyblue', ax=ax1)
ax1.set_xlabel("Number of Interested Investors")
st.pyplot(fig1)

# --- Chart 2: AI Training Needs ---
st.subheader("AI Training & Service Needs")
ai_cols = ['AI Services', 'Team AI Training', 'Personal AI Course']
ai_needs = df_investors[ai_cols].sum().sort_values(ascending=True)

fig2, ax2 = plt.subplots()
ai_needs.plot(kind='barh', color='lightgreen', ax=ax2)
ax2.set_xlabel("Number of Interested Investors")
st.pyplot(fig2)

# --- Raw Data ---
with st.expander("🔍 View Raw Data"):
    st.dataframe(df_investors)
