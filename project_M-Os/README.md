# Experiments on M-Os data set  

When we recorded our traces for experiments, we split the traces into six different groups: _Pre-detection, Reference, Detection, Profiling (Training), Validation, and Attack (Testing)_. The code processing each of these groups can be found in

 -  **0000\_predetection:** to determine the window for our recording.
 -  **0001\_reference:** to find a reference trace for recording quality checking.
 -  **0002\_detection:** to determine points of interest (PoI).
 -  **0003\_training:** to build our templates.
 -  **0004\_validation:** to validate our templates.
 -  **0005\_attack:** to recover keys used in ASCON AEAD with our attack scenario.

Please check the REAMDE.md in each subdirectory for detailed instructions.

The Python scripts for controlling the recording hardware and target hardware can be found seperately at

https://www.cl.cam.ac.uk/research/security/datasets/ascon/src_recording/CW_ASCON_masked_20240528.zip

Please check our [web site](https://www.cl.cam.ac.uk/research/security/datasets/ascon/index.html#M-Os-recording) for details on the configuration of the recording platform.


<!--

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
