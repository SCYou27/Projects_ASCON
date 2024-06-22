Target: to select the interesting clock cycles given we already have the R-square values of each clock cycle within the window of the recording.

1. all-in-one script:
	./script_all.sh

2. tasks in script "ics_original.sh":
	unzip ../detection_O/detect_results_32.zip # The dependent data: R-square values
	python3 ics_original.py 0.040
	python3 ics_original.py 0.035
	python3 ics_original.py 0.030
	python3 ics_original.py 0.025
	python3 ics_original.py 0.020
	python3 ics_original.py 0.015
	python3 ics_original.py 0.010
	python3 ics_original.py 0.005
	python3 ics_original.py 0.004
	python3 ics_original.py 0.003
	python3 ics_original.py 0.002
	python3 ics_original.py 0.001
	rm -vr detect_results_32/ 

3. tasks in script "ics_sliced.sh":
        unzip ../detection_S/detect_results_32.zip # The dependent data: R-square values
        python3 ics_sliced.py 0.040
        python3 ics_sliced.py 0.035
        python3 ics_sliced.py 0.030
        python3 ics_sliced.py 0.025
        python3 ics_sliced.py 0.020
        python3 ics_sliced.py 0.015
        python3 ics_sliced.py 0.010
        python3 ics_sliced.py 0.005
        python3 ics_sliced.py 0.004
        python3 ics_sliced.py 0.003
        python3 ics_sliced.py 0.002
        python3 ics_sliced.py 0.001
        rm -vr detect_results_32/

4. tasks in script "ics_union.sh": to combine the interesting clock cycle sets for lanes
	python3 ics_union.py 0.040
	python3 ics_union.py 0.035
	python3 ics_union.py 0.030
	python3 ics_union.py 0.025
	python3 ics_union.py 0.020
	python3 ics_union.py 0.015
	python3 ics_union.py 0.010
	python3 ics_union.py 0.005
	python3 ics_union.py 0.004
	python3 ics_union.py 0.003
	python3 ics_union.py 0.002
	python3 ics_union.py 0.001

Given a threshold, we can find the interesting clock cycles of each 32-bit intermediate values.
e.g. python3 ics_original.py 0.015 => the resulting file: ics_original_015.zip

