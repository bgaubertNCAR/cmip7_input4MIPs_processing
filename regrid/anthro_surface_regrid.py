#!/usr/bin/env python


### Module import ###
import xarray as xr
import glob
import sys
import os
from pathlib import Path


from Regridding_ESMF import Add_bounds, Regridding


def get_all_files(path):
    """Gets a list of all files in the given directory and its subdirectories."""
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if 'AIR' not in file:
                file_list.append(os.path.join(root, file))
    return file_list



def main():
    print("Welcome")
    """
    Regrid files from the source grid to the destination grid using templates. 
    The regridding is using ESMF and requires a "regridding_weights_file", which only has to be done once, set generate_weight_file = True,
    and if you have to relaunch the program because not all the emissions were created, you can just set it to False.
    Look at USER CHANGES carefully
    This script is for surface emissions ("AIR").
    """

    #####################################
    #           USER CHANGES            #
    #####################################
    # source grid
    CAMS_grid_file = "grids/ceds_surface_emission_grid.nc"      # source grid (has bounds)

    add_bounds_to_source_file = False
    CAMS_grid_file_with_bnds = CAMS_grid_file  # source grid with bounds

    dst_grid_file = "grids/ne30pg3.nc" # Destination grid
    
    ##############################
    # weight file
    generate_weight_file = True  # if Regridding_weights_file does not exist
    Regridding_weights_file =  "grids/anthro_ESMF_Weight_0.5x0.5_to_ne30.nc"

    # outputs
    path_out = "/glade/derecho/scratch/gaubert/cmip_outputs_2025/ne30/anthro/"

    # Inputs:
    path="/glade/derecho/scratch/gaubert/cmip_outputs_2025/anthro/CEDS-CMIP-2025-04-18/"


    #####################################
    #         USER CHANGES END          #
    #####################################

    file_list = get_all_files(path)

    if add_bounds_to_source_file:
        # first step: if bounds need to be added:
        Add_bounds(
            CAMS_grid_file,
            newfilename=CAMS_grid_file_with_bnds,
            creation_date=False,
            verbose=False,
        )

    # second step: if weight file needs to be created
    if generate_weight_file:
        print("########")
        print("Calculating re-gridding weight file")
        try:
            os.remove(Regridding_weights_file)
            print("removing existing weight file")
        except OSError:
            pass

        with xr.open_dataset(file_list[0]) as ds_CAMS:
            Regridding(
                ds_CAMS.isel(time=slice(0, 1)),
                src_grid_file=CAMS_grid_file,
                dst_grid_file=dst_grid_file,
                wgt_file=Regridding_weights_file,
                method="Conserve",
                save_wgt_file=True,
                save_results=False,
                save_wgt_file_only=True,
                check_timings=True,
                creation_date=False,
                nc_file_format="NETCDF3_64BIT_DATA",
            )

    # second step
    # weight file exists, now loop over the list of emissions

    for count, file_name in enumerate(file_list[:]):

        path_temp, file_temp = os.path.split(file_name)

        file_out= path_out + file_temp
        val=file_temp.find("2025-04-18")
        file_temp = file_temp[:val] + "2025-04-18" + file_temp[val+10:]
        file_out= path_out + file_temp
        print( file_out )


        my_file = Path(file_out)

        if my_file.exists():
            print(count, file_out, " already exists !!! ")
        else:

            print("### processing ", count, file_out)

            with xr.open_dataset(file_name) as ds_CAMS:
                Regridding(
                    ds_CAMS,
                    src_grid_file=CAMS_grid_file,
                    dst_grid_file=dst_grid_file,
                    wgt_file=Regridding_weights_file,
                    method="Conserve",
                    save_wgt_file=False,
                    save_results=True,
                    check_timings=True,
                    creation_date=False,
                    nc_file_format="NETCDF3_64BIT_DATA",
                    dst_file=file_out,
                    speed_up=True,
                )

    print("### End ###")

    return ()


if __name__ == "__main__":
    main()





