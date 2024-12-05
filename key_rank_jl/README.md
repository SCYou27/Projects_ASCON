# A fast Julia implementation of the key-enumeration and rank-estimation steps

We provide a Julia implementation of the key-enumeration and rank-estimation steps to estimate the average rank for the correct key (logarithmic guessing entropy, LGE), given probability tables for the candidates of key fragments and the knowledge of the correct key.

This contains 12 experiements with diffferent scenarios as follows.

**U-Os experiments:**  
   - Case 1 _the key (direct) attack_: Tables for 8-bit key fragments with probabilities estimated by only key templates  
   - Case 2 _the byte attack_: Tables for 8-bit key fragments with probabilities estimated after belief propagation on information from templates for the key and intermediate values involved in the tag generation step  
   - Case 3 _the 16-bit attack_: Tables for 16-bit key fragments with probabilities estimated after belief propagation on information from templates for the key and intermediate values involved in the tag generation step  
   - Case 4 _the loopy (bit) attack_: Tables for 1-bit key fragments with probabilities estimated after loopy belief propagation on marginalized information from 8-bit templates for all targeted intermediate values in the AEAD procedure

**U-O3 experiments:**
   - Case 5 _the key (direct) attack_: Tables for 8-bit key fragments with probabilities estimated by only key templates
   - Case 6 _the byte attack_: Tables for 8-bit key fragments with probabilities estimated after belief propagation on information from templates for the key and intermediate values involved in the tag generation step
   - Case 7 _the 16-bit attack_: Tables for 16-bit key fragments with probabilities estimated after belief propagation on information from templates for the key and intermediate values involved in the tag generation step
   - Case 8 _the loopy (bit) attack_: Tables for 1-bit key fragments with probabilities estimated after loopy belief propagation on marginalized information from 8-bit templates for all targeted intermediate values in a the AEAD procedure

**M-Os experiments:**
   - Case  9 _the key (direct) O attack_: Tables for 8-bit H/L key fragments with probabilities estimated by only key templates
   - Case 10 _the byte O attack_: Tables for 8-bit H/L key fragments with probabilities estimated after belief propagation on information from templates for the key and intermediate values involved in the tag generation step
   - Case 11 _the key (direct) S attack_: Tables for 8-bit E/O key fragments with probabilities estimated by only key templates
   - Case 12 _the byte S attack_: Tables for 8-bit E/O key fragments with probabilities estimated after belief propagation on information from templates for the key and intermediate values involved in the tag generation step


The Makefile contains the following steps:

1. make all: to execute `load`, `execute`, `plot`, and `remove`.

2. make load: to load the probability tables and fragments for the correct keys to this subdirectory.

3. make instantiate: ???

4. make plot: to print out the logarithmic guessing entropy in file `report.txt` for plotting tables in LaTeX.

5. make clean: to delete the results (`report.txt` and all NPY file).

6. make remove: to delete the prerequisite probabiltiy tables and fragments for the correct keys.

We also provide a shell script `download.sh` that can download the results from our web site.


