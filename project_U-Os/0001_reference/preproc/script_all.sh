unzip ../inter_gen/ciphertags.zip
python3 pre_ref_count.py
python3 pre_get_corr.py all 4
rm -r ciphertags/ __pycache__/
