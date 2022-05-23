# Final year project: Use of harmonic hall effect in characterising spintronic devices

## Instructions of use for repository:
The repository is organised into different sections:
- Data
- Analysis
- Data processing

### Data
The data folder includes data for sample A and sample B. There is also a csv file for the magnet calibration. The data included is the same data used for analysis in the report in section I: Extracting a spin Hall angle.

### Analysis
The analysis is conducted in Jupyter notebook files. These include:
- sample_A_analysis.ipynb
- sample_B_analysis.ipynb
- magnet_calibration.ipynb

The sample A and sample B analysis files include all relevant analysis to go from a raw data collected using experimental equipment at Loughborough University, to a spin Hall angle. The notebooks are generic, and any harmonic hall measurement data can be used for analysis in the analysis notebook provided the imported csv containing the data is in the correct format.

### Data processing 
The data processing includes a 'txt to csv script' and a 'read_csv.py'.

##### txt to csv script
To run this process, run the 'reading_file_script.py' script from the terminal. Files are to be put in the 'processor' folder before running the script. Make sure to only run the script once on each data txt file. It is necessary to create three folder called 'archive_of_original_files', 'processed_data' and 'processor'. The file paths for these folder are to be input into the code.

##### read_csv.py
This file includes a function that reads the csv in a certain way, such that it can consistently be interacted with in the jupyter notebook. The file is imported at the beginning of the notebook, and the function is called when needed.
