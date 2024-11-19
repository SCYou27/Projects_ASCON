## Tasks in this folder

Goal: to build the templates for 8-bit, H/L-ordered intermediate values in each round of the Initialization and Finalization phases in ASCON-128.  

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) initialize the procedure:  
		`tag='004'`  
		`./init.sh ${tag}`  
		The variable `tag` denotes the _R_<sup>2</sup> threshold to determine interesting clock cycles.

	(b) template profiling:  
		`python3 train_script.py`  

	(c) pack up the data:  
		`./pack.sh ${tag}`  

4. Tasks in `init.sh`:  
	(a)

3. The resulting zip file (`intermediate_values.zip`) will be used in the later template-profiling procedures:  
	`../template_profiling_bytes_O/`  

4. Directly download the resulting data from our server:  
	`./download.sh`  

5. Clean all the generated data (to restart):  
	`./clean.sh`  

 
