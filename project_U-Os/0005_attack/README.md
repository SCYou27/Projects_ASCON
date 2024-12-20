# Attack (Testing) stage  
We recorded 10000 traces (stored in 100 ZIP files) for testing our attack.  

1. **Generate I/O data:**  
   The folder `inter_gen/` contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. We moved the Python code into another folder `inter_gen_code/` to prevent overwriting the data we had used. Note that in these 10000 encryptions for recording, we had each 10 share the same key for extending our single-trace attack to a multi-trace attack.

2. **Download the raw traces:**  
   The 10000 raw traces are stored in 100 ZIP files. Please download the raw traces with the following commands:
   
   `cd Raw/`  
   `./script_all.sh`
   
   Alternatively, please visit our university webpage to download the files manually:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#TS  

   As mentioned we had every 10 encryptions share the same key, the first traces in `Raw/Raw_TS_0000.zip`, `Raw/Raw_TS_0010.zip`, ..., `Raw/Raw_TS_0090.zip` were recorded from encryptions with the same key, for example.  

3. **Check the raw traces and their corresponding AEAD outputs (ciphers and tags):**
   
   `cd preproc/`  
   `./script_all.sh`
   
   This will check the quality of the recorded traces against the reference trace (`0001_reference/preproc/ref_trace.npy`) as well as whether the recorded responses from the CW-Lite board are equal to our pre-calculated ciphers and tags.  

4. **Rearrange the I/O data:**  
   In this attack stage, we do not need the intermediate values but only the pre-generated I/O data to feed into the belief propagation procedure as the known data (the plaintexts, nonces, ciphertexts, and tags), or as the reference (the pre-generated key strings) to verify the correctness of our recovered keys. However, for the convenience of our attack, we still rearranged these pre-generated I/O data by:  
   
   `cd data_SASCA/`  
   `./script_all.sh`  
   
   Here we stored the 1000 key strings in 1000 separated NPY files in `data_SASCA/data_key.zip`. For the other I/O data, we stored them in `data_SASCA/data_nonce.zip`, `data_SASCA/data_plaintext.zip`, and `data_SASCA/data_ciphertag.zip`, where each NPY file contains a 10-element array that stores the same type of data from the 10 encryptions sharing the same key with the corresponding index.

   Besides, as a preparation for the later histogram-based key-rank estimation, we also cut the key strings into 1-bit, 8-bit, and 16-bit fragments:  
   
   `cd data_fragments/`  
   `./script_all.sh`  
   
5. **Downsample the raw traces**  
   With the following command lines, we downsampled the raw traces from 500 to 10 points per clock cycle (PPC) by summing up the values from every 50 consecutive samples to form the new traces:

   `cd Resample_HDF5/`  
   `./script_all.sh`
   
6. **Generate probability tables with template attack and belief propagation**  
   We generated probability tables with four different scenarios as follows:  
   - Tables for 8-bit key fragments with probabilities estimated by only key templates (the _key_ attack)  
   - Tables for 8-bit key fragments with probabilities estimated after belief propagation on information from templates for the key and intermediate values involved in the tag generation step (the _byte_ attack)  
   - Tables for 16-bit key fragments with probabilities estimated after belief propagation on information from templates for the key and intermediate values involved in the tag generation step (the _16-bit_ attack)  
   - Tables for 1-bit key fragments with probabilities estimated after loopy belief propagation on marginalized information from templates for all targeted intermediate values in a full AEAD procedure (the _loopy_ attack)

   _key attack_:  
   `cd template_attack_keys_O_TABLES/`  
   `./script_all.sh`

   _byte attack_:  
   `cd template_attack_bytes_O_TABLES/`  
   `./script_all.sh`  

   _16-bit attack_:  
   `cd template_attack_16bits_O_TABLES/`  
   `./script_all.sh`

   _loopy attack with a single trace_:  
   `cd template_attack_loopy_D99_TABLES_L01/`  
   `./script_all.sh`  

   _loopy attack with multiple traces_:  
   `cd template_attack_loopy_D99_TABLES_LXX/` (`"XX"={"02","03",...,"10"}`)  
   `./script_all.sh`  

7. **Key enumeration**  
   With the probability tables, we apply the key enumeration algorithm to enumerate up to 100000 candidates to estimate the success rate within this computation capacity. We implement this enumeration step assuming that the attacker can access only a pair of plaintext and cipher+tag.   

   _byte attack_:  
   `cd key_enumeration_bytes/`  
   `./script_all.sh`  

   _16-bit attack_:  
   `cd key_enumeration_16bits/`  
   `./script_all.sh`  

   _loopy attack_:  
   `cd key_enumeration_loopy/`  
   `./script_all.sh`  

8. **Rank estimation**  
   We apply the histogram-based rank estimate algorithm to evaluate our attacks.   

   _key attack_:  
   `cd key_rank_estimate_keys/`  
   `./script_all.sh`  

   _byte attack_:  
   `cd key_rank_estimate_bytes/`  
   `./script_all.sh`  

   _16-bit attack_:  
   `cd key_rank_estimate_16bits/`  
   `./script_all.sh`  

   _loopy attack_:  
   `cd key_rank_estimate_loopy/`  
   `./script_all.sh`  

<!--
***This page is still under revision!***
<ul>
<li>"template_attack_loopy_D99_LXX/" to "template_attack_loopy_D99_L04/",</li>
</ul>

<p>set the parameter "leaves" in "template_attack_loopy_D99_L04/Search_Procedure.py" (Line 13), and then execute "script_all.sh". We recorded the results for 1 to 10 traces in the following ZIP file:</p>

<ul>
<li><a href="U-Os/0005_attack/template_attack_loopy_D99_results.zip">template_attack_loopy_D99_results.zip (updated 2024-05-14)</a>.</li>
</ul>

<p>Note that we used the damping technique with a damping rate of 0.99. In addition to the experiment with loopy factor graphs, we also provide our code for tree-shape experiments and the results with both 8-bit and 16-bit fragments:</p>

<ul>
<li><a href="U-Os/0005_attack/template_attack_bytes_O.zip">template_attack_bytes_O.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_bytes_O_results.zip">template_attack_bytes_O_results.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O.zip">template_attack_16bits_O.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_results.zip">template_attack_16bits_O_results.zip (updated 2024-05-14)</a>.</li>
</ul>

<p>While the above codes were mostly based on Python and enumerated up to the first 100,000 key candidates, the final version of the results is a hybrid evaluation, which is the actual key enumeration before the first \($2^24$\) candidates as well as a rank estimate result afterwards. With the procedure of key enumeration and rank estimate later implemented in Julia, we still relied on the following Python code for the probability tables after belief propagation:</p>

<ul>
<li><a href="U-Os/0005_attack/template_attack_loopy_D99_TABLES_LXX.zip">template_attack_loopy_D99_TABLES_LXX.zip (updated 2024-05-16)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_bytes_O_TABLES.zip">template_attack_bytes_O_TABLES.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES.zip">template_attack_16bits_O_TABLES.zip (updated 2024-05-14)</a>,</li>
</ul>

<p>and then the resulting tables are stored in the following ZIP files:</p>

<ul>
<li><a href="U-Os/0005_attack/template_attack_loopy_D99_TABLES_results.zip">template_attack_loopy_D99_TABLES_results.zip (updated 2024-05-16)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_bytes_O_TABLES/Tables.zip">template_attack_bytes_O_TABLES/Tables.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L01.zip">template_attack_16bits_O_TABLES/Tables_L01.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L02.zip">template_attack_16bits_O_TABLES/Tables_L02.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L03.zip">template_attack_16bits_O_TABLES/Tables_L03.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L04.zip">template_attack_16bits_O_TABLES/Tables_L04.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L05.zip">template_attack_16bits_O_TABLES/Tables_L05.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L06.zip">template_attack_16bits_O_TABLES/Tables_L06.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L07.zip">template_attack_16bits_O_TABLES/Tables_L07.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L08.zip">template_attack_16bits_O_TABLES/Tables_L08.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L09.zip">template_attack_16bits_O_TABLES/Tables_L09.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/template_attack_16bits_O_TABLES/Tables_L10.zip">template_attack_16bits_O_TABLES/Tables_L10.zip (updated 2024-05-14)</a>,</li>
</ul>

<p>The remaining source code for our implementation of key enumeration and rank estimate will be released here soon ...</p>
-->

