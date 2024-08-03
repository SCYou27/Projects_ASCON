DIR='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/0005_attack/Resample_HDF5/'
for i in $(seq -f "%02g" 0 9)
  do
    wget ${DIR}part_${i}.hdf5
  done

