## Tasks in this folder

1. check.py: to check the quality of the recorded traces with the reference trace (`ref_trace.npy`) by:  
	`python3 check.py all 0 400`  
   This will also check whether the response is consistent with the pre-calculated values in `../inter_gen/ciphertags.zip`.
   
2. The all-in-one script (including copying the pre-calculated values):  
	`./script_all.sh`  

3. Directly download the generated data from our server:  
	`./download.sh`  

4. Clean the generated data (to restart):  
	`./clean.sh`  


