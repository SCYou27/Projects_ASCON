for i in $(seq -f "%04g" 0 39)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/M-Os/0004_validation/Samples/Samples_VA_'${i}'.hdf5'
    wget $Name
  done
