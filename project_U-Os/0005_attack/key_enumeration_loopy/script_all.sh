lower=0
upper=1000
./init.sh
for i in $(seq -f "%02g" 1 10)
  do
    python3 table_enumerate.py L$i ${lower} ${upper}
    python3 plot_data.py L$i ${lower} ${upper}
    python3 plot_data.py L$i ${lower} ${upper} >> report.txt
  done
./pack.sh
