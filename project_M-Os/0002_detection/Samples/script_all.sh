for i in $(seq -f "%04g" 0 99)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/M-Os/0002_detection/Samples/Samples_DN_'${i}'.hdf5'
    wget $Name
  done
