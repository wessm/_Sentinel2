#!/usr/bin/env python3

import shapefile
import geojson

shape = shapefile.Reader('tiling_grid/shape/sentinel2_tiles_world.shp')

for feature in shape.shapeRecords():
    #print(feature.shape.__geo_interface__)
    print(feature.record[0])
    with open('{0}.geojson'.format(feature.record[0]), 'w') as outfile:
        geojson.dump(feature.shape.__geo_interface__, outfile)
