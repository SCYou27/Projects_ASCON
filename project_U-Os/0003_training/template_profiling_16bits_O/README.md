## Tasks in this folder

Goal: to build the templates for 16-bit, H/L-ordered intermediate values around the tag generation step in ASCON-128. The target values include the key, and the fragments in the last two lanes of the output from the final invocation of ASCON permutation in the ASCON-128 encreyption.

1. The all-in-one script:  
	`./script_all.sh`  

2. Tasks in `script_all.sh`:  
	(a) initialize the procedure (to load the pre-processed intermediate values and interesting clock cycle sets, and to create folders to store the generated templates):  
		`tag='004'`  
		`detail='16bit'`  
		`unzip ../find_intermediates_${detail}/intermediate_values.zip`  
		`unzip ../../0002_detection/ICS_extract/ics_union_${tag}.zip`  
		`mkdir templateLDA_O${tag}_${detail}/`  
		`mkdir templateLDA_O${tag}_${detail}/template_KEY/`  
		`mkdir templateLDA_O${tag}_${detail}/template_F_B11/`  
		The variable `tag` denotes the _R_<sup>2</sup> threshold (`>0.004`) to determine interesting clock cycles.

	(b) template profiling:  
		`python3 train_script.py`  

	(c) pack up the data:  
		`zip templateLDA_O${tag}_${detail}.zip -r templateLDA_O${tag}_${detail}/`  
		`rm -vr intermediate_values/ templateLDA_O${tag}_${detail}/ ics_union_${tag}/ __pycache__/`  
		This will archive the templates in `templateLDA_O004.zip`, for the later template validation (see `../../0004_validation/`) and attacks (see `../../0005_attack/`)  

3. Directly download the templates from our server:  
	`./download.sh`  

4. Clean all the generated data (to restart):  
	`./clean.sh`  

 
