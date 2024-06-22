for i in $(seq -f "%04g" 0 99)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/0002_detection/Raw/Raw_DN_'${i}'.zip'
    wget $Name
  done
