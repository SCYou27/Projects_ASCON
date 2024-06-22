mkdir Rank_log/
for i in $(seq -f "%02g" 1 10)
  do
    unzip ../template_attack_16bits_O_TABLES/Tables_L$i.zip
    mkdir Rank_log/L$i/
  done
unzip ../data_fragments/key_16bits.zip
