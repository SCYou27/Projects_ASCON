1. initialization (make directories)
   ./init.sh

2. generate data for the 1000 data sets, where the same key being used 100 times.
   python3 inter_gen.py

3. package the data
   ./pack.sh

4. if we want to restart:
   ./clean.sh 
