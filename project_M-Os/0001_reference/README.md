# Reference traces  

***This README file is still being revised...***  
<!--
We recorded 1600 traces and took their arithmetic mean vector as a reference trace, so the later recorded traces can be compared against this reference trace to check whether some unexpected event happened and resulted in a wrong recording. This will be divided into the following small tasks:  

1. **Generate I/O data:**  
   The folder `inter_gen/` contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. We moved the Python code into another folder `inter_gen_code/` to prevent overwriting the data we had used.  

2. **Download the raw traces:**  
   The 1600 raw traces are stored in 10 ZIP files. Please download the raw traces with the following commands:  
   `cd Raw/`  
   `./script_all.sh`  
   Alternatively, please visit our university webpage to download the files manually:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#RE  

3. **Process the raw traces and find the reference trace:**  
   `cd preproc/`  
   `./script_all.sh`  
   This will generate the reference trace `preproc/ref_trace.npy` for trace quality validation in the later phases.  




<h2 id=M-Os>M-Os experiments</h2>

<h3 id=M-Os-reference>Reference traces</h3>


<p>I/O data pre-generation, downsampled traces, and reference trace generation:</p>

<ul>
<li><a href="M-Os/0001_reference/inter_gen_RE.zip">inter_gen_RE.zip (updated 2024-05-22)</a></li>
<li><a href="M-Os/0001_reference/Samples_RE.zip">Samples_RE.zip (updated 2024-05-22)</a>: this ZIP file contains 10 HFD5 files</li>
<li><a href="M-Os/0001_reference/preproc_RE.zip">preproc_RE.zip (updated 2024-05-22)</a></li>
</ul>

-->
