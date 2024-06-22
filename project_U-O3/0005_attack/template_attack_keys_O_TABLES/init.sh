tag='004'
mkdir Tables/
for i in $(seq -f "%02g" 1 10)
  do
    mkdir Tables/L$i/
  done
unzip ../../0002_detection/ICS_extract/ics_union_${tag}.zip
unzip ../../0003_training/template_profiling_bytes_O/templateLDA_O${tag}.zip
