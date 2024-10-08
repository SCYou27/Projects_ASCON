# Experiments on U-O3 data set  

When we recorded our traces for experiments, we categorized the traces into five different groups: _Reference, Detection, Profiling (Training), Validation, and Attack (Testing)_. In this repository, we **DO NOT** include our Python scripts for recording, but they can be found  in the following link:

    https://www.cl.cam.ac.uk/research/security/datasets/ascon/src_recording/CW_ASCON_O3_recording_20240528.zip

Please check our [university webpage](https://www.cl.cam.ac.uk/research/security/datasets/ascon/index.html#U-O3-recording) for any interest in recording with the same National Instruments platform.  

When we recorded our traces for experiments, we categorized the traces into the following five groups in separate subdirectories:  
 -  **0001\_reference:** to find a reference trace for recording quality checking.
 -  **0002\_detection:** to determine points of interest (PoI). 
 -  **0003\_training:** to build our templates.
 -  **0004\_validation:** to validate our templates.
 -  **0005\_attack:** to recover keys used in ASCON AEAD with our attack scenario.

## Differences between U-Os and U-O3 data sets  

The Python code and data sets for our U-O3 experiments are quite similar to those for our U-Os experiments, except for the following minor differences:

 - **Data format for raw traces:** The raw traces are stored as arrays of 8-byte floating-point numbers for the U-Os experiments, then archived in ZIP files. For the U-O3 experiments, the raw data are stored in HDF5 files instead of ZIP files. Since the oscilloscope provides only 10-bit data, storing the samples as 8-byte floating-point numbers would be a waste. Instead, we had NI oscilloscope return traces as 16-bit integer arrays along with common gain and offset floating-point values and stored them in our HDF5 files.
 - **Length of downsampled traces:** Each downsampled trace covers 2560 clock cycles in our U-O3 data sets, while it covers 2650 clock cycles in the U-Os data sets.

Please check the REAMDE.md in each subdirectory for detailed instructions.

<!--


<h3 id=U-Os-training>Profiling (Training) traces</h3>
<p>We recorded 64000 traces (stored in 400 ZIP files) for template profiling.</p>

<p>Data pre-generating, raw traces, and trace pre-processing:</p>

<ul>
<li><a href="U-Os/0003_training/inter_gen_TR.zip">inter_gen_TR.zip (updated 2024-05-01)</a>
</li>

<li><a href="U-Os/index.html#TR">Raw traces for the profiling (training) set</a>
</li>

<li><a href="U-Os/0003_training/preproc_TR.zip">preproc_TR.zip (updated 2024-05-01)</a>
</li>
</ul>

<p>Similar to the detection traces, we calculated the intermediate values from the pre-generated I/O data:</p>

<ul>
<li><a href="U-Os/0003_training/find_intermediates.zip">find_intermediates.zip (updated 2024-05-05)</a>,<br>
resulting in <a href="U-Os/0003_training/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (H/L version)</a>,</li>
<li><a href="U-Os/0003_training/find_intermediates_sliced.zip">find_intermediates_sliced.zip (updated 2024-05-05)</a>,<br>
resulting in <a href="U-Os/0003_training/find_intermediates_sliced/intermediate_values.zip">find_intermediates_sliced/intermediate_values.zip (E/O version)</a>.</li>
</ul>

<p>In addition, we also calculated the target 16-bit intermediate values for profiling the 16-bit templates:</p>

<ul>
<li><a href="U-Os/0003_training/find_intermediates_16bit.zip">find_intermediates_16bit.zip (updated 2024-05-05)</a>,<br>
resulting in <a href="U-Os/0003_training/find_intermediates_16bit/intermediate_values.zip">find_intermediates_16bit/intermediate_values.zip (H/L version)</a>.</li>
</ul>

<p>Later, we used the following code to downsample our raw traces:</p>

<ul>
<li><a href="U-Os/0003_training/Resample_HDF5.zip">Resample_HDF5.zip (updated 2024-05-03)</a>,</li>
</ul>

<p>resulting in 8 HDF5 files:</p>

<ul>
<li><a href="U-Os/0003_training/Resample_HDF5/part_00.hdf5">Resample_HDF5/part_00.hdf5 (updated 2024-05-03)</a>,</li>
<li><a href="U-Os/0003_training/Resample_HDF5/part_01.hdf5">Resample_HDF5/part_01.hdf5 (updated 2024-05-03)</a>,</li>
<li><a href="U-Os/0003_training/Resample_HDF5/part_02.hdf5">Resample_HDF5/part_02.hdf5 (updated 2024-05-03)</a>,</li>
<li><a href="U-Os/0003_training/Resample_HDF5/part_03.hdf5">Resample_HDF5/part_03.hdf5 (updated 2024-05-03)</a>,</li>
<li><a href="U-Os/0003_training/Resample_HDF5/part_04.hdf5">Resample_HDF5/part_04.hdf5 (updated 2024-05-03)</a>,</li>
<li><a href="U-Os/0003_training/Resample_HDF5/part_05.hdf5">Resample_HDF5/part_05.hdf5 (updated 2024-05-03)</a>,</li>
<li><a href="U-Os/0003_training/Resample_HDF5/part_06.hdf5">Resample_HDF5/part_06.hdf5 (updated 2024-05-03)</a>,</li>
<li><a href="U-Os/0003_training/Resample_HDF5/part_07.hdf5">Resample_HDF5/part_07.hdf5 (updated 2024-05-03)</a>.</li>
</ul>

<p>After all the preprocessing steps above, we profiled our templates with the following code:</p>

<ul>
<li>8-bit templates with H/L bit order: <a href="U-Os/0003_training/template_profiling_bytes_O.zip">template_profiling_bytes_O.zip (updated 2024-05-04)</a>,</li>
<li>8-bit templates with E/O bit order: <a href="U-Os/0003_training/template_profiling_bytes_S.zip">template_profiling_bytes_S.zip (updated 2024-05-04)</a>,</li>
<li>selected 16-bit templates with H/L bit order: <a href="U-Os/0003_training/template_profiling_16bits_O.zip">template_profiling_16bits_O.zip (updated 2024-05-05)</a>,</li>
</ul>

<p>resulting in:</p>

<ul>
<li><a href="U-Os/0003_training/template_profiling_bytes_O/templateLDA_O004.zip">template_profiling_bytes_O/templateLDA_O004.zip (updated 2024-05-04)</a>,</li>
<li><a href="U-Os/0003_training/template_profiling_bytes_S/templateLDA_O004.zip">template_profiling_bytes_S/templateLDA_O004.zip (updated 2024-05-04)</a>,</li>
<li><a href="U-Os/0003_training/template_profiling_16bits_O/templateLDA_O004_16bit.zip">template_profiling_16bits_O/templateLDA_O004_16bit.zip (updated 2024-05-05)</a>,</li>
</ul>


<h3 id=U-Os-validation>Validation traces</h3>
<p>We recorded 4000 traces (stored in 40 ZIP files) for template quality validation.</p>

<p>Data pre-generating, raw traces, and trace pre-processing:</p>

<ul>
<li><a href="U-Os/0004_validation/inter_gen_VA.zip">inter_gen_VA.zip (updated 2024-05-02)</a>
</li>

<li><a href="U-Os/index.html#VA">Raw traces for the validation set</a>
</li>

<li><a href="U-Os/0004_validation/preproc_VA.zip">preproc_VA.zip (updated 2024-05-02)</a>
</li>
</ul>

<p>Code for intermediate value calculation:</p>

<ul>
<li><a href="U-Os/0004_validation/find_intermediates.zip">find_intermediates.zip (updated 2024-05-05)</a>,<br>
resulting in <a href="U-Os/0004_validation/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (H/L version)</a>,</li>
<li><a href="U-Os/0004_validation/find_intermediates_sliced.zip">find_intermediates_sliced.zip (updated 2024-05-05)</a>,<br>
resulting in <a href="U-Os/0004_validation/find_intermediates_sliced/intermediate_values.zip">find_intermediates_sliced/intermediate_values.zip (E/O version)</a>,</li>
<li><a href="U-Os/0004_validation/find_intermediates_16bit.zip">find_intermediates_16bit.zip (updated 2024-05-05)</a>,<br>
resulting in <a href="U-Os/0004_validation/find_intermediates_16bit/intermediate_values.zip">find_intermediates_16bit/intermediate_values.zip (H/L version)</a>.</li>
</ul>

<p>Code for downsampling:</p>

<ul>
<li><a href="U-Os/0004_validation/Resample_HDF5.zip">Resample_HDF5.zip (updated 2024-05-04)</a>,</li>
</ul>

<p>resulting in 4 HDF5 files (1000 traces for each):</p>

<ul>
<li><a href="U-Os/0004_validation/Resample_HDF5/part_00.hdf5">Resample_HDF5/part_00.hdf5 (updated 2024-05-04)</a>,</li>
<li><a href="U-Os/0004_validation/Resample_HDF5/part_01.hdf5">Resample_HDF5/part_01.hdf5 (updated 2024-05-04)</a>,</li>
<li><a href="U-Os/0004_validation/Resample_HDF5/part_02.hdf5">Resample_HDF5/part_02.hdf5 (updated 2024-05-04)</a>,</li>
<li><a href="U-Os/0004_validation/Resample_HDF5/part_03.hdf5">Resample_HDF5/part_03.hdf5 (updated 2024-05-04)</a>,</li>
</ul>

<p>With the preprocessing steps above, we validated the quality of our templates by calculating the first-order success rate (1-SR) and logarithmic guessing entropy (LGE) with the following code:</p>

<ul>
<li><a href="U-Os/0004_validation/template_validation_bytes_O.zip">template_validation_bytes_O.zip (updated 2024-05-18)</a>,</li>
<li><a href="U-Os/0004_validation/template_validation_bytes_S.zip">template_validation_bytes_S.zip (updated 2024-05-18)</a>,</li>
<li><a href="U-Os/0004_validation/template_validation_16bits_O.zip">template_validation_16bits_O.zip (updated 2024-05-18)</a>.</li>
</ul>

<p>The rank of the correct candidate for the target intermeidate values are recorded in:</p>

<ul>
<li><a href="U-Os/0004_validation/template_validation_bytes_O/Rank_O004.zip">template_validation_bytes_O/Rank_O004.zip (updated 2024-05-18)</a>,</li>
<li><a href="U-Os/0004_validation/template_validation_bytes_S/Rank_O004.zip">template_validation_bytes_S/Rank_O004.zip (updated 2024-05-18)</a>,</li>
<li><a href="U-Os/0004_validation/template_validation_16bits_O/Rank_O004.zip">template_validation_16bits_O/Rank_O004.zip (updated 2024-05-18)</a>.</li>
</ul>

<p>Note that the numbers recorded in these NumPy arrays are actually the indeces (starting from 0) of the sorted probability tables of the correct candidates instead of the ranks (starting from 1). We fixed such difference when calculating the 1-SR and LGE with the results from 1000 traces:</p>

<ul>
<li><a href="U-Os/0004_validation/template_validation_bytes_O/Result_Tables.zip">template_validation_bytes_O/Result_Tables.zip (updated 2024-05-18)</a>,</li>
<li><a href="U-Os/0004_validation/template_validation_bytes_S/Result_Tables.zip">template_validation_bytes_S/Result_Tables.zip (updated 2024-05-18)</a>,</li>
<li><a href="U-Os/0004_validation/template_validation_16bits_O/Result_Tables.zip">template_validation_16bits_O/Result_Tables.zip (updated 2024-05-18)</a>.</li>
</ul>

<p>We published a subsets of the results from the first 1000 traces (part_00.hdf5, labelled as G0). For example, we can access the 1-SR and LGE of the key in "Result_Tables/SR_table_KEY_G0.txt" and "Result_Tables/GE_table_KEY_G0.txt", respectively.</p>

<h3 id=U-Os-attack>Attack (Testing) traces</h3>
<p>We recorded 10000 traces (stored in 100 ZIP files) for our SASCA attacks.</p>

<p>Data pre-generating, raw traces, and trace pre-processing:</p>

<ul>
<li><a href="U-Os/0005_attack/inter_gen_TS.zip">inter_gen_TS.zip (updated 2024-05-02)</a>
</li>

<li><a href="U-Os/index.html#TS">Raw traces for the attack (testing) set</a>
</li>

<li><a href="U-Os/0005_attack/preproc_TS.zip">preproc_TS.zip (updated 2024-05-02)</a>
</li>
</ul>

<p>Note that in these 10000 encryptions for recording, we had each 10 share the same key. For example, the first traces in "Raw/Raw_TS_0000.zip", "Raw/Raw_TS_0010.zip", ..., "Raw/Raw_TS_0090.zip" were recorded from encryptions with the same key.</p>

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

