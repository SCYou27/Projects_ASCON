## Tasks in this folder

Goal: to calculate the intermediate values we need in each round of initialization and finalization for 8-bit H/L template profiling.  

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) make directories for the results and decompress the IO data (keys, nonces, plaintexts, ciphers, and tags):  
		`mkdir intermediate_HEX/`  
		`mkdir intermediate_HEX/intermediate_trace/`  
		`mkdir intermediate_values/`  
		`unzip ../inter_gen/keys.zip`  
		`unzip ../inter_gen/nonces.zip`  
		`unzip ../inter_gen/plaintexts.zip`  
		`unzip ../inter_gen/ciphertags.zip`  

	(b) calculate the intermediate values, and then cut them into bytes:  
		`python3 intermediate_calculate.py all`  
		`python3 find_hex.py all`  
		`python3 intermediate_H2B.py cal`  
		`python3 intermediate_H2B.py check`  

	(c) compress the results and delete the dependent data:  
		`zip intermediate_HEX.zip -r intermediate_HEX/`  
		`zip intermediate_values.zip -r intermediate_values/`  
		`rm -vr __pycache__/ keys/ nonces/ plaintexts/ ciphertags/ intermediate_HEX/ intermediate_values/`  

3. The resulting zip file (`intermediate_values.zip`) will be used in the later template-profiling procedures:  
	`../template_profiling_bytes_O/`  

4. Directly download the resulting data from our server:  
	`./download.sh`  

5. Clean all the generated data (to restart):  
	`./clean.sh`  

 
