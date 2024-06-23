mkdir key_bytes_O/
mkdir key_bytes_S/
unzip ../data_SASCA/data_key.zip
python3 get_answer.py 0 1000
zip -qq key_bytes_O.zip -r key_bytes_O/
zip -qq key_bytes_S.zip -r key_bytes_S/
rm -r data_key/ key_*/
