for i in $(seq -f "%04g" 0 799)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/M-Os/0003_training/Samples/Samples_TR_'${i}'.hdf5'
    wget $Name
  done
