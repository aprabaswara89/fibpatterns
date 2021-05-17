# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:41:30 2021

@author: adipr48

Script for creating seven nanorings arranged in a hexagonal array with one ring at the center
Adjust dimension variable r2, thickness, and a
Output file in dxf
"""

import pya
import numpy as np


## Only edit between these lines ##

#Ring parameters in nm
r2 = 500 # outer radius
thickness = 100
r1 = r2-thickness # inner radius in nm

a = 1500 #pitch
## Only edit between these lines ##


#initialize
layout = pya.Layout()
c_circle = layout.create_cell('circle')
l_circle = layout.layer(1,0)

# make a ring shape
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

c_circle.shapes(l_circle).insert(result)

# Create coordinate for surrounding rings

hex_angles = np.linspace(0,2*np.pi,7)[0:-1]
hex_x = r1*np.cos(hex_angles) 
hex_y = r1*np.sin(hex_angles)

# Draw surrounding rings

for angle in hex_angles:
    c_circle.shapes(l_circle).insert(result.moved(a*np.cos(angle), a*np.sin(angle)))



options = pya.SaveLayoutOptions()
options.format = "DXF"
options.dxf_polygon_mode = 3

file_output = "7 Rings Radius " + str(r2)+ " thickness " + str(thickness) + ".dxf"

layout.write(file_output,options)

print("File saved as " + file_output)
