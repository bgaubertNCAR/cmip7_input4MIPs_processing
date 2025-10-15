#!/usr/bin/env python   


### Module import ###
import numpy as np
import xarray as xr
import esmpy as ESMF
import datetime, time, os
import cftime
from netCDF4 import Dataset
import subprocess
import glob
import sys


from Species_Mapping import sp_map

def main():

    print("Welcome")
    """
    emissions mapping, look at the .dat files in list_anthro and list_bb.
    """

    # fire

    file_name="list_bb/smoothed_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_175001-189912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_bb/smoothed_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_190001-202112.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)


    sys.exit()


    print( " ######################################### ")
    print( "em-anthro_CMIP_CEDS-CMIP-2025-04-18_gn")
    print( "175001-179912" )
    file_name="list_anthro/em-anthro_CMIP_CEDS-CMIP-2025-04-18_gn_175001-179912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    print( "180001-184912" )
    file_name="list_anthro/em-anthro_CMIP_CEDS-CMIP-2025-04-18_gn_180001-184912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    print( "185001-189912" )
    file_name="list_anthro/em-anthro_CMIP_CEDS-CMIP-2025-04-18_gn_185001-189912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True )

    print( "190001-194912" )
    file_name="list_anthro/em-anthro_CMIP_CEDS-CMIP-2025-04-18_gn_190001-194912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    print( "195001-199912" )
    file_name="list_anthro/em-anthro_CMIP_CEDS-CMIP-2025-04-18_gn_195001-199912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    print( "200001-202312" )
    file_name="list_anthro/em-anthro_CMIP_CEDS-CMIP-2025-04-18_gn_200001-202312.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)



    print( " ######################################### ")
    
    file_name="list_bb/smoothed_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_175001-189912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_bb/smoothed_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_190001-202312.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    # fire
    file_name="list_bb/CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_175001-189912"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_bb/CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_190001-202112"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)


    # fire
    file_name="list_bb/CMIP_DRES-CMIP-BB4CMIP7-2-1_gn_175001-189912"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_bb/CMIP_DRES-CMIP-BB4CMIP7-2-1_gn_190001-202312"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)


    print( " ######################################### ")


    ##################
    # Anthro biofuel
    file_name="list_anthro/limited_list_SOLID-BIOFUEL_short_mapping_175001-179912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_anthro/limited_list_SOLID-BIOFUEL_short_mapping_180001-184912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_anthro/limited_list_SOLID-BIOFUEL_short_mapping_185001-189912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_anthro/limited_list_SOLID-BIOFUEL_short_mapping_190001-194912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_anthro/limited_list_SOLID-BIOFUEL_short_mapping_195001-199912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)

    file_name="list_anthro/limited_list_SOLID-BIOFUEL_short_mapping_200001-202312.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True)


    print( "CMIP_CEDS-CMIP-2025-04-18-supplemental" )
    print( "175001-179912" )
    file_name="list_anthro/CMIP_CEDS-CMIP-2025-04-18-supplemental_gn_175001-179912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True, VOC_fix=True )
    
    file_name="list_anthro/CMIP_CEDS-CMIP-2025-04-18-supplemental_gn_180001-184912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True, VOC_fix=True )
    
    file_name="list_anthro/CMIP_CEDS-CMIP-2025-04-18-supplemental_gn_185001-189912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True, VOC_fix=True )
    
    file_name="list_anthro/CMIP_CEDS-CMIP-2025-04-18-supplemental_gn_190001-194912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True, VOC_fix=True )
    
    file_name="list_anthro/CMIP_CEDS-CMIP-2025-04-18-supplemental_gn_195001-199912.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True, VOC_fix=True )
    
    file_name="list_anthro/CMIP_CEDS-CMIP-2025-04-18-supplemental_gn_200001-202312.dat"
    sp_map(file_name, nc_file_format='NETCDF3_64BIT_DATA', print_user_nl_cam=True, keep_sector=False, ignore_warning=False, verbose=True, VOC_fix=True )


    return()


if __name__ == '__main__':
   main()




#
