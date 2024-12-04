# Experiments on U-O3 data set  

When we recorded our traces for experiments, we split the traces into five different groups: _Reference, Detection, Profiling (Training), Validation, and Attack (Testing)_. The code processing each of these groups can be found in

 -  **0001\_reference:** to find a reference trace for recording quality checking.
 -  **0002\_detection:** to determine points of interest (PoI). 
 -  **0003\_training:** to build our templates.
 -  **0004\_validation:** to validate our templates.
 -  **0005\_attack:** to recover keys used in ASCON AEAD with our attack scenario.

Please check the REAMDE.md in each subdirectory for detailed instructions.

The Python scripts for controlling the recording hardware and target hardware can be found seperately at

https://www.cl.cam.ac.uk/research/security/datasets/ascon/src_recording/CW_ASCON_O3_recording_20240528.zip

Please check our [web site](https://www.cl.cam.ac.uk/research/security/datasets/ascon/index.html#U-O3-recording) for details on the configuration of the recording platform.

## Differences between U-Os and U-O3 data sets  

The Python code and data sets for our U-O3 experiments are quite similar to those for our U-Os experiments, except for the following minor differences:

 - **Data format for raw traces:** The raw traces are stored as arrays of 8-byte floating-point numbers for the U-Os experiments, then compressed into ZIP files. For the U-O3 experiments, the raw data are instead compressed and stored in [HDF5](https://www.hdfgroup.org/solutions/hdf5/) files. Since the oscilloscope provides only 10-bit samples, storing each as a 8-byte floating-point number would be wasteful. Instead, we had the NI oscilloscope return traces as 16-bit integer arrays, along with a common floating-point gain and offset values, also stored in our HDF5 files, to enable conversion back into volt values.
 - **Length of downsampled traces:** Each downsampled trace covers 2560 clock cycles in our U-O3 data sets, while it covers 2650 clock cycles in the U-Os data sets.

Please check the REAMDE.md in each subdirectory for detailed instructions.

