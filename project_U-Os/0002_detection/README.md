## Detection traces
<p>We recorded 16000 traces for interesting clock cycle detection.</p>

<p>Similarly, we provide the Python code that generated all the data for the recording in the following ZIP file:</p>

<ul>
<li><a href="U-Os/0002_detection/inter_gen_DN.zip">inter_gen_DN.zip (updated 2024-05-01)</a>
</li>
</ul>

<p>With the pre-generated I/O data, we then calculated all the target intermediate values and cut them into bytes with the following code:</p>

<ul>
<li><a href="U-Os/0002_detection/find_intermediates.zip">find_intermediates.zip (updated 2024-05-02)</a>,<br>
resulting in <a href="U-Os/0002_detection/find_intermediates/intermediate_values.zip">find_intermediates/intermediate_values.zip (H/L version, updated 2024-05-02)</a>
</li>
</ul>

<p>As we mentioned in our paper, the bit-interleaving (slicing) technique is applied in our target implementations. Therefore, we also calculated the bit-interleaved intermediate values:</p>

<ul>
<li><a href="U-Os/0002_detection/find_intermediates_sliced.zip">find_intermediates_sliced.zip (updated 2024-05-02)</a>,<br>
resulting in <a href="U-Os/0002_detection/find_intermediates_sliced/intermediate_values.zip">find_intermediates_sliced/intermediate_values.zip (E/O version, updated 2024-05-02)</a>
</li>
</ul>


<p>The raw traces were recorded and stored in 100 ZIP files in the following directory:</p>

<ul>
<li><a href="U-Os/index.html#DN">Raw traces for the detection set</a>
</li>
</ul>

<p>We used the code in the following ZIP file to check the quality of the recorded traces by comparing them with the reference trace (ref_trace.npy):</p>

<ul>
<li><a href="U-Os/0002_detection/preproc_DN.zip">preproc_DN.zip (updated 2024-05-01)</a>
</li>
</ul>

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
