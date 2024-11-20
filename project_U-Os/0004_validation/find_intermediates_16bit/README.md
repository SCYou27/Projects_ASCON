## Tasks in this folder

The main goal here is to find 16-bit, H/L-ordered intermediate values around the tag generation step in ASCON-128. The target values include the key and the fragments in the last two lanes of the output from the final invocation of ASCON permutation in the ASCON-128 encryption. Unlike the cases in the detection and profiling stages, we did not perform a multiple linear regression with the intermediate values recorded in this stage. We just used the values as reference answers for validation. Therefore, we stored the intermediate values as 16-bit integers here instead of binary variables in the cases of the two previous stages.

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) make directories for the results and decompress the data of intermediate bytes from `../find_intermediates/`:  
		`unzip ../find_intermediates/intermediate_values.zip`  
		`mv intermediate_values/ intermediate_values_old/`  
		`mkdir intermediate_values/`  
		`mkdir intermediate_values/intermediate_D_KEY/`  
		`mkdir intermediate_values/intermediate_D_F_B11/`  

	(b) concatenate two consecutive intermediate bytes in H/L groups:  
		`python3 proc.py`  

	(c) pack up the data:  
		`zip -qq intermediate_values.zip -r intermediate_values/`  
		`rm -r intermediate_values/ intermediate_values_old/`  

4. The resulting zip file (`intermediate_values.zip`) will be used in the later template-profiling procedures:  
	`../template_validation_16bits_O/`  

5. Directly download the resulting data from our server:  
	`./download.sh`  

6. Clean all the generated data (to restart):  
	`./clean.sh`  

 
