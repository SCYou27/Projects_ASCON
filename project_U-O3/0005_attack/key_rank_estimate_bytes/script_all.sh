lower=0
upper=1000
./init.sh
for i in $(seq -f "%02g" 1 10)
  do
    python3 best_estimate.py L$i ${lower} ${upper}
  done
python3 plot_data.py
python3 plot_data.py >> report.txt
./pack.sh
