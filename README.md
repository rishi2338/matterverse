# MATTERVERSE

An interactive Engineering Chemistry and materials-science learning platform.

## Stack
- Streamlit + Python
- Plotly 3D atomic-lattice visualisation
- Streamlit Community Cloud deployment

## Features
- Overview dashboard with interactive 3D atomic lattice
- Searchable materials library
- Material properties and reference values
- Nanoparticle sphere calculator
- Material comparison table and density chart

## Run locally
Python 3.10 or newer is recommended.

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the local URL printed by Streamlit (usually http://localhost:8501).

## Deploy free with Streamlit Community Cloud
1. Open https://share.streamlit.io/ and sign in with GitHub.
2. Click **Create app**.
3. Select repository `rishi2338/matterverse` and branch `main`.
4. Set **Main file path** to `streamlit_app.py`.
5. Click **Deploy**.

This deployment uses Streamlit Community Cloud. Render and Vercel are not required for this version. The free service is subject to Streamlit Community Cloud's usage and availability policies.

## Educational note
The material catalogue contains representative educational reference values, not certified engineering design data or experimental measurements.
