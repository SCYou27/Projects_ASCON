mkdir Predictions/
mkdir Iterations/
for i in '0001' '0002' '0003' '0004' '0005' '0006' '0007' '0008' '0009' '0010' '0020' '0050' '0100'
  do
    mkdir Predictions/L$i/
    mkdir Iterations/L$i/
  done
unzip ../template_attack_MASK_S_TABLES/Tables.zip
unzip ../data_SASCA/data_key.zip
unzip ../data_SASCA/data_ciphertag.zip
unzip ../data_SASCA/data_nonce.zip
unzip ../data_SASCA/data_plaintext.zip
