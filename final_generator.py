# Import packages
import elevation
import netCDF4 as nc4
import numpy as np
import rasterio
import math
import plotly.graph_objects as go
import pandas as pd

# Set grid size
final_grid_x = 130
final_grid_y = 100

# Set target map
target_x_1 = 117.8
target_x_2 = 118
target_y_1 = 30.5
target_y_2 = 30.7

elevation_dataset = None
elevation_data = None
filling_dataset = None
filling_data = None

x_step_length = None
y_step_length = None

# GIS data
filling_x_step = 0.01
filling_y_step = 0.01
filling_x_st = 15.005
filling_y_st = 70.005


def Initialize():
    global elevation_dataset
    global elevation_data
    global filling_dataset
    global filling_data
    global final_grid_x
    global final_grid_y
    global x_step_length
    global y_step_length

    # Step length
    x_step_length = (target_x_2 - target_x_1) / final_grid_x
    y_step_length = (target_y_2 - target_y_1) / final_grid_y

    # Download elevation data
    # elevation.clip(
    #     bounds=(117.8 - 0.1, 30.5 - 0.1, 118 + 0.1, 30.7 + 0.1), output="data.tif"
    # )

    # Load elevation data
    elevation_dataset = rasterio.open("data.tif")
    elevation_data = elevation_dataset.read(1)

    # Read filling data
    filling_dataset_path = "resources/full/gasdata/NO2/TROPOMI_NO2_VCD_2019-07-07.nc"
    filling_dataset = nc4.Dataset(filling_dataset_path)
    filling_data = filling_dataset.variables["weights"][:]


# SearchByIndex
# Return the elevation or filling data
# type = 1: return elevation
# type = 2: return filling data
def SearchByIndex(type, x, y):
    # print(x, y)
    if type == 1:
        index_x, index_y = elevation_dataset.index(x, y)
        return elevation_data[index_x, index_y]
    else:
        index_x = (int)((y - filling_x_st) / filling_x_step)
        index_y = (int)((x - filling_y_st) / filling_y_step)
        return filling_data[index_x, index_y]


# MapGenerator
# Print out the map
# type = 1: print elevation
# type = 2: print filling data
def MapGenerator(type):
    x = target_x_1
    x_index = 1

    result = []
    while x_index <= final_grid_x:
        line = []
        y = target_y_1
        y_index = 1
        while y_index <= final_grid_y:
            line.append(SearchByIndex(type, x, y))
            y = y + y_step_length
            y_index = y_index + 1
        x = x + x_step_length
        x_index = x_index + 1
        result.append(line)
    return np.array(result)


def Plot(data1, data2):
    x_axis = np.arange(target_x_1, target_x_2, x_step_length)
    y_axis = np.arange(target_y_1, target_y_2, y_step_length)
    # print(x_axis.size, y_axis.size)
    fig = go.Figure(
        go.Surface(
            contours={
                "x": {
                    "show": True,
                    "start": 1.5,
                    "end": 2,
                    "size": 0.04,
                    "color": "white",
                },
                "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05},
            },
            x=x_axis,
            y=y_axis,
            z=data1,
        )
    )

    fig.update_layout(
        scene={
            "xaxis": {"nticks": 20},
            "zaxis": {"nticks": 4},
            "camera_eye": {"x": 0, "y": -1, "z": 0.5},
            "aspectratio": {"x": 1, "y": 1, "z": 0.2},
        }
    )
    fig.show()


Initialize()
data1 = MapGenerator(1)
data2 = MapGenerator(2)
print(data1.shape)
print(data2.shape)
Plot(data1, data2)