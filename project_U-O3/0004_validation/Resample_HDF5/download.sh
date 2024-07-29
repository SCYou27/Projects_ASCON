DIR='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-O3/0004_validation/Resample_HDF5/'
for i in $(seq -f "%02g" 0 3)
  do
    wget ${DIR}part_${i}.hdf5
  done

