unzip ../find_intermediates/intermediate_values.zip
mv intermediate_values/ intermediate_values_bytes/
mkdir intermediate_values/
python3 intermediate_combine.py 
zip intermediate_values.zip -r intermediate_values/
rm -vr intermediate_values/ intermediate_values_bytes/
