tag='004'
./init.sh ${tag}
python3 train_script.py
./pack.sh ${tag}
