for i in $(seq -f "%04g" 0 99)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/0005_attack/Raw/Raw_TS_'${i}'.zip'
    wget $Name
  done
