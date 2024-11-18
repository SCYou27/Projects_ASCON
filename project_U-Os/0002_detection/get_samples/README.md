## Tasks in this folder

The main target here is to find the samples for detection. We used one sample per clock cycle to determine whether a clock cycle is interesting. We calculated the summation of 50 points around the peak of a clock cycle as such a sample for detection.  

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) with the downloaded raw traces in `../Raw/`, we find the target samples by:  
		`python3 get_samples.py 0 100`  

	(b) remove the `pyc` files:  
		`rm -r __pycache__/`  

3. The samples will be used in the later detection procedures in `../detection_O/` and `../detection_S/`.  

4. Directly download the resulting data from our server:  
	`./download.sh`  

5. Clean all the generated data (to restart):  
	`./clean.sh`  

 
