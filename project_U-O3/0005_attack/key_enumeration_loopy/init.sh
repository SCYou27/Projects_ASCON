mkdir Tables/
mkdir Iterations/
mkdir Predictions/
for i in $(seq -f "%02g" 1 10)
  do
    mkdir Tables/L$i/
    mkdir Iterations/L$i/
    mkdir Predictions/L$i/
    unzip ../template_attack_loopy_D99_TABLES_L$i/Tables.zip
    mv Tables/*.npy Tables/L$i/
  done
unzip ../data_SASCA/data_key.zip
unzip ../data_SASCA/data_ciphertag.zip
unzip ../data_SASCA/data_nonce.zip
unzip ../data_SASCA/data_plaintext.zip
