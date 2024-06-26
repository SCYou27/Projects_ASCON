lower=0
upper=40
unzip ../inter_gen/ciphertags.zip
mkdir Corrcoef/
python3 check.py all ${lower} ${upper}
python3 check.py show ${lower} ${upper} > report.txt
zip Corrcoef.zip -r Corrcoef/
rm -r ciphertags/ Corrcoef/ __pycache__/
