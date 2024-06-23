lower=0
upper=1000
./init.sh
python3 best_estimate.py ${lower} ${upper}
python3 plot_data.py ${lower} ${upper}
python3 plot_data.py ${lower} ${upper} > report.txt
./pack.sh
