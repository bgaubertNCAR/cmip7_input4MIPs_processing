
Author: 
Benjamin Gaubert (NSF NCAR / ACOM)


Date: 
Thursday 2 October 2025


Purpose:
The goal is to look over the input4MIPs_raw emission files, specifically:
	1. Anthropogenic SLCF and CO2 Emissions (i.e. CEDS / PNNL-JGCRI)
	2. Open Biomass Burning Emissions (i.e., DRES-CMIP-BB4CMIP7)

The input dataset is then processed to i) conservatively regridded to the CESM grid, ii) emission fluxes are provided in the right units for CESM.
The workflow consists in:
 a) process the file to work with the regridding function used in step b
 b) regridding to the destination grid
 c) mapping the chemistry and species to the correct input format
 d) concatenate the files (optional)

Inputs:

1. Anthropogenic SLCF and CO2 Emissions (i.e. CEDS / PNNL-JGCRI):
/glade/campaign/cesm/cesmdata/input4MIPs_raw/input4MIPs/CMIP7/CMIP/PNNL-JGCRI/CEDS-CMIP-2025-04-18/atmos/mon/
/glade/campaign/cesm/cesmdata/input4MIPs_raw/input4MIPs/CMIP7/CMIP/PNNL-JGCRI/CEDS-CMIP-2025-04-18-supplemental/atmos/mon/

2. Open Biomass Burning Emissions (i.e., DRES-CMIP-BB4CMIP7)
/glade/campaign/cesm/cesmdata/input4MIPs_raw/input4MIPs/CMIP7/CMIP/DRES/DRES-CMIP-BB4CMIP7-2-0/atmos/mon/

    
Outputs:

path format: /glade/campaign/acom/MUSICA/emis/cmip7/ + grid directory (ne30, f09) + / + dataset (DRES-CMIP-BB4CMIP7-2-0, CEDS-CMIP-2025-04-18) +
file formats:




Detailed workflow:

a) preprocessing/

   1. example for anthropogenic emissions (e.g., PNNL-JGCRI/CEDS-CMIP-2025-04-18)
	directory: anthro_v2025-04-18/

	job_casper script to run the job on casper
	It does two things, 1. load a python conda environment, and 2. run preprocess_cmip7.py
	
        preprocess_cmip7.py is reading paths from config.py

	edit config.py with input paths:

	path_to_explore="/glade/campaign/cesm/cesmdata/input4MIPs_raw/input4MIPs/CMIP7/CMIP/PNNL-JGCRI/CEDS-CMIP-2025-04-18/atmos/mon/"
	path_to_explore_sup="/glade/campaign/cesm/cesmdata/input4MIPs_raw/input4MIPs/CMIP7/CMIP/PNNL-JGCRI/CEDS-CMIP-2025-04-18-supplemental/atmos/mon/"

        and outputs (user specific): output_data_folder = '/glade/derecho/scratch/gaubert/cmip_outputs_2025/anthro/CEDS-CMIP-2025-04-18/'

	The purpose of preprocess_cmip7.py is just to edit the emission flux variable's vector from (time, sector, lat, lon) to variable for each sectors with dimenstions (time, lat, lon)

	for example: N2O_em_anthro has 7 sectors (also spaces were removed)
	Sector id:  {0: 'Agriculture', 1: 'Energy', 2: 'Industrial', 3: 'Transportation', 4: 'Residential_Commercial_Other', 5: 'Solventsproductionandapplication', 6: 'Waste', 7: 'InternationalShipping'}
         In the outputs there will 7 vectors like Transportation(time, lat, lon) or Residential_Commercial_Other(time, lat, lon)

         Notes: Aircraft emissions do not need to be processed, they alreay are in the acceptable (time, level, lat, lon) format.


   2. Example for fire emissions (DRES-CMIP-BB4CMIP7-2-0)
	directory: DRES-CMIP-BB4CMIP7-2-0

        job_casper script to run the job on casper
        It does two things, 1. load a python conda environment, and 2. run bb_extract.py

        There are 2 paths to edit in config_bb.py  


b) regrid/
   For all 3 jobs (aircraft, anthro and fire), you need to edit the path in USER CHANGES

   There is a need for a source grid (native cmip7 emissions), a destination grid (f09, ne30 etc), and the paths for inputs and outputs.
   You can point to an existing weight file and create one.

   Note that pointing to the same destination grid, and weight file can make the program to crash.
 
   1. job_aircraft script to run the job on casper
	job to run aircraft_regrid.py, reading the following path:
	/glade/campaign/cesm/cesmdata/input4MIPs_raw/input4MIPs/CMIP7/CMIP/PNNL-JGCRI/CEDS-CMIP-2025-04-18/atmos/mon/
   2. job_surface script to run anthro_surface_regrid.py
   3. job_bb script to run bb_surface_regrid.py

   All the regridding jobs are using the Regridding_ESMF.py and Calc_Emis.py codes.

b.2) bb_IVOC/
   Once you have the fire emissions regridded, there is a need to produce the IVOC species.
   The script is sum_IVOC.sh, it uses cdo. 

c) remapping/
   job_casper is the script running mozart.py
   mozart.py uses Species_Mapping and input the text files .dat in list_anthro and list_bb to map the chemicals to the TS1 mechanism.
   One of the main function is to convert from Source_unit = 'kg m-2 s-1' to the Destination_unit = 'molecules cm-2 s-1',
   but it also map the chemicals into the mechanism, and produce vertical emissions for sulfates (so4) from anthropogenic sources (industry and power sector specifically).
   
   The outputs should be "CESM ready", making the next step optional if you are running shorter simulations.

d) concat/
   The provided files contain 175001-189912 and 190001-202312 periods for DRES-CMIP-BB4CMIP7 and 175001-179912, 180001-184912, 185001-189912, 190001-194912, 195001-199912, 200001-202312 for CEDS-CMIP.
   The scripts are using ncrcat to produce files with the whole record.


Notes:
   The programs are designed to process a file only if the output file does not exist, so that if the programs does not have time to process them all,
   it can produce only the remaining files.
   This means you might want to delete an output file in case it has not been fully and correctly processed.





