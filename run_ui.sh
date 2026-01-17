#!/usr/bin/env bash
# Script to run Streamlit web UI - creates venv, installs deps, starts server
cd "$(dirname "$0")"
# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then python3 -m venv .venv; fi
source .venv/bin/activate
# Install dependencies (quiet mode)
pip install -r requirements.txt >/dev/null
# Start Streamlit server in background
(streamlit run ui/app.py --server.headless true --server.port 8501 &)
sleep 2
# Open browser to the app
open -a "Google Chrome" http://localhost:8501
