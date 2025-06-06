
import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="California ROI Dashboard", layout="wide")

# Load your ROI dataset
@st.cache_data
def load_data():
    return pd.read_csv("roi_data.csv")

df = load_data()

st.title("California Housing ROI Dashboard")

# Sidebar filters
st.sidebar.header("Filter Investment Options")
price_range = st.sidebar.slider("Predicted Price Range (in $100,000s)", float(df['PredictedPrice'].min()), float(df['PredictedPrice'].max()), (1.0, 3.5))
roi_range = st.sidebar.slider("ROI Range", float(df['ROI'].min()), float(df['ROI'].max()), (0.0, 1.0))
house_age = st.sidebar.slider("House Age Range", int(df['HouseAge'].min()), int(df['HouseAge'].max()), (10, 40))

# Filter dataset
filtered_df = df[
    (df['PredictedPrice'] >= price_range[0]) & (df['PredictedPrice'] <= price_range[1]) &
    (df['ROI'] >= roi_range[0]) & (df['ROI'] <= roi_range[1]) &
    (df['HouseAge'] >= house_age[0]) & (df['HouseAge'] <= house_age[1])
]

st.subheader(f"Found {len(filtered_df)} Matching Results")

# Map visualization
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=filtered_df['Latitude'].mean(),
        longitude=filtered_df['Longitude'].mean(),
        zoom=6,
        pitch=45,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=filtered_df,
            get_position='[Longitude, Latitude]',
            get_color='[255, 0, 0, 160]',
            get_radius=5000,
        ),
    ],
))

# Data table
st.markdown("### Investment Details Table")
st.dataframe(filtered_df[['Latitude', 'Longitude', 'PredictedPrice', 'ActualPrice', 'ROI', 'HouseAge']])
