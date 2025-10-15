#!/bin/sh





path="/glade/derecho/scratch/gaubert/cmip_outputs_2025/bb/"
output_data_folder="/glade/derecho/scratch/gaubert/cmip_outputs_2025/bb/sum/"

path="/glade/derecho/scratch/gaubert/cmip_outputs_2025/ne30/bb/smoothed/"
output_data_folder="/glade/derecho/scratch/gaubert/cmip_outputs_2025/ne30/bb/smoothed/sum/"

#path="/glade/derecho/scratch/gaubert/cmip_outputs_2025/f19/bb/"
#output_data_folder="/glade/derecho/scratch/gaubert/cmip_outputs_2025/f19/bb/sum/"


mkdir $output_data_folder

cd $path

listvar="C3H6 C3H8 C2H6 C2H4 HigherAlkenes HigherAlkanes C3H6O MEK C2H4O CH2O C6H6 C7H8 C8H10"


dates="190001-202112 175001-189912"

#dates="175001-189912"
#dates="190001-202312"

for date in $dates ; do

    for var in $listvar ; do

	
        file=bb_cmip_${var}smoothed_input4MIPs_emissions_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_${date}.nc
        echo ${path}${file}

	ls ${path}${file}

	if [ ! -f ${path}${file} ] ; then
		exit
	else
		ncdump -h  ${path}${file}
	fi

        ncrename -v ${var}smoothed,bb ${path}${file} ${output_data_folder}${file}

    done


cdo -enssum ${output_data_folder}bb_cmip_*smoothed_input4MIPs_emissions_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_${date}.nc ${path}bb_cmip_IVOCsmoothed_input4MIPs_emissions_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_${date}.nc

done






