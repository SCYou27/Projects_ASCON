# Detection traces  
We recorded 16000 traces to select the points of interest (PoI) for template profiling. This is to determine whether a time sample is related to our target intermediate values. In this attack, we determined whether a _clock cycle_ is interesting instead of individual samples. The tasks in this phase are as follows.  

1. **Generate I/O data:**  
   The folder `inter_gen/` contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. We moved the Python code into another folder `inter_gen_code/` to prevent overwriting the data we had used.  

2. **Download the raw traces:**  
   The 16000 raw traces are stored in 100 ZIP files. Please download the raw traces with the following commands:
   
   `cd Raw/`  
   `./script_all.sh`
   
   Alternatively, please visit our university webpage to manually download the files:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#DN  

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

   Then we also converted the binary H/L data into the E/O data:
   
   `cd find_intermediates_sliced/`  
   `./script_all.sh`  
   
5. **Find samples for interesting clock cycle detection:**  
   We used one sample per clock cycle to determine whether a clock cycle is interesting. We calculated the summation of 50 points around the peak of a clock cycle as such a sample for detection:
   
   `cd get_samples/`  
   `./script_all.sh`   

6. **Find the coefficient of determination (_R_<sup>2</sup>) of each intermediate byte**
   We then applied multiple linear regression on the processed samples against the values of the intermediate binary variables to calculate the coefficient of determination (_R_<sup>2</sup>) between each sample and each target intermediate bytes (H/L ordered):

   `cd detection_O/`  
   `./script_all.sh`  
   
   The results will be stored in `detection_O/detect_results_08.zip`, and this will also calculate the summed _R_<sup>2</sup> of those from the four member bytes to represent the value for a target 32-bit intermediate word, stored in `detection_O/detect_results_32.zip`.  
   
   Similarly, we will also calculate the values for the intermediate bytes in E/O order:
   
   `cd detection_S/`  
   `./script_all.sh`  

7. **Determine the interesting clock cycles**  
   With the _R_<sup>2</sup> for each target 32-bit word, we then determine the interesting clock cycle with a given threshold:  

   `cd ICS_extract/`  
   `./script_all.sh`  

   We used the union set of interesting clock cycles determined with the high, low, even, and odd 32-bit words in a 64-bit lane as the interesting clock cycle set for the eight bytes in such a lane. After the extraction with different thresholds, we chose the union set of the interesting clock cycle with _R_<sup>2</sup> > 0.004 (`ics_union_004.zip`) for all the later experiments.
