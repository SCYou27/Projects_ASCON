# Reference traces

We recorded 1600 traces and took their arithmetic mean vector as a reference trace, so the later recorded traces can be compared against this reference trace to check whether some unexpected event happened and resulted in a wrong recording. This will be divided into the following small tasks:  

1. Generate I/O date:  
   The folder "inter_gen/" contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. To prevent overwriting the data we had used, we moved the Python code into another folder "inter_gen_code/".

2. Download the raw traces:
   Please download the raw traces with the following commands:  
   `cd Raw/`  
   `./script_all.sh`  
   Alternatively, please visit our university webpage to manually download the files:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#RE

3. Process the raw traces and find the reference trace:  
   `cd preproc/`  
   `./script_all.sh`  
   This will generate the reference trace "preproc/ref_trace.npy" for trace quality validation in the later phases.
