## Tasks in this folder

We downsample the raw traces from 500 to 10 points per clock cycle (PPC) by summing up the values from every 50 consecutive samples to form new traces:

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) Downsample the raw traces and store the downsampled traces in 8 HDF5 files, each contains 8000 traces.  
		`python3 downsampling.py 0 8`  

	(b) Remove the pyc files.  
		`rm -r __pycache__/`  

3. The HDF5 will be used in the later template-profiling procedures:  
	`../template_profiling_bytes_O/`  
	`../template_profiling_bytes_S/`  
	`../template_profiling_16bits_O/`  

4. Directly download the HDF5 files from our server:  
	`./download.sh`  

5. Clean all the generated data (to restart):  
	`./clean.sh`  




