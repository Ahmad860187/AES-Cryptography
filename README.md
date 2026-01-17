# AES-Cryptography (AES Again)

AES encryption and decryption toolkit implemented in Python. The repository includes a command line interface (CLI), a Streamlit UI, and a static browser UI that can be deployed to Netlify.

Demo (static web UI): https://relaxed-kataifi-de071e.netlify.app/

## What this project supports
- AES modes: ECB, CBC, CFB, OFB, CTR
- Key sizes: 128, 192, 256-bit (hex keys of 32, 48, 64 characters)
- CTR mode requires a 16-byte counter (32 hex characters)

## Repository structure
- `src/aes_again/`  
  Core implementation (AES block wrapper, modes, padding, utilities, CLI entry)
- `runner.py`  
  Runs the CLI while adding `src/` to the Python path
- `ui/app.py`  
  Streamlit UI
- `ui/web-ui/`  
  Static browser UI (open `index.html`)
- `aes-again-netlify-fixed/`  
  Netlify-ready static site folder
- `demo/`  
  Sample inputs for quick testing
- `tests/`  
  Pytest suite

## Installation (Python)
Create a virtual environment and install dependencies:

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
