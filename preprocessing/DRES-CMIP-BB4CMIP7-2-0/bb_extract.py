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
import config_bb


def dict_replace(da, to_replace, value):
    d = {k: v for k, v in zip(to_replace, value)}
    out = np.vectorize(lambda x: d.get(x, x))(da.values)
    return da.copy(data=out)


def get_all_files(path):
    """Gets a list of all files in the given directory and its subdirectories."""
    file_list = []
    for root, dirs, files in os.walk(path):
        if "percentage" not in root and "datasource" not in root and "bulk" not in root:
            for file in files:
                file_list.append(os.path.join(root, file))
    return file_list


def get_molecular_weight(var_name, emis_ds):
    mw= emis_ds[var_name].attrs['molecular_weight'].split()

    if mw[-1]=='object':
        for mw_val in mw:
            try:
                actual_mw = float(  mw_val  )
                break
            except ValueError:
                pass
    else:
        actual_mw = float(  mw[-1]  )
    return(actual_mw)



def open_and_process_bb(file, file_out):
    " path to open "

    print( file )

    with xr.open_dataset(file) as emis_ds:
        # Regridding required lat and lon dimensions and variables instead of latitude and longitude
        emis_ds = emis_ds.swap_dims( {  "latitude": "lat",  "longitude": "lon"} )
        emis_ds = emis_ds.rename( {  "latitude": "lat",  "longitude": "lon"} )

        ########################################
        # create a 'molecular_weight' attribute
        var_name=emis_ds.attrs["variable_id"]
        print( var_name,  emis_ds[var_name] )

        emis_ds[var_name] = emis_ds[var_name].fillna(0.)
        emis_ds[var_name].attrs['molecular_weight'] = get_molecular_weight(var_name, emis_ds)

        # Writing out
        print("File out", file_out)
        emis_ds.to_netcdf( file_out )
        emis_ds.close()

    return()



def main():
    '''
    Author: Benjamin Gaubert (NSF NCAR / ACOM)

    
    The main function that takes cmip7 netcdf files as input and returns netcdf
    files with latitude and longitude renamed, and include molecular_weight attributes as a float variable.

    Check out path and modify them in config_bb.py:

    Input:
    path_to_explore

    Output:
    output_data_folder
    '''

    # Check processing time
    timeStart = time.perf_counter()


    # inputs are separated in two set of directories
    # First one first:
    # find all files in path and make a list:
    file_list = get_all_files(config_bb.path_to_explore)


    # process each file separately
    for count,file in enumerate(file_list):
        print("File in", file)
        path_temp, file_name = os.path.split(file)
        file_out = config_bb.output_data_folder + "bb_cmip_" + file_name

        my_file = Path(file_out)
        if my_file.exists():
            print( count, file_out, " alredady exists !!! ")
        else:
            open_and_process_bb(file, file_out)

    # Check processing time
    timeEnd = time.perf_counter()
    run_time = timeEnd-timeStart
    print('runtime is', run_time)

    return()


if __name__ == '__main__':
    main()



