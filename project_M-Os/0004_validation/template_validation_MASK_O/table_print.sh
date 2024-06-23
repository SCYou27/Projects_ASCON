TAG='O004'
unzip Rank_${TAG}.zip
mkdir Result_Tables/
python3 draw_all.py 4
zip Result_Tables.zip -r Result_Tables/
rm -vr Rank_*/ Result_Tables/
