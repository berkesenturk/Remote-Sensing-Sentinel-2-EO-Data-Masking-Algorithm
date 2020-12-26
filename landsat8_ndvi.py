from tifffile import * 
from skimage import data
from skimage.viewer import ImageViewer
from skimage import io
import numpy as np


# image = imread('tiffiles/B11.tif')
# im_shape=image.shape
# print(im_shape)
# image_sequence = imread(['tiffiles/B1.tif', 'tiffiles/B2.tif','tiffiles/B3.tif','tiffiles/B4.tif',
#                          'tiffiles/B5.tif','tiffiles/B6.tif','tiffiles/B7.tif',
#                          'tiffiles/B9.tif','tiffiles/B10.tif','tiffiles/B11.tif'])
image_sequence = TiffSequence(['tiffiles/B*.tif'],pattern='axes')

#NDVI func example
def save_ndvi_file(nir =imread('tiffiles/B4.tif'),red = imread('tiffiles/B5.tif')):
    ndvi = (nir - red) / (nir + red)
    ndvi_des=(ndvi*255).astype(np.uint8)
        

    io.imsave('outputs/output.png', ndvi)
save_ndvi_file()