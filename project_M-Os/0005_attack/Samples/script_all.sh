for i in $(seq -f "%04g" 0 999)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/M-Os/0005_attack/Samples/Samples_TS_'${i}'.hdf5'
    wget $Name
  done
