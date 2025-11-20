#!/usr/bin/env bash
set -euo pipefail

if [ -d ".venv" ]; then
  echo ".venv already exists. Skipping creation."
else
  python3 -m venv .venv
fi

# shellcheck source=/dev/null
source .venv/bin/activate
uv sync --upgrade
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

echo "Setup complete. Activate with: source .venv/bin/activate"
