for i in $(seq -f "%04g" 0 9)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/0001_reference/Raw/Raw_RE_'${i}'.zip'
    wget $Name
  done
