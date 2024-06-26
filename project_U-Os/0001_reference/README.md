# Reference traces

We recorded 1600 traces and took their arithmetic mean vector as a reference trace, so the later recorded traces can be compared against this reference trace to check whether some unexpected event happened and resulted in a wrong recording. This will be divided into the following small tasks:  

1. inter_gen/  
   This is to pre-generate the data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording.

***Work on this README file is still ongoing!***
<!--
<p>We first provide the Python code that generated all the input data (keys, nonces, plaintexts) for the recording and pre-calculated the corresponding output data (ciphertexts and tags) in the following ZIP file:</p>

<ul>
<li><a href="U-Os/0001_reference/inter_gen_RE.zip">inter_gen_RE.zip (updated 2024-04-15)</a>
</li>
</ul>
-->

<!--
<p>The raw traces were recorded and stored in 10 ZIP files via the following link:</p>

<ul>
<li><a href="U-Os/index.html#RE">Raw traces for the reference set</a>
</li>
</ul>

<p>We used the code in the following ZIP file to generate the reference trace (<a href="U-Os/0001_reference/ref_trace.npy">ref_trace.npy (updated 2024-05-01)</a>):</p>

<ul>
<li><a href="U-Os/0001_reference/preproc_RE.zip">preproc_RE.zip (updated 2024-05-01)</a>
</li>
</ul>



2. preproc/
  a. to copy and compress the recorded traces from the oscilloscope
  b. to find the refrence trace (ref_trace.npy)
  c. some statistic data

3. Raw/
  all the compressed data (zip files) are stored here

Please find the readme.txt files in the sub-directories to check more details.
-->
