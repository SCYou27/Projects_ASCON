## Tasks in this folder

Goal: to calculate the intermediate values we need in each round of initialization and finalization for 16-bit H/L template profiling.  

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) make directories for the results and decompress the data of intermediate bytes from `../find_intermediates/`:  
		`unzip ../find_intermediates/intermediate_values.zip`  
		`mv intermediate_values/ intermediate_values_bytes/`  
		`mkdir intermediate_values/`  

	(b) concatenate two consecutive intermediate bytes in H/L groups:  
		`python3 intermediate_combine.py`  

	(c) pack up the data:  
		`zip intermediate_values.zip -r intermediate_values/`  
		`rm -vr intermediate_values/ intermediate_values_bytes/`  

4. The resulting zip file (`intermediate_values.zip`) will be used in the later template-profiling procedures:  
	`../template_profiling_16bits_O/`  

5. Directly download the resulting data from our server:  
	`./download.sh`  

6. Clean all the generated data (to restart):  
	`./clean.sh`  

 
