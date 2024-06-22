Target: to calculate the intermediate values we need in each round of initialization and finalization for the ICs detection.

1. all in one script:
	./readme.sh

2. tasks in 'readme.sh':

  a) make directories for the results, decompressed the IO data (keys, nonces, plaintexts, ciphers and tags):
	mkdir intermediate_HEX/
	mkdir intermediate_HEX/intermediate_trace/
	mkdir intermediate_values/
	unzip ../inter_gen/keys.zip
	unzip ../inter_gen/nonces.zip
	unzip ../inter_gen/plaintexts.zip
	unzip ../inter_gen/ciphertags.zip

  b) calculate the intermediate values, and cutting them into bytes:
	python3 intermediate_calculate.py all
	python3 find_hex.py all
	python3 intermediate_H2B.py cal
	python3 intermediate_H2B.py check

  c) compress the results and delete the the dependent data:
	zip intermediate_HEX.zip -r intermediate_HEX/
	zip intermediate_values.zip -r intermediate_values/
	rm -vr __pycache__/ keys/ nonces/ plaintexts/ ciphertags/ intermediate_HEX/ intermediate_values/

3. The resulting zip file (intermediate_values.zip) will be used in the later detection procedures:
	a) detection/
	b) normal_detect_all/
	c) small_detect_all/


