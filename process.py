"""burada ndvi sonucunu işleyen fonksiyon yazılcak

iterate nir üzerinde nir 0 ise ndvi'dada 0 yapılcak
"""

import matplotlib.pyplot as plt
from skimage import *
from skimage import io
import numpy as np
from skimage.viewer import ImageViewer
from tifffile import * 
import matplotlib.patches as mpatches   

red = io.imread('tiffiles/B4.tif')
nir = io.imread('tiffiles/B5.tif')

np.seterr(divide='ignore', invalid='ignore')
ndvi = (nir - red) / (nir + red)
ndvi= np.nan_to_num(ndvi)
print(red)
print(nir)

for array in ndvi:
    for array_2_ndvi in array:
        for array_3_ndvi in array_2_ndvi:
            for array in nir:
                for array_2_nir in array:
                    for array_3_nir in array_2_nir:
                        if (array_3_nir == 0 and array_3_ndvi != 0):
                                array_3_ndvi=0
                                print(ndvi)
        
