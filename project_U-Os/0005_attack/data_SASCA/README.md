## Tasks in this folder

In this attack stage, we do not need the intermediate values but only the pre-generated I/O data to feed into the belief propagation procedure as the known data (the plaintexts, nonces, ciphertexts, and tags), or as the reference (the pre-generated key strings) to verify the correctness of our recovered keys. However, for the convenience of our attack, we rearrange these data in this folder.

Here we stored the 1000 key strings in 1000 separated NPY files in `data_key.zip`. For the other I/O data, we stored them in `data_nonce.zip`, `data_plaintext.zip`, and `data_ciphertag.zip`, where each NPY file contains a 10-element array that stores the same type of data from the 10 encryptions sharing the same key with the corresponding index.

1. The all-in-one script:  
	`./script_all.sh`  

2. Directly download the resulting data from our server:  
	`./download.sh`  

3. Clean all the generated data (to restart):  
	`./clean.sh`  

 
