1. compress.py:
	When the oscilloscope is recording the traces for the reference data set, execute the following script to move and compress the data:

	python3 compress.py 0 10

	We separate the date set into ten subsets, and the compressed files shall be stored as:

	../Raw/Raw_RE_*.zip


2. pre_ref_count.py:
	To calculate the reference trace (ref_trace.npy) by:

	python3 pre_ref_count.py

	We checked that all traces recorded have a Pearson correlation of at least a selected thresold with the reference trace.
	Such threshold has been selected with value equals to 0.99.

 
