for i in $(seq -f "%04g" 0 39)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-O3/0004_validation/Raw/Raw_VA_'${i}'.hdf5'
    wget $Name
  done
