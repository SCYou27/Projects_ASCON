TAG=$1 # Os or O3
DATA_DIR='../project_U-'${TAG}'/0005_attack/'
DIR='U-'${TAG}'/' 
mkdir ${DIR}
#
# bits
mkdir ${DIR}Tables_bits/
for i in $(seq -f "%02g" 1 10)
  do
    unzip ${DATA_DIR}template_attack_loopy_D99_TABLES_L$i/Tables.zip
    mv Tables/ ${DIR}Tables_bits/L$i/
  done
unzip ${DATA_DIR}data_fragments/key_bits.zip
mv key_bits/ ${DIR}Key_bits/
#
# bytes
unzip ${DATA_DIR}template_attack_bytes_O_TABLES/Tables.zip
mv Tables/ ${DIR}Tables_bytes/
unzip ${DATA_DIR}data_fragments/key_bytes.zip
mv key_bytes/ ${DIR}Key_bytes/
#
# 16bits
for i in $(seq -f "%02g" 1 10)
  do
    unzip ${DATA_DIR}template_attack_16bits_O_TABLES/Tables_L$i.zip
  done
mv Tables/ ${DIR}Tables_16bits/
unzip ${DATA_DIR}data_fragments/key_16bits.zip
mv key_16bits/ ${DIR}Key_16bits/
#
