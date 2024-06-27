# Detection traces  
We recorded 16000 traces to select the points of interest (PoI) for template profiling. This is to determine whether a time sample is related to our target intermediate values. In this attack, we determined whether a _clock cycle_ is interesting instead of individual samples. The tasks in this phase are as follows.  

1. **Generate I/O date:**  
   The folder "inter\_gen/" contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. To prevent overwriting the data we had used, we moved the Python code into another folder "inter\_gen\_code/".  

2. **Download the raw traces:**  
   The 16000 raw traces are stored in 100 ZIP files. Please download the raw traces with the following commands:  
   `cd Raw/`  
   `./script_all.sh`  
   Alternatively, please visit our university webpage to manually download the files:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#DN  

3. **Check the raw traces and their corresponding AEAD outputs (ciphers and tags):**  
   `cd preproc/`  
   `./script_all.sh`  
   This will check the quality of the recorded traces against the reference trace ("0001\_reference/preproc/ref\_trace.npy") as well as whether the recorded responses from the CW-Lite board are equal to our pre-calculated ciphers and tags.

4. **Calculate our target intermediate values:**  
   With the pre-generated I/O data, we calculated all the target intermediate values and cut them into bytes. As we mentioned in our paper, the bit-interleaving (slicing) technique is applied in our target implementations. This means that a 64-bit lane of our target intermediate values will be stored in two 32-bit registers, either separated into high/low (H/L) bits or even/odd (E/O) bits.

   We first calculated the target intermediate values in 32-bit H/L words (cut into bytes):  
   `cd find_intermediates/`  
   `./script_all.sh`  

   Then we coverted the H/L data into the E/O data:  
   `cd find_intermediates_sliced/`  
   `./script_all.sh`  
   
***This page is still unfinished!***


<!--
<p>Later, the code in the following ZIP file was for calculating the sample for detection in each clock cycle: </p>

<ul>
<li><a href="U-Os/0002_detection/get_samples.zip">get_samples.zip (updated 2024-05-02)</a>,
</li>
</ul>

<p>resulting in: </p>

<ul>
<li><a href="U-Os/0002_detection/get_samples/Detect_Samples.hdf5">get_samples/Detect_Samples.hdf5 (updated 2024-05-02)</a>.
</li>
</ul>

<p>With the above proprocessed data, we then used the code in the following ZIP files to calculate the \(R^2\) values for each intermediate bytes:</p>

<ul>
<li><a href="U-Os/0002_detection/detection_O.zip">detection_O.zip (updated 2024-05-11) for H/L words</a>,</li>
<li><a href="U-Os/0002_detection/detection_S.zip">detection_S.zip (updated 2024-05-11) for E/O words</a>,</li>
</ul>

<p>resulting in: </p>

<ul>
<li><a href="U-Os/0002_detection/detection_O/detect_results_08.zip">detection_O/detect_results_08.zip (updated 2024-05-11)</a>,</li>
<li><a href="U-Os/0002_detection/detection_S/detect_results_08.zip">detection_S/detect_results_08.zip (updated 2024-05-11)</a>,</li>
</ul>

<p>as well as the \(\sum R^2\) for 32-bit words:</p>

<ul>
<li><a href="U-Os/0002_detection/detection_O/detect_results_32.zip">detection_O/detect_results_32.zip (updated 2024-05-11)</a>,</li>
<li><a href="U-Os/0002_detection/detection_S/detect_results_32.zip">detection_S/detect_results_32.zip (updated 2024-05-11)</a>.</li>
</ul>

<p>With the \(\sum R^2\) for 32-bit words, we then used the code in the following ZIP to extract the union set of interesting clock cycles for each lane of our target intermediate states:</p>

<ul>
<li><a href="U-Os/0002_detection/ICS_extract.zip">ICS_extract.zip (updated 2024-05-03)</a>.
</li>
</ul>

<p>After the extraction with different threshold, we chose the union set of the interesting clock cycle with \(\sum R^2 > 0.004\) for all the later experiments:</p>

<ul>
<li><a href="U-Os/0002_detection/ICS_extract/ics_union_004.zip">ICS_extract/ics_union_004.zip (updated 2024-05-03)</a>.
</li>
</ul>
-->
