tag='004'
unzip ../find_intermediates/intermediate_values.zip
unzip ../../0002_detection/ICS_extract/ics_union_${tag}.zip
python3 init.py O${tag}
python3 train_script.py
zip -qq templateLDA_O${tag}.zip -r templateLDA_O${tag}/
rm -r intermediate_values/ templateLDA_*/ ics_*/ __pycache__/
