## Tasks in this folder

1. Generate the reference trace (`ref_trace.npy`) by averaging the 1600 recorded traces:  
	`python3 pre_ref_count.py`  

2. We checked that all traces recorded have a Pearson correlation of at least higher than the selected threshold (0.99) against the reference trace.  
	`python3 pre_get_corr.py all 4`  
 
3. The all-in-one script:  
    `./script_all.sh`  

4. Directly download the reference trace from our server:  
	`./download.sh`  

5. Clean all the generated data:  
	`./clean.sh`  


