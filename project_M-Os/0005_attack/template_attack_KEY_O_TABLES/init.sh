mkdir Tables/
for i in '0001' '0002' '0003' '0004' '0005' '0006' '0007' '0008' '0009' '0010' '0020' '0050' '0100'
  do
    mkdir Tables/L$i/
  done
unzip ../../0002_detection/ICS_extract/ics_union_004.zip
unzip ../../0003_training/template_profiling_MASK_O/templateLDA_O004.zip
