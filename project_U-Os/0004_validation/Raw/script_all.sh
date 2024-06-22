for i in $(seq -f "%04g" 0 39)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/0004_validation/Raw/Raw_VA_'${i}'.zip'
    wget $Name
  done
