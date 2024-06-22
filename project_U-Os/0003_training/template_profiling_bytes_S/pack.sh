tag=$1
zip templateLDA_O${tag}.zip -r templateLDA_O${tag}/
rm -vr intermediate_values/ templateLDA_O${tag}/ ics_union_${tag}/ __pycache__/
