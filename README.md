Aida_data_parser

# Purpose:
Python 3.x script that takes data from AidaLight application data (in selected file) and saves it do csv file (in the same folder).

# What do next:
One can open this csv file in QGIS as a point layer (set the Geometry CRS to EPSG:4326) and view the photos by road_inspection_viewer plugin.

# AidaLight:
AidaLight is an Android very simple application that takes a photo every 0.7 second and save it into device memory folder named AidaLight_xxxx
(eg. for road inspection) with location data in a files. Be sure to chose the oldest (the biggest) location data file for this script.
AidaLight is a part of an old project with source code lost, so it is needed a conversion script for location data.

# License:
GNU General Public License, version 2.

