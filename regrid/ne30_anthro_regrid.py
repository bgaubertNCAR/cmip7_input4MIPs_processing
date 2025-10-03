#!/usr/bin/env python   


### Module import ###
import numpy as np
import xarray as xr
import esmpy as ESMF
from pathlib import Path
import datetime, time, os
import cftime
from netCDF4 import Dataset
import subprocess
import glob
import sys
'''    "from dsj.array.chk import chk\n",
    "from dsj.plot.Plot_2D import Plot_2D\n",
    "from dsj.analysis.Calc_Emis import Calc_Emis_T\n",
    "from dsj.analysis.Regridding_ESMF import Add_bounds, Regridding\n",
    "from dsj.io.get_sp import get_sp\n",
    "import multiprocessing, psutil"
'''
# Duseong's program
from Regridding_ESMF import Add_bounds, Regridding


def main():
    print("Welcome")

    path="/glade/derecho/scratch/gaubert/cmip_outputs_2025/anthro/CEDS-CMIP-2025-04-18/"



    print("path=", path)

#    file_list = glob.glob( path + "*_input4MIPs_emissions_*.nc")
    #file_list = glob.glob( path + "*-em-anthro_input4MIPs_emissions_*.nc") 
    #file_list = glob.glob( path + "*_input4MIPs_emissions_*175001-179912.nc")
    #file_list = glob.glob( path + "*_input4MIPs_emissions_*195001-199912.nc")
    #file_list = glob.glob( path + "*_input4MIPs_emissions_*190001-194912.nc")

    # -em-anthro_
    file_list = glob.glob( path + "*_input4MIPs_emissions_*.nc" )


    print("there is ", len(file_list), "to regrid")
    print("first on the list is ", file_list[0]) 


    #for count, file_name in enumerate(file_list[:]):
    #    print("have to process these:", count, file_name)
    
    # 1st step => input grid in the correct format
    CAMS_grid_file="grids/VOC17-other-arom-em-speciated-VOC-anthro_input4MIPs_emissions_CMIP_CEDS-CMIP-2024-10-21-supplemental_gn_175001-179912.nc"
    #CAMS_grid_file="grids/grid_CAMS-GLOB-ANT_v5.3.nc"


    #print("create grid information (inputs)", CAMS_grid_file)
    # if Bounds need to be added then uncomment:
#    Add_bounds( file_list[0], newfilename=CAMS_grid_file, creation_date=False, verbose=False )

   
    # 2nd step => output grid in the right format
    # Regridding_weights_file 
    #dst_grid_file="ex_dst/fv09.nc"
    dst_grid_file="/glade/campaign/acom/MUSICA/grids/ne30pg3/ne30pg3.nc"
    dst_grid_file="ex_dst/2_ne30pg3.nc"

    grid_file_dst=dst_grid_file
    SERR_scrip_file=dst_grid_file
    # if Bounds need to be added then uncomment:
#    Add_bounds( dst_grid_file, newfilename=SERR_scrip_file, creation_date=False, verbose=False )

    ###
    generate_weight_file=False
    if generate_weight_file:
       print( "########")
       print( "Calculate re-gridding weight file (only need to be done once)" )    

       Regridding_weights_file="grids/weights_ne30.nc"
       ds_CAMS = xr.open_dataset( file_list[0])
       rr = Regridding( ds_CAMS.isel(time=slice(0,1)), src_grid_file=CAMS_grid_file, dst_grid_file=grid_file_dst,
                         wgt_file=Regridding_weights_file, method='Conserve', save_wgt_file=True, save_results=False,
                         save_wgt_file_only=True, check_timings=True, creation_date=False, nc_file_format='NETCDF3_64BIT_DATA' )
#       rr = Regridding( ds_CAMS, src_grid_file=CAMS_grid_file, dst_grid_file=grid_file_dst,
#                         wgt_file=Regridding_weights_file, method='Conserve', save_wgt_file=True, save_results=False,
#                         save_wgt_file_only=True, check_timings=True, creation_date=False, nc_file_format='NETCDF3_64BIT_DATA' )
       # Exit to make sure the file is ready
       #sys.exit()
    else:
       Regridding_weights_file="grids/weights_ne30.nc"


    ### Now that the regridding weight file is available
    # loop over species
    print("   ")
    print("   ")
    print("   ")


    path_out="/glade/derecho/scratch/gaubert/cmip_outputs_2025/ne30/anthro/"


    for count, file_name in enumerate(file_list[:]):
        print("Processing =", file_name)


        path_temp, file_temp = os.path.split(file_name)

        file_out= path_out + file_temp
        val=file_temp.find("2025-04-18")
        file_temp = file_temp[:val] + "2025-04-18" + file_temp[val+10:]
        file_out= path_out + file_temp
        print( file_out )


        my_file = Path(file_out)

        if my_file.exists():
           print( count, file_out, " already exists !!! ")
        else:
           print( "### processing ", count, file_out)


           with xr.open_dataset(file_name) as ds_CAMS:
                rr = Regridding( ds_CAMS, src_grid_file=CAMS_grid_file, dst_grid_file=grid_file_dst,
                         wgt_file=Regridding_weights_file, method='Conserve', save_wgt_file=False, save_results=True,
                         check_timings=True, creation_date=False, nc_file_format='NETCDF3_64BIT_DATA',  dst_file=file_out, speed_up=True)

           #sys.exit()
    print("### End ###")



    return()








if __name__ == '__main__':
   main()





