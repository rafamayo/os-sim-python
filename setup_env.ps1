<#
Windows PowerShell setup script
#>
Write-Host "== OS-Sim: Setup (Windows PowerShell) =="

if (-not (Test-Path -Path ".venv")) {
    python -m venv .venv
    Write-Host "-> .venv created"
} else {
    Write-Host "-> .venv already exists"
}

Write-Host "Activating venv..."
& .\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip setuptools wheel
if (Test-Path -Path "requirements.txt") {
    pip install -r requirements.txt
}
if (Test-Path -Path "requirements-dev.txt") {
    pip install -r requirements-dev.txt
}

$response = Read-Host "Install JupyterLab in venv? [Y/n]"
if ($response -eq "" -or $response -match '^[Yy]') {
    pip install jupyterlab
    Write-Host "-> JupyterLab installed"
}

python -m ipykernel install --user --name=os-sim --display-name "OS-Sim (.venv)" 2>$null

Write-Host "== Setup complete =="
Write-Host "Activate in future (PowerShell): .\.venv\Scripts\Activate.ps1"
Write-Host "Start JupyterLab: jupyter lab"
