TAG='004'
unzip ../find_intermediates/intermediate_values.zip
unzip ../../0002_detection/ICS_extract/ics_union_${TAG}.zip
unzip ../../0003_training/template_profiling_MASK_S/templateLDA_O${TAG}.zip
mkdir Rank_O${TAG}/
python3 validate_script.py 0 40
zip Rank_O${TAG}.zip -r Rank_O${TAG}/
mkdir Result_Tables/
python3 draw_all.py 4
zip Result_Tables.zip -r Result_Tables/
rm -vr intermediate_values/ ics_*/ templateLDA_*/ __pycache__/ Rank_*/ Result_Tables/
