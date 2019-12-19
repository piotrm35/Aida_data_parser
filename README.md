Aida_data_parser

# Purpose:
Road inspection.
Python 3.x script that takes location data from AidaLight application data (in selected file) and saves it to csv file (in the same folder).

# What do next:
One can open this csv file in QGIS as a point layer (set the Geometry CRS to EPSG:4326) and view the photos by road_inspection_viewer plugin.

# AidaLight:
AidaLight (the installer is in the AidaLight_0.7_install folder) is an Android very simple application that takes a photo every 0.7 second 
and saves it into device memory folder named AidaLight_xxxx with location data in a files. Be sure to chose the oldest (the biggest) location 
data file for this script.
AidaLight is a part of my old project with source code lost, so it is needed a conversion script for location data.

# How to run it directly on Windows (Windows 10 x64):
Unpack the file Aida_data_parser.7z and run Aida_data_parser.exe.

# License:
GNU General Public License, version 2.

