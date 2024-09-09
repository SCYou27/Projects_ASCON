# Validation stage  
We recorded 4000 traces (stored in 40 ZIP files) for template profiling.  

1. **Generate I/O data:**  
   The folder `inter_gen/` contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. We moved the Python code into another folder `inter_gen_code/` to prevent overwriting the data we had used.  

2. **Download the raw traces:**  
   The 4000 raw traces are stored in 40 ZIP files. Please download the raw traces with the following commands:
   
   `cd Raw/`  
   `./script_all.sh`
   
   Alternatively, please visit our university webpage to download the files manually:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#VA  

3. **Check the raw traces and their corresponding AEAD outputs (ciphers and tags):**
   
   `cd preproc/`  
   `./script_all.sh`
   
   This will check the quality of the recorded traces against the reference trace (`0001_reference/preproc/ref_trace.npy`) as well as whether the recorded responses from the CW-Lite board are equal to our pre-calculated ciphers and tags.

4. **Calculate our target intermediate values:**  
   With the pre-generated I/O data, we calculated all the target intermediate values. Unlike the cases in the detection and profiling stages, we did not perform a multiple linear regression with the intermediate values recorded in this stage. We just used the values as reference answers for validation. Therefore, we stored the intermediate values as an 8-bit or 16-bit integer here instead of binary variables in the two previous stages.     

   We first calculated the target intermediate values in 32-bit H/L words (stored in bytes):
   
   `cd find_intermediates/`  
   `./script_all.sh`  
   
   Then we bit-interleaved the H/L data into the E/O data:
   
   `cd find_intermediates_sliced/`  
   `./script_all.sh`  

   In addition, we also calculated the target 16-bit intermediate values (H/L) by concatenating two consecutive bytes:  

   `cd find_intermediates_16bit/`  
   `./script_all.sh`  

5. **Downsample the raw traces**  
   With the following command lines, we downsample the raw traces from 500 to 10 points per clock cycle (PPC) by summing up the values from every 50 consecutive samples to form the new traces:

   `cd Resample_HDF5/`  
   `./script_all.sh`  

***This page is still under revision***

<!--
6. **Validate our templates**  
   After all the preprocessing steps above, we validated our templates in the following subdirectories:
   
   *templates for byte fragments (H/L)*:  
   `cd template_validation_bytes_O/`  
   `./script_all.sh`
   
   *templates for byte fragments (E/O)*:  
   `cd template_validation_bytes_S/`  
   `./script_all.sh`
   
   *templates for 16-bit fragments (H/L)*:  
   `cd template_validation_16bits_O/`  
   `./script_all.sh`  
-->


