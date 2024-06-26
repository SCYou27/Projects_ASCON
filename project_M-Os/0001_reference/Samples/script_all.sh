for i in $(seq -f "%04g" 0 9)
  do
    Name='https://www.cl.cam.ac.uk/research/security/datasets/ascon/M-Os/0001_reference/Samples/Samples_RE_'${i}'.hdf5'
    wget $Name
  done
