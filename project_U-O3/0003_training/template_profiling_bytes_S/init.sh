tag=$1
unzip ../find_intermediates_sliced/intermediate_values.zip
unzip ../../0002_detection/ICS_extract/ics_union_${tag}.zip
mkdir templateLDA_O004/
python3 init.py O${tag}

