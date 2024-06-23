Target: The detection procedure given the critical parameters to get the R-square values of each 32-bit intermediate values, which is the summation of the R-square values of its four member bytes.

1. all-in-one script:
	./script_all.sh

2. tasks in the script:
  a) Initialization: decompress the dependent data and make directories for the precessed traces in later steps
	./init.sh

  b) Detection steps:
	python3 detect_script.py

3. to package the resulting files:
	./pack.sh


