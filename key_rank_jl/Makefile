JULIA=julia
THREADS=25

all: load execute plot remove

load:
	sh init_U.sh Os
	sh init_U.sh O3
	sh init_M.sh Os

execute:
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 1   # U-Os direct
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 2   # U-Os bytes
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 3   # U-Os 16bits
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 4   # U-Os bits      1h47 (i7-3770, 3.4 GHz)
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 5   # U-O3 direct
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 6   # U-O3 bytes     2h20
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 7   # U-O3 16bits    2h51
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 8   # U-O3 bits
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 9   # M-Os direct_O
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 10  # M-Os bytes_O
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 11  # M-Os direct_S
	date
	time $(JULIA) --project --threads=$(THREADS) rank.jl 12  # M-Os bytes_S   6h51
	date

instantiate:
	$(JULIA) --project -e "using Pkg; Pkg.instantiate()"

plot:
	python3 make_tables_U.py U-Os-Tables_direct-result   >> report.txt
	python3 make_tables_U.py U-Os-Tables_bytes-result    >> report.txt
	python3 make_tables_U.py U-Os-Tables_16bits-result   >> report.txt
	python3 make_tables_U.py U-Os-Tables_bits-result     >> report.txt
	python3 make_tables_U.py U-O3-Tables_direct-result   >> report.txt
	python3 make_tables_U.py U-O3-Tables_bytes-result    >> report.txt
	python3 make_tables_U.py U-O3-Tables_16bits-result   >> report.txt
	python3 make_tables_U.py U-O3-Tables_bits-result     >> report.txt
	python3 make_tables_M.py M-Os-Tables_direct_O-result >> report.txt
	python3 make_tables_M.py M-Os-Tables_bytes_O-result  >> report.txt
	python3 make_tables_M.py M-Os-Tables_direct_S-result >> report.txt
	python3 make_tables_M.py M-Os-Tables_bytes_S-result  >> report.txt

clean:
	rm -rf *.npy report.txt

remove:
	rm -rf U-Os/ U-O3/ M-Os/

