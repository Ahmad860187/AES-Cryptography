Demo
Static web UI: https://relaxed-kataifi-de071e.netlify.app/
What this project supports
- AES modes: ECB, CBC, CFB, OFB, CTR
- Key sizes: 128, 192, 256-bit (hex keys of 32, 48, 64 characters)
- CTR mode requires a 16-byte counter (32 hex characters)
Repository structure
- src/aes_again/, core implementation (AES block wrapper, modes, padding, utilities, CLI entry)
- runner.py, CLI entrypoint that adds src/ to the Python path
- ui/app.py, Streamlit UI
- ui/web-ui/, static browser UI (open index.html)
- aes-again-netlify-fixed/, Netlify-ready static site folder
- demo/, sample inputs
- tests/, pytest suite
Installation (Python)
Create a virtual environment and install dependencies:
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
Dependencies (requirements.txt)
- pycryptodome
- pytest
- streamlit
AES-Cryptography (AES Again) README Page 2
CLI usage
General form:
python runner.py --mode <ecb|cbc|cfb|ofb|ctr> --op <enc|dec> --key <hex> \
 [--ctr <hex>] [--in <path>] [--out <path>] \
 [--hex-in] [--hex-out]
Arguments
- --mode (required): ecb, cbc, cfb, ofb, ctr
- --op (required): enc or dec
- --key (required): hex key (32, 48, or 64 hex chars)
- --ctr (CTR only): 16-byte counter as hex (32 hex chars)
- --in (optional): input file, otherwise reads stdin
- --out (optional): output file, otherwise writes stdout
- --hex-in (optional): treat input as a hex string
- --hex-out (optional): output as a hex string
Examples
# CBC encrypt a file
python runner.py --mode cbc --op enc --key 603deb1015ca71be2b73aef0857d7781 \
 --in demo/sample.txt --out sample.cbc
# CBC decrypt a file
python runner.py --mode cbc --op dec --key 603deb1015ca71be2b73aef0857d7781 \
 --in sample.cbc --out sample.dec.txt
# CTR encrypt a file (ctr is required)
python runner.py --mode ctr --op enc --key 2b7e151628aed2a6abf7158809cf4f3c \
 --ctr f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff \
 --in demo/sample.txt --out sample.ctr
# Read from stdin and print hex output
cat demo/sample.txt | python runner.py --mode ecb --op enc \
 --key 2b7e151628aed2a6abf7158809cf4f3c --hex-out > out.hex
Streamlit UI (local)
Run:
streamlit run ui/app.py
Convenience scripts (if included in your OS)
- run_ui.sh (macOS/Linux)
- Run AES UI.command (macOS)
AES-Cryptography (AES Again) README Page 3
Static web UI (local and deployment)
- Local: open ui/web-ui/index.html in a browser
- Deploy: deploy aes-again-netlify-fixed/ to Netlify as a static site
- Static UI uses CryptoJS and JSZip
Tests
Run:
pytest -q
Crypto notes (demo-focused behavior)
- CBC, CFB, and OFB use a fixed all-zero IV (zero_iv() in src/aes_again/utils.py). Not secure
for production.
- ECB and CBC use a custom zero-count padding: data + 0x00... + one final byte storing
padding length (src/aes_again/padding.py).
- CTR requires a 16-byte counter provided by the user and increments it per block.
