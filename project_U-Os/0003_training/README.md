# Profiling (Training) traces  
We recorded 64000 traces (stored in 400 ZIP files) for template profiling.  

1. **Generate I/O data:**  
   The folder `inter_gen/` contains the pre-generated I/O data interacting with the device (including the keys, nonces, plaintexts, and the corresponding ciphers and tags) for trace recording. We moved the Python code into another folder `inter_gen_code/` to prevent overwriting the data we had used.  

2. **Download the raw traces:**  
   The 64000 raw traces are stored in 400 ZIP files. Please download the raw traces with the following commands:
   
   `cd Raw/`  
   `./script_all.sh`
   
   Alternatively, please visit our university webpage to manually download the files:  
   https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/index.html#TR  

3. **Check the raw traces and their corresponding AEAD outputs (ciphers and tags):**
   
   `cd preproc/`  
   `./script_all.sh`
   
   This will check the quality of the recorded traces against the reference trace (`0001_reference/preproc/ref_trace.npy`) as well as whether the recorded responses from the CW-Lite board are equal to our pre-calculated ciphers and tags.

4. **Calculate our target intermediate values:**  
   With the pre-generated I/O data, we calculated all the target intermediate values. As we mentioned in our paper, the bit-interleaving (slicing) technique is applied in our target implementations. This means that a 64-bit lane of our binary target intermediate values will be stored in two 32-bit registers, divided into either high/low (H/L) bits or even/odd (E/O) bits.

   We first calculated the target intermediate values in 32-bit H/L words:
   
   `cd find_intermediates/`  
   `./script_all.sh`  
   
   Here each 32-bit value will be cut into four bytes, and then further converted to eight binary variables representing each byte, as we will later apply a multiple linear regression on our samples against these binary variables. 

   Then we also converted the binary H/L data into the E/O data:
   
   `cd find_intermediates_sliced/`  
   `./script_all.sh`  

   In addition, we also calculated the target 16-bit intermediate values for profiling the 16-bit templates (H/L):  

  `cd find_intermediates_16bit/`  
  `./script_all.sh`  

5. **Downsample the raw traces**  
  

***This file is not yet finished!***

<!--
<h3 id=U-Os-training>Profiling (Training) traces</h3>


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

-->

