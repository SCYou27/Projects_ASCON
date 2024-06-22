unzip ../template_attack_keys_O_TABLES/Tables.zip
mkdir Rank_log/
for i in $(seq -f "%02g" 1 10)
  do
    mkdir Rank_log/L$i/
  done
unzip ../data_fragments/key_bytes.zip
