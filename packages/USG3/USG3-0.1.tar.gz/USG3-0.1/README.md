# Background
The USGS 3DEP project (United States Geological Survey 3D Elevation Program) aims at responding to growing needs for high-quality topographic data and a wide range of 3D data representation of the county’s features. You can read about the full project here.
The data is stored in a repository on an amazon server. The server contains geospatial data on over 1000 geographical regions. The data stored is in a .ept JSON file format. Entwine Point Tile format (ept)is a simple way to store data. It achieves this by a simple tree-based format. To enable processing ept has crucial keys that enable smooth processing. The dataset is however very complicated to understand

Hence this project aims to create a package to interact with the data and process it into a less complex file

# Data

Download USGS 3DEP data from here

# Folders
jsons-folder contains all pipleines in form of .ept.json files

laz-stores processed laz files

tif-stores .tif files

notebooks- contains notebooks used


<<<<<<< HEAD
## notebooks

scripts- folder contains python scripts used int he project

## scripts
=======


# Package

The package is naed USG3, to download and use it follow this steps.

Before Interacting with the package ensure you go through and have the ept file located in the jsons folder labelled ``` user.json ``` 

## Installation


``` python setup.py sdist bdist_wheel ``` - This makes the package available for local system usage  

>>>>>>> 5008b8b2173e1144705e22b428283a3ac74ca6ac
``` classification.py ``` allows user to define classification for pipeline processing

``` generate.py ``` base script to generate new tif and laz files

``` reprojection.py ``` this script reprojects the sh files into a standard format using geopandas

<<<<<<< HEAD
=======
``` elevation_data.py ``` this script calculates elevation and returns a geodataframe and a csv file containing elevation and geometry data

``` visualize.py ``` this script contains all visaulization libraries for the data.

## Download

After that you can now run ``` pip install USG3 ``` to your respective scripts

## Tutorial 

Simple tutorials on how to interact with the API are available in the notebooks folder.

``` scriptdemonstration.ipynb ``` this contains tutorial on basic preprocessing and interaction of the API with the data

``` plotting bounds.ipynb ``` this illustrate how user can define bounds and plot the map of the bounds in respect to the general area

``` standardizing points ``` this tutorial highlights how to standardize elevation and points of the data and plot them 

``` testfile.html ``` is an example 3d render obtained from the scriptdemonstration notebook

>>>>>>> 5008b8b2173e1144705e22b428283a3ac74ca6ac


# Resources
https://www.usgs.gov/core-science-systems/ngp/3dep/what-is-3dep?qt-science_support_page_related_con=0#qt-science_support_page_related_con

https://entwine.io/entwine-point-tile.html

# Badges
[![GitHub issues](https://img.shields.io/github/issues/Blvisse/USG3-DataEngineering?style=for-the-badge)](https://github.com/Blvisse/USG3-DataEngineering/issues)
[![GitHub forks](https://img.shields.io/github/forks/Blvisse/USG3-DataEngineering?style=for-the-badge)](https://github.com/Blvisse/USG3-DataEngineering/network)
[![GitHub license](https://img.shields.io/github/license/Blvisse/USG3-DataEngineering?style=for-the-badge)](https://github.com/Blvisse/USG3-DataEngineering)
