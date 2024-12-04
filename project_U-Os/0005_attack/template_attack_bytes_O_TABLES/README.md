## Tasks in this folder

We generate the probabilty tables for the key fragments after the believe propagation. It can be separated into the following steps:

1. Use the templates for 8-bit, H/L-ordered fragments to estimate the probability tables for the key and fragments for the last two lanes output by the ASCON permutation in the Finalization phase.

2. Apply the believe propagation with a factor graph covering the XOR operation on the key and these two lanes, with the known tag values as the output.

3. After the above two steps, we collect the new probability tables for the key fragment, with the information updated by the believe propagation.


<!--
1. the all-in-one script:  
	`./script_all.sh`  
	This will generate the ZIP files: `Rank_O004.zip` contains the rank data of the correct candidate for the target fragment in each validation trial, while `Result_Tables.zip` contains the SR and GE values we calculated based on the rank data.  

2. print the result tables:  
	`./table_print.sh`  

3. Directly download the resulting data from our server:  
	`./download.sh`  

4. Clean all the generated data (to restart):  
	`./clean.sh`  
-->

