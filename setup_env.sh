#!/usr/bin/env bash
set -euo pipefail

echo "== OS-Sim: Setup (Linux/macOS) =="

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  echo "-> .venv created"
else
  echo "-> .venv already exists"
fi

source .venv/bin/activate

python -m pip install --upgrade pip setuptools wheel
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

if [ -f requirements-dev.txt ]; then
  pip install -r requirements-dev.txt
fi

read -r -p "Install JupyterLab in venv if not already installed? [Y/n] " yn
yn=${yn:-Y}
if [[ $yn =~ ^([yY][eE][sS]|[yY])$ ]]; then
  pip install jupyterlab
  echo "-> JupyterLab installed in .venv"
fi

python -m ipykernel install --user --name=os-sim --display-name "OS-Sim (.venv)" || true

echo "== Setup complete =="
echo "Activate the venv:  source .venv/bin/activate"
echo "Start JupyterLab:    jupyter lab"
