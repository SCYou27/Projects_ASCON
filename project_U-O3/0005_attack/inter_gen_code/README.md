1. initialization (make directories)
   ./init.sh

2. generate data for the 100 data sets, with the same key being used 10 times.
   python3 inter_gen.py

3. package the data
   ./pack.sh

4. if we want to restart:
   ./clean.sh 
