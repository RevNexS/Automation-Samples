
# Navigate to your project directory
cd "."

# Create a virtual environment
Write-Host
Write-Host "Creating Virtual Environment..."
python -m venv venv


# Activate the virtual environment
Write-Host "Activating Virtual Environment..."
.\venv\Scripts\Activate

# Install the Python packages
Write-Host "Installing Required Python Library in Vitural Environment..."
pip install -r requirement.txt
Write-Host 
Write-Host 
Write-Host 

# Run Scripts
Write-Host 
Write-Host 
Write-Host "Running Scrapper..."
Write-Host 
Write-Host 
python .\main.py

deactivate