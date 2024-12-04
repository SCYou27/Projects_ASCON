# A template attack to recover ASCON AEAD keys

This repository contains the Python and Julia code used to conduct the
side-channel attacks described in

 -  Shih-Chun You, Markus G. Kuhn, Sumanta Sarkar, Feng Hao:   
    _Low trace-count template attacks on 32-bit implementations of ASCON AEAD_,  
    IACR Transactions on Cryptographic Hardware and Embedded Systems (TCHES),  
    Volume 2023, Issue 4, DOI: https://doi.org/10.46586/tches.v2023.i4.344-366  

 -  Shih-Chun You: _Single-trace template attacks on permutation-based cryptography_,  
    PhD thesis, University of Cambridge, 2022,
    DOI: https://doi.org/10.17863/CAM.100592  

These attacks reconstruct the cryptographic key used by ASCON AEAD implementations.

This software can be used together with the powertraces available at
https://www.cl.cam.ac.uk/research/security/datasets/ascon/ where you
will also find the firmware running on the STM32F303RCT7 CPU targeted
by these experiments.

That [ASCON dataset](https://www.cl.cam.ac.uk/research/security/datasets/ascon/) contains recordings of the power-supply current changes of the 32-bit processor STM32F303RCT7, which has one ARM Cortex-M4 core, on a ChipWhisperer-Lite (CW-Lite) board.

We recorded our trace data using an NI PXIe-5160 10-bit oscilloscope, sampling at 2.5 GS/s into 2 GB of sampling memory, and a synchronized NI PXIe-5423 wave generator to supply the target board with a 5 MHz square-wave external clock signal. Therefore, this code assumes a sampling rate of 500 samples per clock cycle of the target CPU.

## Projects

We separated our Python code into three sub-projects by the [ASCON AEAD implementations](https://www.cl.cam.ac.uk/research/security/datasets/ascon/src_recording/ascon_src_website.zip) and experiment that they target:

 -  **U-Os experiments:** in [`project_U-Os/`](project_U-Os/) (unmasked implementation, optimized for space)
 -  **U-O3 experiments:** in [`project_U-O3/`](project_U-O3/) (unmasked implementation, optimized for speed)
 -  **M-Os experiments:** in [`project_M-Os/`](project_M-Os/) (masked implementation)

A fast Julia implementation of the key-enumeration and rank-estimation steps used in all three experiments is in [`key_rank_jl/`](key_rank_jl/)

For each sub-task in our experiments, we provide three shell scripts:

 -  `script_all.sh`: an all-in-one script to finish all tasks in that subdirectory
 -  `download.sh`: directly download the results from [our web site](https://www.cl.cam.ac.uk/research/security/datasets/ascon/)
 -  `clean.sh`: delete all the results and intermediate files
