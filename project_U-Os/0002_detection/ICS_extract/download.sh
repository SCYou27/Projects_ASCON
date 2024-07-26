DIR='https://www.cl.cam.ac.uk/research/security/datasets/ascon/U-Os/0002_detection/ICS_extract/'
for tag in '001' '002' '003' '004' '005' '010' '015' '020' '025' '030' '035' '040'
  do
    for set_tag in 'original' 'sliced' 'union'
      do
        wget ${DIR}ics_${set_tag}_${tag}.zip
      done
  done
