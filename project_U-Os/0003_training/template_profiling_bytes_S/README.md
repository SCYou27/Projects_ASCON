## Tasks in this folder

Goal: to build the templates for 8-bit, E/O-ordered intermediate values in each round of the Initialization and Finalization phases in ASCON-128.  

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) initialize the procedure (to load the pre-processed intermediate values and interesting clock cycle sets, and to create folders to store the generated templates):  
		`tag='004'`  
		`./init.sh ${tag}`  
		The variable `tag` denotes the _R_<sup>2</sup> threshold (`>0.004`) to determine interesting clock cycles.

	(b) template profiling:  
		`python3 train_script.py`  

	(c) pack up the data:  
		`./pack.sh ${tag}`  
		This will archive the templates in `templateLDA_O004.zip`, for the later template validation (see `../../0004_validation/`) and attacks (see `../../0005_attack/`)  

3. Directly download the templates from our server:  
	`./download.sh`  

4. Clean all the generated data (to restart):  
	`./clean.sh`  

 
