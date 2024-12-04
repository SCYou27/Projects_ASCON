## Tasks in this folder

We applied multiple linear regression on the processed samples against the values of the intermediate binary variables to calculate the coefficient of determination (_R_<sup>2</sup>) between each sample and each target intermediate byte (E/O ordered). The results will be stored in `detection_S/detect_results_08.zip`, and this will also calculate the summed _R_<sup>2</sup> of those from the four member bytes to represent the value for a target 32-bit intermediate word, stored in `detection_S/detect_results_32.zip`.    

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) copy the E/O intermediate bytes from `../find_intermediates_sliced/`, and generate folders `detect_results_08` and`detect_results_32`:  
		`./init.sh`  

	(b) apply multiple linear regression:  
		`python3 detect_script.py`

	(c) pack up the results:  
		`./pack.sh`  

4. The coefficients will be used in `ICS_extract` to determine the interesting clock cycles.  

5. Directly download the resulting data from our server:  
	`./download.sh`  

6. Clean all the generated data (to restart):  
	`./clean.sh`  

 
