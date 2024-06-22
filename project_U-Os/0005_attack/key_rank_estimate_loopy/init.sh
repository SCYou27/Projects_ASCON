mkdir Tables/
mkdir Rank_log/
for i in $(seq -f "%02g" 1 10)
  do
    mkdir Tables/L$i/
    mkdir Iterations/L$i/
    mkdir Predictions/L$i/
    unzip ../template_attack_loopy_D99_TABLES_L$i/Tables.zip
    mv Tables/*.npy Tables/L$i/
    mkdir Rank_log/L$i/
  done
unzip ../data_fragments/key_bits.zip
