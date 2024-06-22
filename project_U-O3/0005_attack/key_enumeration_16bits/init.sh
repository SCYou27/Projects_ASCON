mkdir Iterations/
mkdir Predictions/
for i in $(seq -f "%02g" 1 10)
  do
    unzip ../template_attack_16bits_O_TABLES/Tables_L$i.zip
    mkdir Iterations/L$i/
    mkdir Predictions/L$i/
  done
unzip ../data_SASCA/data_key.zip
unzip ../data_SASCA/data_ciphertag.zip
unzip ../data_SASCA/data_nonce.zip
unzip ../data_SASCA/data_plaintext.zip
