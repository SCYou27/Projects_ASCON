for i in $(seq -f "%04g" 0 99)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-O3/0005_attack/Raw/Raw_TS_'${i}'.hdf5'
    wget $Name
  done
