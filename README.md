# Brewdog-Beer-Challenge
Abbax - Test Automation coding challenge 

# Active venv
source .venv/bin/activate

# Install depdendcies
pip install -r requirements.txt

# Run smoke tests
python3 -m pytest --cache-clear --capture=tee-sys -m Smoke

# Run single test
python3 -m pytest --cache-clear --capture=tee-sys test_beers.py

