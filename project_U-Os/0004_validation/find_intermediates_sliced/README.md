## Tasks in this folder

The main goal here is to calculate the intermediate values we need in each round of initialization and finalization for 8-bit E/O template profiling. Unlike the cases in the detection and profiling stages, we did not perform a multiple linear regression with the intermediate values recorded in this stage. We just used the values as reference answers for validation. Therefore, we stored the intermediate values as an 8-bit integer here instead of binary variables in the two previous stages.

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) make directories for the results and decompress the data of intermediate bytes from `../find_intermediates/`:  
		`./init.sh`  

	(b) reorder the intermediate byte from H/L to E/O groups (aka. _interleaving_ or _slicing_):  
		`python3 intermediate_slice.py`  

	(c) check the results:  
		`python3 check_combine.py`

	(d) pack up the data:  
		`./pack.sh`  

4. The resulting zip file (`intermediate_values.zip`) will be used in the later template-profiling procedures:  
	`../template_validation_bytes_S/`  

5. Directly download the resulting data from our server:  
	`./download.sh`  

6. Clean all the generated data (to restart):  
	`./clean.sh`  

 
