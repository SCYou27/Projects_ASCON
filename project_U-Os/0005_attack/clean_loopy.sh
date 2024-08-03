for i in $(seq -f "%02g" 1 10)
do
cd template_attack_loopy_D99_TABLES_L${i}/
sh clean.sh
cd ../
done
