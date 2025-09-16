# Crystal-Orbital-Hamilton-Population-COHP-analysis
Workflow
1. Relax the structure.
2. Do a scf calculation based on the relaxed structure. The key output is WAVECAR so need to have 'LWAVE =T' and 'LORBIT = 12'.
3. Just in the scf folder, modify the 'lobsterin' file based on your requirment and use run_lobster to submit the job.
4. Use 'draw_cohp.py' to draw the COHP pdf.
