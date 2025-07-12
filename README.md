# Event Recommender

A modular portfolio project demonstrating semantic retrieval, and **Streamlit** for interactive event recommendations using parsed Eventbrite-like data.

## Features
✅ Filter events by location radius
✅ Retrieve semantically similar events based on user interests using sentence-transformers  
✅ Interactive Streamlit app for testing recommendations visually

## Project Structure
- `utils/geo_filter_events.py`: Geospatial filtering pipeline
- `utils/text_retrieval.py`: Semantic retrieval pipeline
- `streamlit_app.py`: User-facing demo app
- `data/`: Contains event JSON dataset
- `requirements.txt`: Dependencies

## Installation
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running Streamlit App
```bash
streamlit run streamlit_app.py
```

## License
MIT

---