unzip ../template_attack_bytes_O_TABLES/Tables.zip
mkdir Iterations/
mkdir Predictions/
for i in $(seq -f "%02g" 1 10)
  do
    mkdir Iterations/L$i/
    mkdir Predictions/L$i/
  done
unzip ../data_SASCA/data_key.zip
unzip ../data_SASCA/data_ciphertag.zip
unzip ../data_SASCA/data_nonce.zip
unzip ../data_SASCA/data_plaintext.zip
