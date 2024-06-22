mkdir intermediate_HEX/
mkdir intermediate_HEX/intermediate_trace/
mkdir intermediate_values/
unzip ../inter_gen/keys.zip
unzip ../inter_gen/nonces.zip
unzip ../inter_gen/plaintexts.zip
unzip ../inter_gen/ciphertags.zip
python3 intermediate_calculate.py all
python3 find_hex.py all
python3 intermediate_H2B.py cal
python3 intermediate_H2B.py check
zip intermediate_HEX.zip -r intermediate_HEX/
zip intermediate_values.zip -r intermediate_values/
rm -vr __pycache__/ keys/ nonces/ plaintexts/ ciphertags/ intermediate_HEX/ intermediate_values/
