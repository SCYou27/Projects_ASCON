## Tasks in this folder

1. initialize (make directories):  
	`./init.sh`

2. generate data for the 100 data sets, containing I/O data for 10000 encryptions:  
	`python3 inter_gen.py`  
	Note that in these 10000 encryptions for recording, we had each 10 share the same key for extending our single-trace attack to a multi-trace attack.   

3. check the data:  
	`python3 key_check.py 0 100 > report.txt`  

4. pack up the data:  
	`./pack.sh`  

5. all-in-one script:  
	`./script_all.sh`  
   
6. clean the generated data to restart:  
	`./clean.sh`  
