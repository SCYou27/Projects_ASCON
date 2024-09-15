# Experiments on U-Os data set  

When we recorded our traces for experiments, we categorized the traces into five different groups: _Reference, Detection, Profiling (Training), Validation, and Attack (Testing)_. In this repository, we **DO NOT** include our Python scripts for recording, but they can be found  in the following link:

    https://www.cl.cam.ac.uk/research/security/datasets/ascon/src_recording/CW_ASCON_recording_20240414.zip

Please check our [university webpage](https://www.cl.cam.ac.uk/research/security/datasets/ascon/index.html#U-Os-recording) for any interest in recording with the same National Instruments platform.  

When we recorded our traces for experiments, we categorized the traces into the following five groups in separate subdirectories:  
 -  **0001\_reference:** to find a reference trace for recording quality checking.
 -  **0002\_detection:** to determine points of interest (PoI). 
 -  **0003\_training:** to build our templates.
 -  **0004\_validation:** to validate our templates.
 -  **0005\_attack:** to recover keys used in ASCON AEAD with our attack scenario.

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

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang=en>
<head>
<title>ASCON dataset: building templates for recovering ASCON keys</title>
<script type="text/javascript" src="https://www.cl.cam.ac.uk/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<h1>ASCON dataset: building templates for recovering ASCON keys</h1>

<p>The ASCON dataset contains recordings of the power-supply current changes of the 32-bit processor STM32F303RCT7, which has one
ARM Cortex-M4 core, on a <a href="https://media.newae.com/datasheets/NAE-CW1173_datasheet.pdf"> ChipWhisperer-Lite (CW-Lite) board</a>.
We used an <a href="https://www.ni.com/en-gb/support/model.pxie-5160.html">NI PXIe-5160 10-bit oscilloscope</a>,
which can sample at 2.5 GS/s into 2 GB of sampling memory, and an <a href="https://www.ni.com/en-gb/support/model.pxie-5423.html">
NI PXIe-5423 wave generator</a>, as an external clock signal source, to supply the target board with a 5 MHz square wave signal.

<p>More details of the attack are described in the following paper and thesis:

<ul>
<li>Shih-Chun You, Markus G. Kuhn, Sumanta Sarkar, Feng
Hao: <a href="https://doi.org/10.46586/tches.v2023.i4.344-366">Low
trace-count template attacks on 32-bit implementations of ASCON
AEAD</a>.
<a href="https://tches.iacr.org/">IACR Transactions on Cryptographic Hardware and Embedded Systems (TCHES)</a>, 
Volume 2023, Issue 4 (<a href="TCHES2023_4_14.pdf">PDF file</a>).</li>

<li>Shih-Chun You: <a href="https://doi.org/10.17863/CAM.100592">Single-trace template attacks on permutation-based cryptography</a>.
PhD thesis, 2022, Apollo - University of Cambridge Repository (<a href="PhD_thesis.pdf">PDF file</a>).
</li>
</ul>

<p>On this web page, we provide <a href="#source">our target source code</a> and <a href="#recording">the Python scripts for recording the traces on the NI platform</a>.

<p>The scripts that perform and evaluate the template attacks can be found at:</p>

<ul><li><a href="https://github.com/SCYou27/Projects_ASCON">https://github.com/SCYou27/Projects_ASCON</a></li></ul>

<h2 id=source>Source code for our targets</h2>

<p>The source code of the ASCON AEAD implementations on CW-Lite is available below.</p>

<ul>
<li><a href="src_recording/ascon_src_website.zip">ascon_src_website.zip (updated: 2024-04-12)</a>
</li>
</ul>

<p>With the parameters and software version that we stated in our paper, you can find the following compiled HEX files for three different versions of ASCON-128 implementations after decompressing the above ZIP file:</p>

<ul>
<li><b>U-Os experiments,</b> an unmasked implementation with compiler optimization option "-Os":<br>
ascon_src/simpleserial-ascon-aead-128/simpleserial-aead-CWLITEARM.hex</li>
<li><b>U-O3 experiments,</b> an unmasked implementation with compiler optimization option "-O3":<br>
ascon_src/simpleserial-ascon-aead-128-O3/simpleserial-aead-CWLITEARM.hex</li>
<li><b>M-Os experiments,</b> a masked implementation with compiler optimization option "-Os":<br>
ascon_src/simpleserial-masked-ascon-aead-128/simpleserial-aead-CWLITEARM.hex</li>
</ul>

<h2 id=recording>Recording scripts</h2>

<h3 id=U-Os-recording>U-Os recordings</h3>

<p>The Python scripts to control the recording platform is available below.</p>

<ul>
<li><a href="src_recording/CW_ASCON_recording_20240414.zip">CW_ASCON_recording_20240414.zip</a>
</li>
</ul>

<p>When we recorded our traces for experiments, we categorized the traces into five different groups: Reference, Detection, Profiling (Training), Validation, and Attack (Testing). For each there is an independent subdirectroy, which contains the recording control scripts, the pre-generated input data (key, nonces, plaintexts), and the corresponding output data (ciphertexts and tags) for checking:</p>

<ul>
<li><b>NI_RE_code:</b> Reference traces,</li>
<li><b>NI_DN_code:</b> Detection traces,</li>
<li><b>NI_TR_code:</b> Profiling (Training) traces,</li>
<li><b>NI_VA_code:</b> Validation traces,</li>
<li><b>NI_TS_code:</b> Attack (Testing) traces.</li>
</ul>

<p>Meanwhile, the subdirectory "SRC_TEST/simpleserial-ascon-aead-128/" contains the target HEX file, and please execute the following command to write the HEX file onto the CW-Lite board and check the correctness of the implementation:</p>

<ul><li>python3 test_AEAD_128_Enc.py</li></ul>

<h3 id=U-O3-recording>U-O3 recordings</h3>

<p>The Python scripts to control the recording platform is available below.</p>

<ul>
<li><a href="src_recording/CW_ASCON_O3_recording_20240528.zip">CW_ASCON_O3_recording_20240528.zip</a>
</li>
</ul>

<p>When we recorded our traces for experiments, we categorized the traces into five different groups: Reference, Detection, Profiling (Training), Validation, and Attack (Testing). For each there is an independent subdirectroy, which contains the recording control scripts, the pre-generated input data (key, nonces, plaintexts), and the corresponding output data (ciphertexts and tags) for checking:</p>

<ul>
<li><b>NI_RE_code:</b> Reference traces,</li>
<li><b>NI_DN_code:</b> Detection traces,</li>
<li><b>NI_TR_code:</b> Profiling (Training) traces,</li>
<li><b>NI_VA_code:</b> Validation traces,</li>
<li><b>NI_TS_code:</b> Attack (Testing) traces.</li>
</ul>

<p>Meanwhile, the subdirectory "simpleserial-ascon-aead-128-O3/" contains the target HEX file, and please execute the following command to write the HEX file onto the CW-Lite board and check the correctness of the implementation:</p>

<ul><li>python3 test_AEAD_128_Enc.py</li></ul>

<!--

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

<h2 id=U-O3>U-O3 experiments</h2>
<p>The codes and data sets for our U-O3 experiments are quite similar to the U-Os experiments, expect for the following minor differences:</p>

<ul>
<li>For the U-Os expeimnents, the raw traces are stored as arrays of 8-byte floating-point numbers, then being archived in ZIP files. For the U-O3 experiments, the raw data are stored in HDF5 files instead of ZIP files. Since the oscilloscope provides only 10-bit data, it would be a waste if we store the samples as 8-byte floating-point numbers. Instead, we had NI oscilloscope return traces as 16-bit integer arrays along with common gain and offset floating-point values and stored them in our HDF5 files.</li>
<li>Each downsampled trace covers 2560 clock cycles in our U-O3 data sets, while it covers 2650 clock cycles in the U-Os data sets.</li>
</ul>


<h3 id=U-O3-recording>Code for recording on the NI platform</h3>

<p>The Python scripts to control the recording platform:</p>

<ul>
<li><a href="src_recording/CW_ASCON_O3_recording_20240528.zip">CW_ASCON_O3_recording_20240528.zip</a>
</li>
</ul>


<h3 id=U-O3-reference>Reference traces</h3>

<p>I/O data pre-generation, raw traces, and reference trace generation:</p>

<ul>
<li><a href="U-O3/0001_reference/inter_gen_RE.zip">inter_gen_RE.zip (updated 2024-05-21)</a>
</li>
<li><a href="U-O3/index.html#RE">Raw traces for the reference set</a>
</li>
<li><a href="U-O3/0001_reference/preproc_RE.zip">preproc_RE.zip (updated 2024-05-21)</a>
</li>
</ul>

<h3 id=U-O3-detection>Detection traces</h3>

<p>I/O data pre-generation, raw traces, and trace quality checking:</p>

<ul>
<li><a href="U-O3/0002_detection/inter_gen_DN.zip">inter_gen_DN.zip (updated 2024-05-21)</a>
</li>
<li><a href="U-O3/index.html#DN">Raw traces for the detection set</a>
</li>
<li><a href="U-O3/0002_detection/preproc_DN.zip">preproc_DN.zip (updated 2024-05-21)</a>
</li>
</ul>

<p>Intermediate value calculation (both H/L and E/O groupings):</p>

<ul>
<li><a href="U-O3/0002_detection/find_intermediates.zip">find_intermediates.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0002_detection/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (H/L version, updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0002_detection/find_intermediates_sliced.zip">find_intermediates_sliced.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0002_detection/find_intermediates_sliced/intermediate_values.zip">find_intermediates_sliced/intermediate_values.zip (E/O version, updated 2024-05-21)</a>.</li>
</ul>


<p>Sample generation for detection: </p>

<ul>
<li><a href="U-O3/0002_detection/get_samples.zip">get_samples.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0002_detection/get_samples/Detect_Samples.hdf5">get_samples/Detect_Samples.hdf5 (updated 2024-05-21)</a>.</li>
</ul>

<p>Resulting \(R^2\) values after detection:</p>

<ul>
<li><a href="U-O3/0002_detection/detection_O.zip">detection_O.zip (updated 2024-05-21) for H/L words</a>,</li>
<li><a href="U-O3/0002_detection/detection_O/detect_results_08.zip">detection_O/detect_results_08.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0002_detection/detection_O/detect_results_32.zip">detection_O/detect_results_32.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0002_detection/detection_S.zip">detection_S.zip (updated 2024-05-21) for E/O words</a>,</li>
<li><a href="U-O3/0002_detection/detection_S/detect_results_08.zip">detection_S/detect_results_08.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0002_detection/detection_S/detect_results_32.zip">detection_S/detect_results_32.zip (updated 2024-05-21)</a>.</li>
</ul>

<p>Interesting clock cycles extraction for a given threshold:</p>

<ul>
<li><a href="U-O3/0002_detection/ICS_extract.zip">ICS_extract.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0002_detection/ICS_extract/ics_union_004.zip">ICS_extract/ics_union_004.zip (updated 2024-05-21)</a>.</li>
</ul>

<h3 id=U-O3-training>Profiling (Training) traces</h3>

<p>I/O data pre-generation, raw traces, and trace quality checking:</p>

<ul>
<li><a href="U-O3/0003_training/inter_gen_TR.zip">inter_gen_TR.zip (updated 2024-05-21)</a>
</li>
<li><a href="U-O3/index.html#TR">Raw traces for the profiling (training) set</a>
</li>
<li><a href="U-O3/0003_training/preproc_TR.zip">preproc_TR.zip (updated 2024-05-21)</a>
</li>
</ul>

<p>Intermediate value calculation (H/L and E/O bytes as well as H/L 16-bit fragments):</p>

<ul>
<li><a href="U-O3/0003_training/find_intermediates.zip">find_intermediates.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (H/L version)</a>,</li>
<li><a href="U-O3/0003_training/find_intermediates_sliced.zip">find_intermediates_sliced.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/find_intermediates_sliced/intermediate_values.zip">find_intermediates_sliced/intermediate_values.zip (E/O version)</a>,</li>
<li><a href="U-O3/0003_training/find_intermediates_16bit.zip">find_intermediates_16bit.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/find_intermediates_16bit/intermediate_values.zip">find_intermediates_16bit/intermediate_values.zip (H/L version)</a>.</li>
</ul>

<p>Trace downsampling:</p>

<ul>
<li><a href="U-O3/0003_training/Resample_HDF5.zip">Resample_HDF5.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/Resample_HDF5/part_00.hdf5">Resample_HDF5/part_00.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/Resample_HDF5/part_01.hdf5">Resample_HDF5/part_01.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/Resample_HDF5/part_02.hdf5">Resample_HDF5/part_02.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/Resample_HDF5/part_03.hdf5">Resample_HDF5/part_03.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/Resample_HDF5/part_04.hdf5">Resample_HDF5/part_04.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/Resample_HDF5/part_05.hdf5">Resample_HDF5/part_05.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/Resample_HDF5/part_06.hdf5">Resample_HDF5/part_06.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/Resample_HDF5/part_07.hdf5">Resample_HDF5/part_07.hdf5 (updated 2024-05-21)</a>.</li>
</ul>

<p>Template profiling codes:</p>

<ul>
<li>8-bit templates with H/L bit order: <a href="U-O3/0003_training/template_profiling_bytes_O.zip">template_profiling_bytes_O.zip (updated 2024-05-21)</a>,</li>
<li>8-bit templates with E/O bit order: <a href="U-O3/0003_training/template_profiling_bytes_S.zip">template_profiling_bytes_S.zip (updated 2024-05-21)</a>,</li>
<li>selected 16-bit templates with H/L bit order: <a href="U-O3/0003_training/template_profiling_16bits_O.zip">template_profiling_16bits_O.zip (updated 2024-05-21)</a>.</li>
</ul>

<p>Resulting Templates:</p>

<ul>
<li><a href="U-O3/0003_training/template_profiling_bytes_O/templateLDA_O004.zip">template_profiling_bytes_O/templateLDA_O004.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/template_profiling_bytes_S/templateLDA_O004.zip">template_profiling_bytes_S/templateLDA_O004.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0003_training/template_profiling_16bits_O/templateLDA_O004_16bit.zip">template_profiling_16bits_O/templateLDA_O004_16bit.zip (updated 2024-05-21)</a>.</li>
</ul>


<h3 id=U-O3-validation>Validation traces</h3>

<p>I/O data pre-generation, raw traces, and trace quality checking:</p>

<ul>
<li><a href="U-O3/0004_validation/inter_gen_VA.zip">inter_gen_VA.zip (updated 2024-05-21)</a>
</li>
<li><a href="U-O3/index.html#VA">Raw traces for the validation set</a>
</li>
<li><a href="U-O3/0004_validation/preproc_VA.zip">preproc_VA.zip (updated 2024-05-21)</a>
</li>
</ul>

<p>Intermediate value calculation (H/L and E/O bytes as well as H/L 16-bit fragments):</p>

<ul>
<li><a href="U-O3/0004_validation/find_intermediates.zip">find_intermediates.zip (updated 2024-05-21)</a>,</li>
<li> <a href="U-O3/0004_validation/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (H/L version)</a>,</li>
<li><a href="U-O3/0004_validation/find_intermediates_sliced.zip">find_intermediates_sliced.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/find_intermediates_sliced/intermediate_values.zip">find_intermediates_sliced/intermediate_values.zip (E/O version)</a>,</li>
<li><a href="U-O3/0004_validation/find_intermediates_16bit.zip">find_intermediates_16bit.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/find_intermediates_16bit/intermediate_values.zip">find_intermediates_16bit/intermediate_values.zip (H/L version)</a>.</li>
</ul>

<p>Trace downsampling:</p>

<ul>
<li><a href="U-O3/0004_validation/Resample_HDF5.zip">Resample_HDF5.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/Resample_HDF5/part_00.hdf5">Resample_HDF5/part_00.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/Resample_HDF5/part_01.hdf5">Resample_HDF5/part_01.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/Resample_HDF5/part_02.hdf5">Resample_HDF5/part_02.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/Resample_HDF5/part_03.hdf5">Resample_HDF5/part_03.hdf5 (updated 2024-05-21)</a>.</li>
</ul>

<p>Template validation codes:</p>

<ul>
<li><a href="U-O3/0004_validation/template_validation_bytes_O.zip">template_validation_bytes_O.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/template_validation_bytes_S.zip">template_validation_bytes_S.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/template_validation_16bits_O.zip">template_validation_16bits_O.zip (updated 2024-05-21)</a>.</li>
</ul>

<p>The resulting "indeces":</p>

<ul>
<li><a href="U-O3/0004_validation/template_validation_bytes_O/Rank_O004.zip">template_validation_bytes_O/Rank_O004.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/template_validation_bytes_S/Rank_O004.zip">template_validation_bytes_S/Rank_O004.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/template_validation_16bits_O/Rank_O004.zip">template_validation_16bits_O/Rank_O004.zip (updated 2024-05-21)</a>.</li>
</ul>

<p>The resulting 1-SR and LGE:</p>

<ul>
<li><a href="U-O3/0004_validation/template_validation_bytes_O/Result_Tables.zip">template_validation_bytes_O/Result_Tables.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/template_validation_bytes_S/Result_Tables.zip">template_validation_bytes_S/Result_Tables.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0004_validation/template_validation_16bits_O/Result_Tables.zip">template_validation_16bits_O/Result_Tables.zip (updated 2024-05-21)</a>.</li>
</ul>

<h3 id=U-O3-attack>Attack (Testing) traces</h3>

<p>I/O data pre-generation, raw traces, and trace quality checking:</p>

<ul>
<li><a href="U-O3/0005_attack/inter_gen_TS.zip">inter_gen_TS.zip (updated 2024-05-21)</a>
</li>
<li><a href="U-O3/index.html#TS">Raw traces for the attack (testing) set</a>
</li>
<li><a href="U-O3/0005_attack/preproc_TS.zip">preproc_TS.zip (updated 2024-05-21)</a>
</li>
</ul>

<p>I/O data rearrangement:</p>

<ul>
<li><a href="U-O3/0005_attack/data_SASCA.zip">data_SASCA.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/data_SASCA/data_key.zip">data_SASCA/data_key.zip (updated 2024-05-21)</a>.</li>
<li><a href="U-O3/0005_attack/data_SASCA/data_nonce.zip">data_SASCA/data_nonce.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/data_SASCA/data_plaintext.zip">data_SASCA/data_plaintext.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/data_SASCA/data_ciphertag.zip">data_SASCA/data_ciphertag.zip (updated 2024-05-21)</a>.</li>
</ul>

<p>Trace downsampling:</p>

<ul>
<li><a href="U-O3/0005_attack/Resample_HDF5.zip">Resample_HDF5.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_00.hdf5">Resample_HDF5/part_00.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_01.hdf5">Resample_HDF5/part_01.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_02.hdf5">Resample_HDF5/part_02.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_03.hdf5">Resample_HDF5/part_03.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_04.hdf5">Resample_HDF5/part_04.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_05.hdf5">Resample_HDF5/part_05.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_06.hdf5">Resample_HDF5/part_06.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_07.hdf5">Resample_HDF5/part_07.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_08.hdf5">Resample_HDF5/part_08.hdf5 (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/Resample_HDF5/part_09.hdf5">Resample_HDF5/part_09.hdf5 (updated 2024-05-21)</a>.</li>
</ul>

<p>Full attack procedure with template attack, belief propagation, and key enumeration:</p>

<ul>
<li><a href="U-O3/0005_attack/template_attack_loopy_D99_LXX.zip">template_attack_loopy_D99_LXX.zip (updated 2024-05-21)</a>.</li>
<li><a href="U-O3/0005_attack/template_attack_loopy_D99_results.zip">template_attack_loopy_D99_results.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_bytes_O.zip">template_attack_bytes_O.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_bytes_O_results.zip">template_attack_bytes_O_results.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O.zip">template_attack_16bits_O.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_results.zip">template_attack_16bits_O_results.zip (updated 2024-05-21)</a>.</li>
</ul>

<p>Python code for the probability tables after belief propagation:</p>

<ul>
<li><a href="U-O3/0005_attack/template_attack_loopy_D99_TABLES_LXX.zip">template_attack_loopy_D99_TABLES_LXX.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_bytes_O_TABLES.zip">template_attack_bytes_O_TABLES.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES.zip">template_attack_16bits_O_TABLES.zip (updated 2024-05-21)</a>.</li>
</ul>

<p>Tables for later key enumeration and rank estimate implemented in Julia:</p>

<ul>
<li><a href="U-O3/0005_attack/template_attack_loopy_D99_TABLES_results.zip">template_attack_loopy_D99_TABLES_results.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_bytes_O_TABLES/Tables.zip">template_attack_bytes_O_TABLES/Tables.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L01.zip">template_attack_16bits_O_TABLES/Tables_L01.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L02.zip">template_attack_16bits_O_TABLES/Tables_L02.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L03.zip">template_attack_16bits_O_TABLES/Tables_L03.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L04.zip">template_attack_16bits_O_TABLES/Tables_L04.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L05.zip">template_attack_16bits_O_TABLES/Tables_L05.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L06.zip">template_attack_16bits_O_TABLES/Tables_L06.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L07.zip">template_attack_16bits_O_TABLES/Tables_L07.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L08.zip">template_attack_16bits_O_TABLES/Tables_L08.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L09.zip">template_attack_16bits_O_TABLES/Tables_L09.zip (updated 2024-05-21)</a>,</li>
<li><a href="U-O3/0005_attack/template_attack_16bits_O_TABLES/Tables_L10.zip">template_attack_16bits_O_TABLES/Tables_L10.zip (updated 2024-05-21)</a>.</li>
</ul>

<p>The remaining source code for our implementation of key enumeration and rank estimate will be released here soon ...</p>


<h2 id=M-Os>M-Os experiments</h2>
<h3 id=M-Os-recording>Code for recording on the NI platform</h3>

<p>The Python scripts to control the recording platform:</p>

<ul>
<li><a href="src_recording/CW_ASCON_masked_20240528.zip">CW_ASCON_masked_20240528.zip</a>
</li>
</ul>

<p>We found it required a window with 18000 clock cycles to cover a complete encrypotion with the masked implementation optimized for space. Given that we only targeted the clockc cycles that were related to the operations on keys and tag generation, it was not necessary to store raw traces as long as \(18000 \times 500\). Instead, we recorded only 1600 traces covering all 18000 clock cycles for a pre-detection step to determine which regions of clock cycles we should keep in the later recorded traces (for reference, detection, profiling, validation, and attack). Besides, we had the NI computer controlling the oscilloscope downsample the raw traces to 50 points per clock cycle and stored the downsampled traces in our HDF5 files (the 'traces' dataset in Sample_{PD,RE,DN,TR,VA,TS}_****.hdf5). Meanwhile, for the recordings for pre-detection and detection, we also had the NI computer calculate the samples for detection (the summed value for the 50 raw samples around the peak in each clock cycle, same as previously in the U-Os and U-O3 cases), and stored in the HDF5 files as the 'detects' dataset.</p>

<h3 id=M-Os-predetection>Pre-detection traces</h3>

<p>I/O data pre-generation and downsampled complete traces:</p>

<ul>
<li><a href="M-Os/0000_predetection/inter_gen_PD.zip">inter_gen_PD.zip (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0000.hdf5">Samples/Samples_PD_0000.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0001.hdf5">Samples/Samples_PD_0001.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0002.hdf5">Samples/Samples_PD_0002.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0003.hdf5">Samples/Samples_PD_0003.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0004.hdf5">Samples/Samples_PD_0004.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0005.hdf5">Samples/Samples_PD_0005.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0006.hdf5">Samples/Samples_PD_0006.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0007.hdf5">Samples/Samples_PD_0007.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0008.hdf5">Samples/Samples_PD_0008.hdf5 (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/Samples/Samples_PD_0009.hdf5">Samples/Samples_PD_0009.hdf5 (updated 2024-05-29)</a></li>
</ul>

<p>Then we used the following code to find the mean traces for reference and check the quality of these 1600 traces (no problems detected):</p>

<ul>
<li><a href="M-Os/0000_predetection/preproc_PD.zip">preproc_PD.zip (updated 2024-05-29)</a></li>
</ul>

<p>Note that the target intermediate values in the M-Os experiments are dependent on not only the pre-generated I/O data, but also the counters used in ChaCha to generate masks (key used in ChaCha is fixed and nonces can be calculated in this implementation). Therefore, we can only generated the intermediate values once we finished the recording, where the counters were also recorded in the HDF5 files. We generated both the H/L and E/O grouping intermediate values with the following code:</p>

<ul>
<li><a href="M-Os/0000_predetection/find_intermediates.zip">find_intermediates.zip (updated 2024-05-29)</a></li>
<li><a href="M-Os/0000_predetection/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (updated 2024-05-29)</a></li>
</ul>

<p>Then we used the following code to pre-detect the interesting clock cycles with these 1600 traces to determine the regions we want record:</p>

<ul>
<li><a href="M-Os/0000_predetection/detection_O.zip">detection_O.zip (updated 2024-05-29) for H/L words</a>,</li>
<li><a href="M-Os/0000_predetection/detection_S.zip">detection_S.zip (updated 2024-05-29) for E/O words</a>,</li>
</ul>

<p>and the resulting \(R^2\) values after detection:</p>

<ul>
<li><a href="M-Os/0000_predetection/detection_O/detect_results_08.zip">detection_O/detect_results_08.zip (updated 2024-05-29)</a>,</li>
<li><a href="M-Os/0000_predetection/detection_O/detect_results_32.zip">detection_O/detect_results_32.zip (updated 2024-05-29)</a>,</li>
<li><a href="M-Os/0000_predetection/detection_S/detect_results_08.zip">detection_S/detect_results_08.zip (updated 2024-05-29)</a>,</li>
<li><a href="M-Os/0000_predetection/detection_S/detect_results_32.zip">detection_S/detect_results_32.zip (updated 2024-05-29)</a>.</li>
</ul>

<p>With visual inspection, we selected the following regions of clock cycles in the later recordings, given the 18000 clock cycles in raw traces enumerated from 0 to 17999:</p>

<ul>
<li>[ 3030,  3109],  80 clock cycles,</li>
<li>[ 3350,  3859], 510 clock cycles,</li>
<li>[ 4125,  4264],  50 clock cycles,</li>
<li>[ 6290,  6309],  20 clock cycles,</li>
<li>[ 9780,  9859],  80 clock cycles,</li>
<li>[10840, 10939], 100 clock cycles,</li>
<li>[14540, 14899], 360 clock cycles,</li>
</ul>

<p>and 1200 clock cycles (60000 samples) in total for the concatenated, downsampled traces.</p>

<h3 id=M-Os-reference>Reference traces</h3>


<p>I/O data pre-generation, downsampled traces, and reference trace generation:</p>

<ul>
<li><a href="M-Os/0001_reference/inter_gen_RE.zip">inter_gen_RE.zip (updated 2024-05-22)</a></li>
<li><a href="M-Os/0001_reference/Samples_RE.zip">Samples_RE.zip (updated 2024-05-22)</a>: this ZIP file contains 10 HFD5 files</li>
<li><a href="M-Os/0001_reference/preproc_RE.zip">preproc_RE.zip (updated 2024-05-22)</a></li>
</ul>

<h3 id=M-Os-detection>Detection traces</h3>

<p>I/O data pre-generation, downsampled traces for selected regions, and trace quality checking:</p>

<ul>
<li><a href="M-Os/0002_detection/inter_gen_DN.zip">inter_gen_DN.zip (updated 2024-05-22)</a></li>
<li><a href="M-Os/0002_detection/Samples_DN.zip">Samples_DN.zip (updated 2024-05-22)</a>: this ZIP file contains 100 HFD5 files</li>
<li><a href="M-Os/0002_detection/preproc_DN.zip">preproc_DN.zip (updated 2024-05-22)</a></li>
</ul>

<p>Intermediate value calculation (both H/L and E/O groupings were generated and stored in the same ZIP file):</p>

<ul>
<li><a href="M-Os/0002_detection/find_intermediates.zip">find_intermediates.zip (updated 2024-05-22)</a></li>
<li><a href="M-Os/0002_detection/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (updated 2024-05-22)</a></li>
</ul>

<p>Resulting \(R^2\) values after detection:</p>

<ul>
<li><a href="M-Os/0002_detection/detection_O.zip">detection_O.zip (updated 2024-05-22) for H/L words</a>,</li>
<li><a href="M-Os/0002_detection/detection_O/detect_results_08.zip">detection_O/detect_results_08.zip (updated 2024-05-22)</a>,</li>
<li><a href="M-Os/0002_detection/detection_O/detect_results_32.zip">detection_O/detect_results_32.zip (updated 2024-05-22)</a>,</li>
<li><a href="M-Os/0002_detection/detection_S.zip">detection_S.zip (updated 2024-05-22) for E/O words</a>,</li>
<li><a href="M-Os/0002_detection/detection_S/detect_results_08.zip">detection_S/detect_results_08.zip (updated 2024-05-22)</a>,</li>
<li><a href="M-Os/0002_detection/detection_S/detect_results_32.zip">detection_S/detect_results_32.zip (updated 2024-05-22)</a>.</li>
</ul>

<p>Interesting clock cycles extraction for a given threshold:</p>

<ul>
<li><a href="M-Os/0002_detection/ICS_extract.zip">ICS_extract.zip (updated 2024-05-22)</a>.
</li>
<li><a href="M-Os/0002_detection/ICS_extract/ics_union_004.zip">ICS_extract/ics_union_004.zip (updated 2024-05-22)</a>.
</li>
</ul>

<h3 id=M-Os-training>Profiling (Training) traces</h3>

<p>I/O data pre-generation, downsampled traces for selected regions, and trace quality checking:</p>

<ul>
<li><a href="M-Os/0003_training/inter_gen_TR.zip">inter_gen_TR.zip (updated 2024-05-22)</a></li>
<li><a href="M-Os/0003_training/Samples_TR_part00.zip">Samples_TR_part00.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0003_training/Samples_TR_part01.zip">Samples_TR_part01.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0003_training/Samples_TR_part02.zip">Samples_TR_part02.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0003_training/Samples_TR_part03.zip">Samples_TR_part03.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0003_training/Samples_TR_part04.zip">Samples_TR_part04.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0003_training/Samples_TR_part05.zip">Samples_TR_part05.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0003_training/Samples_TR_part06.zip">Samples_TR_part06.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0003_training/Samples_TR_part07.zip">Samples_TR_part07.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0003_training/preproc_TR.zip">preproc_TR.zip (updated 2024-05-22)</a>
</li>
</ul>

<p>Intermediate value calculation (H/L and E/O bytes in the same file):</p>

<ul>
<li><a href="M-Os/0003_training/find_intermediates.zip">find_intermediates.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0003_training/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (updated 2024-05-23)</a>.</li>
</ul>


<p>Template profiling codes:</p>

<ul>
<li>8-bit templates with H/L bit order: <a href="M-Os/0003_training/template_profiling_MASK_O.zip">template_profiling_MASK_O.zip (updated 2024-05-23)</a>,</li>
<li>8-bit templates with E/O bit order: <a href="M-Os/0003_training/template_profiling_MASK_S.zip">template_profiling_MASK_S.zip (updated 2024-05-23)</a>.</li>
</ul>

<p>Resulting Templates:</p>

<ul>
<li><a href="M-Os/0003_training/template_profiling_MASK_O/templateLDA_O004.zip">template_profiling_MASK_O/templateLDA_O004.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0003_training/template_profiling_MASK_S/templateLDA_O004.zip">template_profiling_MASK_S/templateLDA_O004.zip (updated 2024-05-23)</a>.</li>
</ul>


<h3 id=M-Os-validation>Validation traces</h3>

<p>I/O data pre-generation, downsampled traces for selected regions, and trace quality checking:</p>

<ul>
<li><a href="M-Os/0004_validation/inter_gen_VA.zip">inter_gen_VA.zip (updated 2024-05-23)</a>
</li>
<li><a href="M-Os/0004_validation/Samples_VA.zip">Samples_VA.zip (updated 2024-05-23)</a>
</li>
<li><a href="M-Os/0004_validation/preproc_VA.zip">preproc_VA.zip (updated 2024-05-23)</a>
</li>
</ul>

<p>Intermediate value calculation (both H/L and E/O bytes):</p>

<ul>
<li><a href="M-Os/0004_validation/find_intermediates.zip">find_intermediates.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0004_validation/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (updated 2024-05-23)</a>.</li>
</ul>

<p>Template validation codes:</p>

<ul>
<li><a href="M-Os/0004_validation/template_validation_MASK_O.zip">template_validation_MASK_O.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0004_validation/template_validation_MASK_S.zip">template_validation_MASK_S.zip (updated 2024-05-23)</a>.</li>
</ul>

<p>The resulting "indeces":</p>

<ul>
<li><a href="M-Os/0004_validation/template_validation_MASK_O/Rank_O004.zip">template_validation_MASK_O/Rank_O004.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0004_validation/template_validation_MASK_S/Rank_O004.zip">template_validation_MASK_S/Rank_O004.zip (updated 2024-05-23)</a>.</li>
</ul>

<p>The resulting 1-SR and LGE:</p>

<ul>
<li><a href="M-Os/0004_validation/template_validation_MASK_O/Result_Tables.zip">template_validation_MASK_O/Result_Tables.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0004_validation/template_validation_MASK_S/Result_Tables.zip">template_validation_MASK_S/Result_Tables.zip (updated 2024-05-23)</a>.</li>
</ul>

<h3 id=M-Os-attack>Attack (Testing) traces</h3>

<p>I/O data pre-generation, downsampled traces for selected regions, and trace quality checking:</p>

<ul>
<li><a href="M-Os/0005_attack/inter_gen_TS.zip">inter_gen_TS.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part00.zip">Samples_TS_part00.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part01.zip">Samples_TS_part01.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part02.zip">Samples_TS_part02.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part03.zip">Samples_TS_part03.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part04.zip">Samples_TS_part04.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part05.zip">Samples_TS_part05.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part06.zip">Samples_TS_part06.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part07.zip">Samples_TS_part07.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part08.zip">Samples_TS_part08.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/Samples_TS_part09.zip">Samples_TS_part09.zip (updated 2024-05-23)</a></li>
<li><a href="M-Os/0005_attack/preproc_TS.zip">preproc_TS.zip (updated 2024-05-23)</a></li>
</ul>

<p>I/O data rearrangement:</p>

<ul>
<li><a href="M-Os/0005_attack/data_SASCA.zip">data_SASCA.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0005_attack/data_SASCA/data_key.zip">data_SASCA/data_key.zip (updated 2024-05-23)</a>.</li>
<li><a href="M-Os/0005_attack/data_SASCA/data_nonce.zip">data_SASCA/data_nonce.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0005_attack/data_SASCA/data_plaintext.zip">data_SASCA/data_plaintext.zip (updated 2024-05-23)</a>,</li>
<li><a href="M-Os/0005_attack/data_SASCA/data_ciphertag.zip">data_SASCA/data_ciphertag.zip (updated 2024-05-23)</a>,</li>
</ul>

<p>Full attack procedure with template attack, belief propagation, and key enumeration with both H/L and E/O fragments:</p>

<ul>
<li><a href="M-Os/0005_attack/template_attack_MASK_O.zip">template_attack_MASK_O.zip (updated 2024-05-24)</a>,</li>
<li><a href="M-Os/0005_attack/template_attack_MASK_O_result.zip">template_attack_MASK_O_result.zip (updated 2024-05-24)</a>,</li>
<li><a href="M-Os/0005_attack/template_attack_MASK_S.zip">template_attack_MASK_S.zip (updated 2024-05-24)</a>,</li>
<li><a href="M-Os/0005_attack/template_attack_MASK_S_result.zip">template_attack_MASK_S_result.zip (updated 2024-05-24)</a>.</li>
</ul>

<p>Python code for the probability tables after belief propagation:</p>

<ul>
<li><a href="M-Os/0005_attack/template_attack_MASK_O_tables.zip">template_attack_MASK_O_tables.zip (updated 2024-05-25)</a>,</li>
<li><a href="M-Os/0005_attack/template_attack_MASK_S_tables.zip">template_attack_MASK_S_tables.zip (updated 2024-05-25)</a>,</li>
</ul>

<p>and the tables generated for later key enumeration and rank estimate implemented in Julia:</p>

<ul>
<li><a href="M-Os/0005_attack/template_attack_MASK_O_tables/Tables.zip">template_attack_MASK_O_tables/Tables.zip (updated 2024-05-25)</a>,</li>
<li><a href="M-Os/0005_attack/template_attack_MASK_S_tables/Tables.zip">template_attack_MASK_S_tables/Tables.zip (updated 2024-05-25)</a>,</li>
</ul>

<p>The remaining source code for our Julia implementation of key enumeration and rank estimate will be released here soon ...</p>

-->
