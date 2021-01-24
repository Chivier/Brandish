#!/bin/python3

import netCDF4 as nc4

datafile = './full/data/2017-11-02T03_00_00_MET.nc'
dataset = nc4.Dataset(datafile)

print(dataset)