# Experiments on U-Os data set  

When we recorded our traces for experiments, we split the traces into five different groups: _Reference, Detection, Profiling (Training), Validation, and Attack (Testing)_. The code processing each of these groups can be found in

 -  **0001\_reference:** to find a reference trace for recording quality checking.
 -  **0002\_detection:** to determine points of interest (PoI). 
 -  **0003\_training:** to build our templates.
 -  **0004\_validation:** to validate our templates.
 -  **0005\_attack:** to recover keys used in ASCON AEAD with our attack scenario.

Please check the REAMDE.md in each subdirectory for detailed instructions.

The Python scripts for controlling the recording hardware and target hardware can be found seperately at

https://www.cl.cam.ac.uk/research/security/datasets/ascon/src_recording/CW_ASCON_recording_20240414.zip

Please check our [web site](https://www.cl.cam.ac.uk/research/security/datasets/ascon/index.html#U-Os-recording) for details on the configuration of the recording platform.  
