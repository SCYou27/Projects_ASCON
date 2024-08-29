TAG=$1 # Os or O3
DATA_DIR='../project_M-'${TAG}'/0005_attack/'
DIR='M-'${TAG}'/' 
mkdir ${DIR}
#
# bytes_O
unzip ${DATA_DIR}template_attack_MASK_O_TABLES/Tables.zip
mv Tables/ ${DIR}Tables_bytes_O/
unzip ${DATA_DIR}template_attack_KEY_O_TABLES/Tables.zip
mv Tables/ ${DIR}Tables_direct_O/
unzip ${DATA_DIR}data_fragments/key_bytes_O.zip
mv key_bytes_O/ ${DIR}Key_bytes_O/
cp -r ${DIR}Key_bytes_O/ ${DIR}Key_direct_O/
#
# bytes_S
unzip ${DATA_DIR}template_attack_MASK_S_TABLES/Tables.zip
mv Tables/ ${DIR}Tables_bytes_S/
unzip ${DATA_DIR}template_attack_KEY_S_TABLES/Tables.zip
mv Tables/ ${DIR}Tables_direct_S/
unzip ${DATA_DIR}data_fragments/key_bytes_S.zip
mv key_bytes_S/ ${DIR}Key_bytes_S/
cp -r ${DIR}Key_bytes_S/ ${DIR}Key_direct_S/
#
