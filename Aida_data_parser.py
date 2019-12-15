"""
/***************************************************************************
  Aida_data_parser.py

  Python 3.x script that takes data from AidaLight application data (in selected file) and saves it to csv file (in the same folder).
  One can open this csv file in QGIS as a point layer (set the Geometry CRS to EPSG:4326) and view the photos by road_inspection_viewer plugin.

  version: 0.1.3
  
  --------------------------------------
  Date : 05.12.2019
  Copyright: (C) 2019 by Piotr Michałowski
  Email: piotrm35@hotmail.com
/***************************************************************************
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as published
 * by the Free Software Foundation.
 *
 ***************************************************************************/
"""


import os, sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
import xml.etree.ElementTree as ET
from Lat_Lon_extractor import Lat_Lon_extractor

		
#========================================================================================================

class EXIF_parser(QWidget):

    HEADER_TUPLE = ('lat', 'lon', 'time_stamp', 'file_names')


    def __init__(self):
        super().__init__()
        self.work()
        input('Press Enter to exit:')
        sys.exit()
        

    def work(self):
        try:
            lat_Lon_extractor = Lat_Lon_extractor()
            Aida_data_file_path = str(QFileDialog.getOpenFileName(self, "Select Aida data file:", None,"text files (*.txt)")[0])
            result_file_full_path = os.path.join(os.path.split(Aida_data_file_path)[0], "QGIS_CSV_EPSG4326_" + time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time())) + ".csv")
            result_file = open(result_file_full_path, 'w')
            print(','.join(self.HEADER_TUPLE))
            result_file.write(','.join(self.HEADER_TUPLE) + '\n')
            tree = ET.parse(Aida_data_file_path)
            root = tree.getroot()
            for child in root:
                lat = None
                lon = None
                time_stamp = None
                file_names = None
                for child2 in child:
                    try:
                        if str(child2.tag) == 'position_latitude':
                            lat_tuple = str(child2.text).split(' ')
                            lat = lat_Lon_extractor.get_lat_lon_str(lat_tuple)
                            continue
                        if str(child2.tag) == 'position_longitude':
                            lon_tuple = str(child2.text).split(' ')
                            lon = lat_Lon_extractor.get_lat_lon_str(lon_tuple)
                            continue
                        if str(child2.tag) == 'right_picture_file_name':
                            if not file_names:
                                file_names = str(child2.text)
                            else:
                                file_names += ';' + str(child2.text)
                            if not time_stamp:
                                time_stamp = file_names.replace('Right_cam_', '').replace('.jpg', '').replace('+', ':').replace('_', ' ')
                            continue
                        if str(child2.tag) == 'left_picture_file_name':
                            if not file_names:
                                file_names = str(child2.text)
                            else:
                                file_names += ';' + str(child2.text)
                            if not time_stamp:
                                time_stamp = file_names.replace('Left_cam_', '').replace('.jpg', '').replace('+', ':').replace('_', ' ')
                            continue
                    except:
                        break
                data_tuple = (lat, lon, time_stamp, file_names)
                if not None in data_tuple:
                    print(','.join(data_tuple))
                    result_file.write(','.join(data_tuple) + '\n')
        except Exception as e:
            print('work Exception: ' + str(e))
        finally:
            result_file.close()


#========================================================================================================


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EXIF_parser()
    sys.exit(app.exec_())




