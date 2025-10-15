#!/bin/sh





path="/glade/derecho/scratch/gaubert/cmip_outputs_2025/bb/"
output_data_folder="/glade/derecho/scratch/gaubert/cmip_outputs_2025/bb/sum/"

path="/glade/derecho/scratch/gaubert/cmip_outputs_2025/ne30/bb/"
output_data_folder="/glade/derecho/scratch/gaubert/cmip_outputs_2025/ne30/bb/sum/"

#path="/glade/derecho/scratch/gaubert/cmip_outputs_2025/f19/bb/"
#output_data_folder="/glade/derecho/scratch/gaubert/cmip_outputs_2025/f19/bb/sum/"


mkdir $output_data_folder

cd $path

listvar="C3H6 C3H8 C2H6 C2H4 HigherAlkenes HigherAlkanes CH3COCH3 MEK CH3CHO CH2O C6H6 C7H8 C8H10"


dates="190001-202212 175001-189912"

#dates="175001-189912"
#dates="190001-202312"

for date in $dates ; do

    for var in $listvar ; do
        echo bb_cmip_${var}_input4MIPs_emissions_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_${date}.nc

	
        file=bb_cmip_${var}_input4MIPs_emissions_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_${date}.nc
        echo ${path}${file}
	exit


        ncdump -h  ${path}${file}
        ncrename -v ${var},bb ${path}${file} ${output_data_folder}${file}
    done

cdo -enssum ${output_data_folder}bb_cmip_*_input4MIPs_emissions_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_${date}.nc ${path}bb_cmip_IVOC_input4MIPs_emissions_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_${date}.nc

done



