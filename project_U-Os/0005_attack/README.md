# Attack (Testing) stage  
We recorded 10000 traces (stored in 100 ZIP files) for testing our attack.  

1. **Generate I/O data:**  
   The folder `inter_gen/` contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. We moved the Python code into another folder `inter_gen_code/` to prevent overwriting the data we had used. Note that in these 10000 encryptions for recording, we had each 10 share the same key for extending our single-trace attack to a multi-trace attack.

3. **Download the raw traces:**  
   The 10000 raw traces are stored in 100 ZIP files. Please download the raw traces with the following commands:
   
   `cd Raw/`  
   `./script_all.sh`
   
   Alternatively, please visit our university webpage to download the files manually:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#TS  

   As mentioned we had every 10 encryptions share the same key, the first traces in `Raw/Raw_TS_0000.zip`, `Raw/Raw_TS_0010.zip`, ..., `Raw/Raw_TS_0090.zip` were recorded from encryptions with the same key, for example.  

5. **Check the raw traces and their corresponding AEAD outputs (ciphers and tags):**
   
   `cd preproc/`  
   `./script_all.sh`
   
   This will check the quality of the recorded traces against the reference trace (`0001_reference/preproc/ref_trace.npy`) as well as whether the recorded responses from the CW-Lite board are equal to our pre-calculated ciphers and tags.  

4. **Rearrange the I/O data:**  
In this attack stage, we do not need the intermediate values but only the pre-generated I/O date to verify the correctness of our recovered key by SASCA. However, for the convenience of our attack, we still rearranged the pre-generated I/O data by:  

`cd data_SASCA/`  
`./script_all.sh`  

Here we stored the 1000 key strings in 1000 separated NPY files `data_key.zip`.  
***This page is still under revision!***
<!--

<p>For the other I/O data, we stored them in:</p>

<ul>
<li><a href="U-Os/0005_attack/data_SASCA/data_nonce.zip">data_SASCA/data_nonce.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/data_SASCA/data_plaintext.zip">data_SASCA/data_plaintext.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/data_SASCA/data_ciphertag.zip">data_SASCA/data_ciphertag.zip (updated 2024-05-14)</a>,</li>
</ul>

<p>where each file contains a 10-element array that stores the data from the 10 encryptions sharing the same key with the corresponding index.</p>

5. **Downsample the raw traces**  
   With the following command lines, we downsampled the raw traces from 500 to 10 points per clock cycle (PPC) by summing up the values from every 50 consecutive samples to form the new traces:

   `cd Resample_HDF5/`  
   `./script_all.sh`  

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

   In these validation procedures, we divided the traces into four groups with equal size: G0 for the first 1000 traces, G1 for the second ones, G2 for the third ones, and G3 for the last ones. The validation results from G0 were reported and published in our paper, whereas the others were for comparison.

<h3 id=U-Os-attack>Attack (Testing) traces</h3>

<p>In this attack stage, we do not need the intermediate values but need only the pre-generated I/O date for verifying the correctness of our recovered key by SASCA. Hoever, for the convenience of our attack, we still rearranged the pre-generated I/O data with the following code:</p>

<ul>
<li><a href="U-Os/0005_attack/data_SASCA.zip">data_SASCA.zip (updated 2024-05-14)</a>,</li>
</ul>

<p>where we stored the 1000 key strings in 1000 separated NPY files:</p>

<ul>
<li><a href="U-Os/0005_attack/data_SASCA/data_key.zip">data_SASCA/data_key.zip (updated 2024-05-14)</a>.</li>
</ul>

<p>For the other I/O data, we stored them in:</p>

<ul>
<li><a href="U-Os/0005_attack/data_SASCA/data_nonce.zip">data_SASCA/data_nonce.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/data_SASCA/data_plaintext.zip">data_SASCA/data_plaintext.zip (updated 2024-05-14)</a>,</li>
<li><a href="U-Os/0005_attack/data_SASCA/data_ciphertag.zip">data_SASCA/data_ciphertag.zip (updated 2024-05-14)</a>,</li>
</ul>

<p>where each file contains a 10-element array that stores the data from the 10 encryptions sharing the same key with the corresponding index.</p>

<p>Similarly, we provide the code for downsampling:</p>

<ul>
<li><a href="U-Os/0005_attack/Resample_HDF5.zip">Resample_HDF5.zip (updated 2024-05-14)</a>,</li>
</ul>

<p>resulting in 10 HDF5 files (1000 traces for each):</p>

<ul>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_00.hdf5">Resample_HDF5/part_00.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_01.hdf5">Resample_HDF5/part_01.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_02.hdf5">Resample_HDF5/part_02.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_03.hdf5">Resample_HDF5/part_03.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_04.hdf5">Resample_HDF5/part_04.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_05.hdf5">Resample_HDF5/part_05.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_06.hdf5">Resample_HDF5/part_06.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_07.hdf5">Resample_HDF5/part_07.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_08.hdf5">Resample_HDF5/part_08.hdf5 (updated 2024-05-06)</a>,</li>
<li><a href="U-Os/0005_attack/Resample_HDF5/part_09.hdf5">Resample_HDF5/part_09.hdf5 (updated 2024-05-06)</a>,</li>
</ul>

<p>With the preprocessing steps above, we performed our attack with belief propagation based on the loopy factor graph with the following code:</p>

<ul>
<li><a href="U-Os/0005_attack/template_attack_loopy_D99_LXX.zip">template_attack_loopy_D99_LXX.zip (updated 2024-05-14)</a>.</li>
</ul>

<p>After decompressing this ZIP file, we should manually rename the directory with the number of traces (four traces for example):</p>

<ul>
<li>"template_attack_loopy_D99_LXX/" to "template_attack_loopy_D99_L04/",</li>
</ul>

<p>set the parameter "leaves" in "template_attack_loopy_D99_L04/Search_Procedure.py" (Line 13), and then execute "script_all.sh". We recorded the results for 1 to 10 traces in the following ZIP file:</p>

<ul>
<li><a href="U-Os/0005_attack/template_attack_loopy_D99_results.zip">template_attack_loopy_D99_results.zip (updated 2024-05-14)</a>.</li>
</ul>

<p>Note that we used the damping technique with a damping rate equal to 0.99. In addition to the experiment with loopy factor graphs, we also provide our code for tree-shape experiments and the results with both 8-bit and 16-bit fragments:</p>

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
