BOUND='004'
unzip ../find_intermediates/intermediate_values.zip
unzip ../../0002_detection/ICS_extract/ics_union_${BOUND}.zip
unzip ../../0003_training/template_profiling_bytes_O/templateLDA_O${BOUND}.zip
mkdir Rank_O${BOUND}/
python3 validate_script.py 0 4
zip Rank_O${BOUND}.zip -r Rank_O${BOUND}/
mkdir Result_Tables/ 
python3 draw_all.py 4
zip Result_Tables.zip -r Result_Tables/
rm -vr intermediate_values/ templateLDA_O*/ ics_*/ __pycache__/ Rank_O*/ Result_Tables/
