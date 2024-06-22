zip -qq Key_fragments.zip -r Key_fragments/
for i in $(seq -f "%02g" 1 10)
  do
    zip Tables_L$i.zip -r Tables/L$i/
  done
rm -r __pycache__/ Key_fragments/ Tables/ ics_*/ templateLDA_*/ data_*/

