## Tasks in this folder

We validated our templates for 8-bit, H/L-ordered fragments. We used two metrics, the first-order success rate (SR) and the guessing entropy (GE), to evaluate the quality of our templates. 

After the downsampling procedure in `../Resample_HDF5/`, we divided the 4000 traces into four groups with equal size: G0 for the first 1000 traces, G1 for the second ones, G2 for the third ones, and G3 for the last ones. The validation results (SR and GE) from G0 were reported and published in our paper, whereas the others were for comparison.

1. the all-in-one script:
	`./script_all.sh`  
	This will generate the ZIP files: `Rank_O004.zip` contains the rank data of the correct candidate for the target fragment in each validation trials, while `Result_Tables.zip` contains the SR and GE values we calculated based on the rank data.  

2. print the result tables:
	`./table_print.sh`  

3. Directly download the resulting data from our server:  
	`./download.sh`  

4. Clean all the generated data (to restart):  
	`./clean.sh`  

