#!/usr/bin/env python3

import shapefile
import shapely_geojson
import geojson
from shapely.geometry import shape

shapefile = shapefile.Reader('tiling_grid/shape/sentinel2_tiles_world.shp')
records = shapefile.shapeRecords()
for feature in records:
    #print(feature.shape.__geo_interface__)
    print(feature.record[0])

    geom = shape(feature.shape).buffer(-0.001)
    geom2 = shapely_geojson.Feature(geom, properties={'name': feature.record[0]})
    #print(shapely_geojson.dumps(geom2))
    with open('{0}.geojson'.format(feature.record[0]), 'w') as outfile:
        outfile.write(shapely_geojson.dumps(geom2))
