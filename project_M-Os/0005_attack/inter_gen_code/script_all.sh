./init.sh
python3 inter_gen.py
python3 key_check.py 0 1000 > report.txt
./pack.sh
