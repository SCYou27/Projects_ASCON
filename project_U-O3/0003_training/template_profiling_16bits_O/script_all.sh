tag='004'
detail='16bit'
unzip ../find_intermediates_${detail}/intermediate_values.zip
unzip ../../0002_detection/ICS_extract/ics_union_${tag}.zip
mkdir templateLDA_O${tag}_${detail}/
mkdir templateLDA_O${tag}_${detail}/template_KEY/
mkdir templateLDA_O${tag}_${detail}/template_F_B11/
python3 train_script.py
zip templateLDA_O${tag}_${detail}.zip -r templateLDA_O${tag}_${detail}/
rm -vr intermediate_values/ templateLDA_O${tag}_${detail}/ ics_union_${tag}/ __pycache__/
