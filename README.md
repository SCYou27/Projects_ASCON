# Projects ASCON:  
## building templates for recovering ASCON keys

The ASCON dataset contains recordings of the power-supply current changes of the 32-bit processor STM32F303RCT7, which has one ARM Cortex-M4 core, on a ChipWhisperer-Lite (CW-Lite) board.

We used an NI PXIe-5160 10-bit oscilloscope, which can sample at 2.5 GS/s into 2 GB of sampling memory, and an NI PXIe-5423 wave generator, as an external clock signal source, to supply the target board with a 5 MHz square wave signal.

More details of the attack are described in the following paper and theis:

Shih-Chun You, Markus G. Kuhn, Sumanta Sarkar, Feng Hao:   
Low trace-count template attacks on 32-bit implementations of ASCON AEAD,  
IACR Transactions on Cryptographic Hardware and Embedded Systems (TCHES),  
Volume 2023, Issue 4, DOI: https://doi.org/10.46586/tches.v2023.i4.344-366  

Shih-Chun You:  
Single-trace template attacks on permutation-based cryptography,  
Apollo - University of Cambridge Repository,  
PhD thesis, 2022, DOI: https://doi.org/10.17863/CAM.100592  

With the parameters and software version that we stated in our paper, we provide three different implementations of ASCON-128, a variant of ASCON AEAD:

U-Os experiments (project_U-Os): an unmasked implementation with compiler optimization option "-Os".  
U-O3 experiments (project_U-O3): an unmasked implementation with compiler optimization option "-O3".  
M-Os experiments (project_M-Os): a masked implementation with compiler optimization option "-Os".  


