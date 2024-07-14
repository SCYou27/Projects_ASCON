DIR='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-O3/0005_attack/template_attack_16bits_O_TABLES/'
for i in $(seq -f "%02g" 1 10)
  do
    wget ${DIR}Tables_L${i}.zip
  done
