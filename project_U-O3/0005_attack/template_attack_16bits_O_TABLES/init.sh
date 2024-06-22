tag='004'
mkdir Key_fragments/
mkdir Tables/
for i in $(seq -f "%02g" 1 10)
  do
    mkdir Tables/L$i/
  done
unzip ../../0002_detection/ICS_extract/ics_union_${tag}.zip
unzip ../../0003_training/template_profiling_16bits_O/templateLDA_O${tag}_16bit.zip
unzip ../data_SASCA/data_key.zip
unzip ../data_SASCA/data_ciphertag.zip
