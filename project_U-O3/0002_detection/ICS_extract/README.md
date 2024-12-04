## Tasks in this folder

Here we select the interesting clock cycles given that we already have the R-square values of each clock cycle within the window of the recording.

1. all-in-one script:  
	`./script_all.sh`
   This includes three sub-scripts as follows:
   	`./ics_original.sh`  
	`./ics_sliced.sh`  
	`./ics_union.sh`  

2. tasks in script `ics_original.sh`:  
	`unzip ../detection_O/detect_results_32.zip` # _The dependent data: R-square values_  
	`python3 ics_original.py 0.040` # _Extract the interesting clock cycles with R-square values against 32-bit H/L words higher than 0.040_  
	`python3 ics_original.py 0.035`  
	`python3 ics_original.py 0.030`  
	`python3 ics_original.py 0.025`  
	`python3 ics_original.py 0.020`  
	`python3 ics_original.py 0.015`  
	`python3 ics_original.py 0.010`  
	`python3 ics_original.py 0.005`  
	`python3 ics_original.py 0.004`  
	`python3 ics_original.py 0.003`  
	`python3 ics_original.py 0.002`  
	`python3 ics_original.py 0.001`  
	`rm -vr detect_results_32/`  

3. tasks in script `ics_sliced.sh`:  
        `unzip ../detection_S/detect_results_32.zip` # _The dependent data: R-square values_  
        `python3 ics_sliced.py 0.040` # _Extract the interesting clock cycles with R-square values against 32-bit E/O words higher than 0.040_  
        `python3 ics_sliced.py 0.035`  
        `python3 ics_sliced.py 0.030`  
        `python3 ics_sliced.py 0.025`  
        `python3 ics_sliced.py 0.020`  
        `python3 ics_sliced.py 0.015`  
        `python3 ics_sliced.py 0.010`  
        `python3 ics_sliced.py 0.005`  
        `python3 ics_sliced.py 0.004`  
        `python3 ics_sliced.py 0.003`  
        `python3 ics_sliced.py 0.002`  
        `python3 ics_sliced.py 0.001`  
        `rm -vr detect_results_32/`  

4. tasks in script `ics_union.sh`, which are to find the union set of the interesting clock cycle from H/L and E/L words for each lane:  
	`python3 ics_union.py 0.040`  
	`python3 ics_union.py 0.035`  
	`python3 ics_union.py 0.030`  
	`python3 ics_union.py 0.025`  
	`python3 ics_union.py 0.020`  
	`python3 ics_union.py 0.015`  
	`python3 ics_union.py 0.010`  
	`python3 ics_union.py 0.005`  
	`python3 ics_union.py 0.004`  
	`python3 ics_union.py 0.003`  
	`python3 ics_union.py 0.002`  
	`python3 ics_union.py 0.001`  

5. The (union) interesting clock cycles will be used in the later profiling, validation, and attack stages.  

6. Directly download the resulting data from our server:  
	`./download.sh`  

7. Clean all the generated data (to restart):  
	`./clean.sh`  



