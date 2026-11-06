# MATTERVERSE

An interactive educational material-science platform for exploring engineering materials and nanomaterials.

## Stack
- React + Vite + Three.js frontend (Vercel)
- Flask + Python API backend (Render)

## Features
- Interactive 3D atomic/material visualizer
- Material library and material comparison
- Nanoparticle sphere calculator
- Health and materials API endpoints

## Run locally
Requirements: Node.js 20+ and Python 3.11+.

### Backend
```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
API runs at http://127.0.0.1:5000.

### Frontend
Open a second terminal:
```bash
cd frontend
npm install
npm run dev
```
Open the URL printed by Vite (usually http://localhost:5173).

## Deploy
- Render: create a Web Service from this repository, root directory `backend`, build command `pip install -r requirements.txt`, start command `gunicorn app:app`.
- Vercel: import this repository, set root directory to `frontend`, framework preset Vite, build command `npm run build`, output directory `dist`.
- Set Vercel environment variable `VITE_API_URL` to the Render service URL.
- Set Render environment variable `FRONTEND_ORIGIN` to the deployed Vercel URL.

## Educational note
Values in the demo material catalogue are representative reference values for learning. They are not certified engineering design data or experimental measurements.
