
import streamlit as st
import pandas as pd
import pydeck as pdk
import os

st.set_page_config(page_title="California ROI Dashboard", layout="wide")

# Load your ROI dataset
@st.cache_data
def load_data():
    path = os.path.join(os.path.dirname(__file__), "roi_data.csv")
    return pd.read_csv(path)

df = load_data()

st.title("California Housing ROI Dashboard")

# Sidebar filters

st.sidebar.header("Filter Investment Options")

price_range = st.sidebar.slider(
    "Predicted Price Range ($)", 
    int(df['PredictedPrice'].min()), 
    int(df['PredictedPrice'].max()), 
    (100000, 300000)
)

roi_cap = df['ROI'].quantile(0.99)
roi_min = max(-20, df['ROI'].min())
roi_max = min(roi_cap, df['ROI'].max())

roi_range = st.sidebar.slider(
    "ROI Range (%)", 
    float(roi_min), 
    float(roi_max), 
    (0.0, 20.0)
)

house_age = st.sidebar.slider(
    "House Age Range", 
    int(df['HouseAge'].min()), 
    int(df['HouseAge'].max()), 
    (10, 40)
)


# Filter dataset
filtered_df = df[
    (df['PredictedPrice'] >= price_range[0]) & (df['PredictedPrice'] <= price_range[1]) &
    (df['ROI'] >= roi_range[0]) & (df['ROI'] <= roi_range[1]) &
    (df['HouseAge'] >= house_age[0]) & (df['HouseAge'] <= house_age[1])
]

st.subheader(f"Found {len(filtered_df)} Matching Results")

if filtered_df.empty:
    st.warning("No blocks match your filter. Please adjust the sliders.")
else:
    st.subheader("Map of High ROI Blocks")

    tooltip = {
        "html": "<b>ROI:</b> {ROI}<br/><b>Price:</b> ${PredictedPrice}M",
        "style": {"color": "white"}
    }

    st.pydeck_chart(pdk.Deck(
        map_style="light",
        initial_view_state=pdk.ViewState(
            latitude=filtered_df['Latitude'].mean(),
            longitude=filtered_df['Longitude'].mean(),
            zoom=8,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=filtered_df,
                get_position=["Longitude", "Latitude"],
                get_color="[255, 140 * ROI, 0, 160]",
                get_radius=5000,
                pickable=True,
            ),
        ],
        tooltip=tooltip
    ))

    st.markdown("### Investment Details Table")
    st.dataframe(filtered_df[['Latitude', 'Longitude', 'PredictedPrice', 'MedianHouseValue', 'ROI', 'HouseAge']])

