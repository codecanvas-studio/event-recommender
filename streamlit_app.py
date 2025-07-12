import json
import streamlit as st
import pandas as pd
from utils.geo_filter_events import GeoFilterEvents
from utils.text_retrieval import TextRetrieval

st.title("🗓️ Event Recommender")

# Load data
with open("data/events_eventbrite.json", "r", encoding="utf-8") as f:
     events = json.load(f)

# Radius filter
radius_km = st.slider("Radius (km)", 1, 500, 20)

# Initialize GeoFilterEvents with current radius
geo_filter = GeoFilterEvents(
    reference_location=(48.148598, 17.107748),  # Bratislava center
    radius_km=radius_km
)

geo_filtered = geo_filter.filter_events(events)
st.write(f"Filtered events: {len(geo_filtered)}")

# Interests filter
user_interests = st.text_input("Your interests (comma separated)", "brunch, networking, outdoor, coding")

text_retrieval = TextRetrieval()
text_filtered = text_retrieval.event_recommender(geo_filtered, user_interests, 10)

data = []
for e in text_filtered:
    tags = e['tags']
    if isinstance(tags, list):
        tags_str = ", ".join(tags)
    elif isinstance(tags, str):
        tags_str = tags
    else:
        tags_str = ""
    data.append({
        "Title": e['title'],
        "Date": e['date'],
        "Address": e['address'],
        "Tags": tags_str,
        "URL": e['url']
    })

# Create pandas DataFrame for display in Streamlit
df = pd.DataFrame(data)

# Display DataFrame in Streamlit
st.dataframe(df)



