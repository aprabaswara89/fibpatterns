# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:41:30 2021

Create a hexagonal array of nanorings, with specified outer radius, wall thickness, and pitch

@author: adipr48
"""

import pya
import numpy as np

#array parameter
## Only edit between these lines ##
r2 = 1000           # Outer radius
thickness = 100     # Ring thickness
a = 3000            # pitch
i = 4               # number of instances, even number


## Only edit between these lines ##

r1 = r2-thickness   # inner radius in nm

#initialize
layout = pya.Layout()
top = layout.create_cell('top')
c_circle = layout.create_cell('circle')
l_circle = layout.layer(1,0)

# make ring
nr_points = 64 #number of points
angles = np.linspace(0,2*np.pi,nr_points+1)[0:-1]
points1 = [] #array of point
points2 = []

for angle in angles:
    points1.append(pya.Point(r1*np.cos(angle),r1*np.sin(angle)))
    points2.append(pya.Point(r2*np.cos(angle),r2*np.sin(angle)))
    

circle1 = pya.SimplePolygon(points1)
circle2 = pya.SimplePolygon(points2)

c2 = pya.Region()
c2.insert(circle2)

c1 = pya.Region()
c1.insert(circle1)

result = c2-c1

#for hexagonal grid

c_circle.shapes(l_circle).insert(result)
c_circle.shapes(l_circle).insert(result.moved(0.5*a*np.sqrt(3),a/2))

trans = pya.Trans(pya.Point(0,0))

new_instance = pya.CellInstArray(c_circle.cell_index(),trans,pya.Vector(a*np.sqrt(3), 0 ), pya.Vector(0, a), i/2, i/2)
top.insert(new_instance)

options = pya.SaveLayoutOptions()
options.format = "DXF"
options.dxf_polygon_mode = 3

layout.write("Rings Radius " + str(r2)+ " thickness " + str(thickness) + ".dxf",options)
