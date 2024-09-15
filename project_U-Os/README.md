# Experiments on U-Os data set  

When we recorded our traces for experiments, we categorized the traces into five different groups: _Reference, Detection, Profiling (Training), Validation, and Attack (Testing)_. In this repository, we **DO NOT** include our Python scripts for recording, but they can be found  in the following link:

    https://www.cl.cam.ac.uk/research/security/datasets/ascon/src_recording/CW_ASCON_recording_20240414.zip

Please check our [university webpage](https://www.cl.cam.ac.uk/research/security/datasets/ascon/index.html#U-Os-recording) for any interest in recording with the same National Instruments platform.  

When we recorded our traces for experiments, we categorized the traces into the following five groups in separate subdirectories:  
 -  **0001\_reference:** to find a reference trace for recording quality checking.
 -  **0002\_detection:** to determine points of interest (PoI). 
 -  **0003\_training:** to build our templates.
 -  **0004\_validation:** to validate our templates.
 -  **0005\_attack:** to recover keys used in ASCON AEAD with our attack scenario.

Please check the REAMDE.md in each subdirectory for detailed instructions.
