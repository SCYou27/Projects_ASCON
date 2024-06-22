for i in $(seq -f "%04g" 0 399)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-O3/0003_training/Raw/Raw_TR_'${i}'.hdf5'
    wget $Name
  done
