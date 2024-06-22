unzip ../find_intermediates/intermediate_values.zip
mv intermediate_values/ intermediate_values_old/
mkdir intermediate_values/
mkdir intermediate_values/intermediate_D_KEY/
mkdir intermediate_values/intermediate_D_F_B11/
python3 proc.py
zip -qq intermediate_values.zip -r intermediate_values/
rm -r intermediate_values/ intermediate_values_old/
