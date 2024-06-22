mkdir key_bits/
mkdir key_bytes/
mkdir key_16bits/
unzip ../data_SASCA/data_key.zip
python3 get_answer.py 0 1000
zip -qq key_bytes.zip -r key_bytes/
zip -qq key_16bits.zip -r key_16bits/
zip -qq key_bits.zip -r key_bits/
rm -r data_key/ key_*/
