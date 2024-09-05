# A template attack to recover keys in ASCON AEAD

The ASCON dataset contains recordings of the power-supply current changes of the 32-bit processor STM32F303RCT7, which has one ARM Cortex-M4 core, on a ChipWhisperer-Lite (CW-Lite) board.

We used an NI PXIe-5160 10-bit oscilloscope, which can sample at 2.5 GS/s into 2 GB of sampling memory, and an NI PXIe-5423 wave generator, as an external clock signal source, to supply the target board with a 5 MHz square wave signal.

More details of the attack are described in the following paper and thesis:

 -  Shih-Chun You, Markus G. Kuhn, Sumanta Sarkar, Feng Hao:   
    _Low trace-count template attacks on 32-bit implementations of ASCON AEAD_,  
    IACR Transactions on Cryptographic Hardware and Embedded Systems (TCHES),  
    Volume 2023, Issue 4, DOI: https://doi.org/10.46586/tches.v2023.i4.344-366  

 -  Shih-Chun You:  
    _Single-trace template attacks on permutation-based cryptography_,  
    Apollo - University of Cambridge Repository,  
    PhD thesis, 2022, DOI: https://doi.org/10.17863/CAM.100592  

## Source code for our targets

The source code of the ASCON AEAD implementations on CW-Lite is available below.

	https://www.cl.cam.ac.uk/research/security/datasets/ascon/src_recording/ascon_src_website.zip

With the parameters and software version that we stated in our paper, we also include the following compiled HEX files for three different versions of ASCON-128 implementations in the above ZIP file:  

 -  **U-Os experiments,** an unmasked implementation with compiler optimization option "-Os":  
    ascon_src/simpleserial-ascon-aead-128/simpleserial-aead-CWLITEARM.hex
 -  **U-O3 experiments,** an unmasked implementation with compiler optimization option "-O3":
    ascon_src/simpleserial-ascon-aead-128-O3/simpleserial-aead-CWLITEARM.hex
 -  **M-Os experiments,** a masked implementation with compiler optimization option "-Os":  
    ascon_src/simpleserial-masked-ascon-aead-128/simpleserial-aead-CWLITEARM.hex

## Projects

We separated our attack Python code into three sub-projects by their target ASCON AEAD implementations:

 -  **U-Os experiments:** in `Project_U-Os/`
 -  **U-O3 experiments:** in `Project_U-O3/`
 -  **M-Os experiments:** in `Project_M-Os/`

