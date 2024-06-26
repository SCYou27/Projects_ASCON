lower=0
upper=100
mkdir Corrcoef/
python3 check.py all ${lower} ${upper}
python3 check.py show ${lower} ${upper} > report.txt
zip Corrcoef.zip -r Corrcoef/
rm -r Corrcoef/ __pycache__/
