1. compress.py:
	When the oscilloscope is recording the traces for the reference data set, execute the following script to move and compress the data:

	python3 compress.py 0 100

	We separate the date set into ten subsets, and the compressed files shall be stored as:

	../Raw/Raw_DN_*.zip


2. check.py:
	To check the quality of the recorded traces with the reference trace (ref_trace.npy) by:

	python3 check.py all 0 100

