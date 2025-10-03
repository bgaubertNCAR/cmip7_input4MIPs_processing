#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Ben Gaubert, gaubert@ucar.edu


KNOWN ISSUES/CHANGES

"""

#%%import packages
import netCDF4 as nc
import numpy as np
import xarray as xr
import time
import os
import fnmatch
import sys 
import glob
import ast
from pathlib import Path


# paths
import config

from get_sp import get_sp


def get_all_files(path):
    """Gets a list of all files in the given directory and its subdirectories."""
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_sectors(sector_in):

    # read in sectors and return a dictionnary:
    sectors=str(sector_in)

    # separate sectors:
    delim=";"
    temp = sectors.split(delim)

    # initialize dict:
    sector_dict= dict()

    delim_2=":"
    # using loop to reform dictionary with splits
    for idx, ele in enumerate(temp):
        #print(idx)
        actual_sector = ele.split(delim_2)
        sector_dict[idx] = actual_sector[1].replace(" ", "").replace(",", "_")
    return(sector_dict)

def open_and_process_anthro(file):


    with xr.open_dataset( file ) as emis_ds:
        sector_dict = get_sectors(emis_ds["sector"].attrs["ids"])
        var_name=emis_ds.attrs["variable_id"]
        nsector=len( emis_ds['sector'] )

    print( "variable name id: ", var_name )
    print( "Sector id: ", sector_dict )

    try:
        emis_ds[var_name][:,0,:,:]
    except:
        list_var = list( emis_ds.data_vars )
        var_name = list_var[0]
        print( var_name, "different from var id" )
            

    # split variables in sectors, rename with no space or commas
    for sect_index in range(nsector):
        var_array = xr.DataArray( emis_ds[var_name][:,sect_index,:,:], 
                                 coords={ "time" : (emis_ds.coords['time'] ), 'lat': emis_ds.coords['lat'], 'lon': emis_ds.coords['lon'] })
        var_array.attrs =  emis_ds[var_name].attrs
        var_array.attrs["sector"] = sector_dict[sect_index]

        emis_ds.update( { sector_dict[sect_index] : var_array } )

    emis_ds = emis_ds.drop_vars(var_name)
    emis_ds = emis_ds.drop_vars("sector_bnds")



    # Writing out
    path_temp, file_name = os.path.split(file)
    file_out = config.output_data_folder + file_name

    print("File out", file_out)
    emis_ds.to_netcdf( file_out )
    emis_ds.close()

    return()


def main():
    '''
    Author: Benjamin Gaubert (NSF NCAR / ACOM)

    Anthropogenic short-lived climate forcer (SLCF) and CO2 emissions

    The main function that takes cmip7 netcdf files as input and returns netcdf
    files with sectors splitted in different variables.
    
    Check out path and modify them in config.py:
    Input:
    path_to_explore
    path_to_explore_sup
    
    Output:
    output_data_folder
    '''

    # Check processing time
    timeStart = time.perf_counter()


    # inputs are separated in two set of directories
    # find all files in path and make a list:
    file_list = get_all_files(config.path_to_explore)


    # process each file separately
    for count,file in enumerate(file_list):
        print("File in", file)

        # Check for writing out
        path_temp, file_name = os.path.split(file)
        file_out = config.output_data_folder + file_name

        my_file = Path(file_out)
        if my_file.exists():
            print( count, file_out, " already exists !!! ")
        else:
            print("File in", file)
            if "AIR" not in file:
                open_and_process_anthro(file)

    file_list = get_all_files(config.path_to_explore_sup)


    # process each file separately
    for count,file in enumerate(file_list):

        # Check for writing out
        path_temp, file_name = os.path.split(file)
        file_out = config.output_data_folder + file_name

        my_file = Path(file_out)
        if my_file.exists():
            print( count, file_out, " alredady exists !!! ")
        else:
            print("File in", file)
            open_and_process_anthro(file)


    # Check processing time
    timeEnd = time.perf_counter()
    run_time = timeEnd-timeStart
    print('runtime is', run_time)


    return


if __name__ == '__main__':
    main()

