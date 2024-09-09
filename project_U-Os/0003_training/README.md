# Profiling (Training) traces  
We recorded 64000 traces (stored in 400 ZIP files) for template profiling.  

1. **Generate I/O data:**  
   The folder `inter_gen/` contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. We moved the Python code into another folder `inter_gen_code/` to prevent overwriting the data we had used.  

2. **Download the raw traces:**  
   The 64000 raw traces are stored in 400 ZIP files. Please download the raw traces with the following commands:
   
   `cd Raw/`  
   `./script_all.sh`
   
   Alternatively, please visit our university webpage to download the files manually:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#TR  

3. **Check the raw traces and their corresponding AEAD outputs (ciphers and tags):**
   
   `cd preproc/`  
   `./script_all.sh`
   
   This will check the quality of the recorded traces against the reference trace (`0001_reference/preproc/ref_trace.npy`) as well as whether the recorded responses from the CW-Lite board are equal to our pre-calculated ciphers and tags.

4. **Calculate our target intermediate values:**  
   With the pre-generated I/O data, we calculated all the target intermediate values. As we mentioned in our paper, the bit-interleaving (slicing) technique is applied in our target implementations. This means that a 64-bit lane of our binary target intermediate values will be stored in two 32-bit registers, divided into either high/low (H/L) bits or even/odd (E/O) bits.

   We first calculated the target intermediate values in 32-bit H/L words:
   
   `cd find_intermediates/`  
   `./script_all.sh`  
   
   Here each 32-bit value will be cut into four bytes, and then converted to eight binary variables representing each byte, as we will later apply a multiple linear regression on our samples against these binary variables. 

   Then we bit-interleaved the binary H/L data into the E/O data:
   
   `cd find_intermediates_sliced/`  
   `./script_all.sh`  

   In addition, we also calculated the target 16-bit intermediate values for profiling the 16-bit templates (H/L):  

   `cd find_intermediates_16bit/`  
   `./script_all.sh`  

5. **Downsample the raw traces**  
   With the following command lines, we downsample the raw traces from 500 to 10 points per clock cycle (PPC) by summing up the values from every 50 consecutive samples to form the new traces:

   `cd Resample_HDF5/`  
   `./script_all.sh`  

6. **Profile templates**  
   After all the preprocessing steps above, we profiled our templates in the following subdirectories:
   
   *templates for byte fragments (H/L)*:  
   `cd template_profiling_bytes_O/`  
   `./script_all.sh`
   
   *templates for byte fragments (E/O)*:  
   `cd template_profiling_bytes_S/`  
   `./script_all.sh`
   
   *templates for 16-bit fragments (H/L)*:  
   `cd template_profiling_16bits_O/`  
   `./script_all.sh`  



