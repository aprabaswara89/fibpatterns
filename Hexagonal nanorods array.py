# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:41:30 2021

@author: adipr48

Create a hexagonal array of circles with defined radius,
pitch, and numer of instances
"""

import pya
import numpy as np

# Only edit between these lines
#array parameter
radius = 100 #radius in nm
a = 500 #pitch

#number of instances, even number
i=6
# Only edit between these lines

#initialize
layout = pya.Layout()
top = layout.create_cell('top')
c_circle = layout.create_cell('circle')
l_circle = layout.layer(1,0)

# make a circle pcell
nr_points = 32 #number of points

#create an array of angles
angles = np.linspace(0,2*np.pi,nr_points+1)[0:-1]
points = [] #array of point
for angle in angles:
    points.append(pya.Point(radius*np.cos(angle),radius*np.sin(angle)))
circle = pya.SimplePolygon(points)

#for hexagonal grid


c_circle.shapes(l_circle).insert(circle)
c_circle.shapes(l_circle).insert(circle.moved(0.5*a*np.sqrt(3),a/2))

trans = pya.Trans(pya.Point(0,0))

new_instance = pya.CellInstArray(c_circle.cell_index(),trans,pya.Vector(a*np.sqrt(3), 0 ), pya.Vector(0, a), i/2, i/2)
top.insert(new_instance)

options = pya.SaveLayoutOptions()
options.format = "DXF"
options.dxf_polygon_mode = 3

file_output = "Radius " + str(radius)+ " pitch " + str(a) + ".dxf"

#layout.write("test.gds")
layout.write(file_output, options)
print("File saved as " + file_output)
