mkdir Rank_log/
for i in '0001' '0002' '0003' '0004' '0005' '0006' '0007' '0008' '0009' '0010' '0020' '0050' '0100'
  do
    mkdir Rank_log/L$i/
  done
unzip ../template_attack_KEY_S_TABLES/Tables.zip
unzip ../data_fragments/key_bytes_S.zip
