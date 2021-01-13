import matplotlib.pyplot as plt
from skimage import *
from skimage import io
import numpy as np
from skimage.viewer import ImageViewer
from tifffile import * 
import matplotlib.patches as mpatches   

def create_ndwi(green_band,nir_band):
    """
    -----------
    Definition
    -----------

    NDWI calculator

    input params
    ------------

    nir_band : tiff file
    green_band : tiff file 
    
    output
    ------

    img : tiff file 
    """
    np.seterr(divide='ignore', invalid='ignore')
    ndwi = (nir_band - green_band) / (nir_band + green_band)
    ndwi= np.nan_to_num(ndwi)
    return ndwi
    
def create_ndvi(nir_band,red_band):
    """
    -----------
    Definition
    -----------

    NDVI calculator

    input params
    ------------

    red_band : tiff file
    nir_band : tiff file

    output
    ------

    img : tiff file 
    """
    np.seterr(divide='ignore', invalid='ignore')
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    ndvi= np.nan_to_num(ndvi)
    return ndvi

def water_mask_ndvi_for_landsat_8(ndvi_band,nir_band):
    """
    -----------
    Definition
    -----------

    Mask for water bodies

    input params
    ------------

    ndvi_band : tiff file
    nir_band : tiff file

    output
    ------

    img : tiff file 
    """
    ndvi_in_uint = (ndvi_band*255).astype('uint8')
    for x in range(ndvi_in_uint.shape[0]):
        for y in range(ndvi_in_uint.shape[1]):
            if (ndvi_in_uint[x][y][1]!=0 and nir_band[x][y][1]<=100): 
                ndvi_in_uint[x][y][1]=0
    
    img = ndvi_in_uint[:, :, 1]
    return img

def water_mask_ndvi_for_sentinel_2(ndvi_band,nir_band):
    """
    -----------
    Definition
    -----------

    Mask for water bodies

    input params
    ------------

    ndvi_band : tiff file
    nir_band : tiff file

    output
    ------

    img : tiff file 
    """
    
    for x in range(len(ndvi_band)):
        for y in range(x):
            if (ndvi_band[x][y]!=0 and nir_band[x][y]<=0.1): 
                ndvi_band[x][y]=0
    
    img = ndvi_band
    return img
    
def water_mask_ndwi_for_landsat_8(ndwi_band,nir_band):
    """
    -----------
    Definition
    -----------

    Mask for water bodies

    input params
    ------------

    ndvi_band : tiff file
    nir_band : tiff file

    output
    ------

    img : tiff file 
    """
    ndwi_in_uint = (ndwi_band*255).astype('uint8')
    for x in range(ndwi_in_uint.shape[0]):
        for y in range(ndwi_in_uint.shape[1]):
            if (ndwi_in_uint[x][y][1]!=0 and nir_band[x][y][1]<=50): 
                ndwi_in_uint[x][y][1]=0
    
    img = ndwi_in_uint[:, :, 1]
    return img

def water_mask_ndwi_for_sentinel_2(ndwi_band,nir_band):
    """
    -----------
    Definition
    -----------

    Mask for water bodies

    input params
    ------------

    ndvi_band : tiff file
    nir_band : tiff file

    output
    ------

    img : tiff file 
    """
    
    for x in range(len(ndwi_band)):
        for y in range(x):
            if (ndwi_band[x][y]!=0 and nir_band[x][y]<=0.1): 
                ndwi_band[x][y]=0
    
    img = ndwi_band
    return img
    
if __name__=='__main__':
    red = io.imread('test_images_tiff/B4.tif')
    nir = io.imread('test_images_tiff/B5.tif')
    swir = io.imread('test_images_tiff/B7.tif')
    
    ndvi=create_ndvi(nir_band=nir,red_band=red)

    # masked image
    img=water_mask_ndvi(ndvi_band=ndvi,nir_band=nir)

    plt.title("NDVI Map of Landsat 8 Satellite Imagery")
    plt.xlabel("Y coordinates")
    plt.ylabel("X coordinates")

    plt.imshow(img,cmap='PRGn',vmin=0,vmax=255)
    plt.colorbar()
    plt.savefig('outputs/NDVI.png',format="png")
    plt.show()
    
    #ndwi
    ndwi=create_ndwi(nir_band=nir,swir_band=swir)
    # masked image
    img=water_mask_ndwi(ndwi_band=ndwi,nir_band=nir)
    plt.title("NDWI Map of Landsat 8 Satellite Imagery")
    plt.xlabel("Y coordinates")
    plt.ylabel("X coordinates")
    
    plt.imshow(img,cmap='PRGn',vmin=0,vmax=255)
    plt.colorbar()
    plt.savefig('outputs/NDWI.png',format="png")
    plt.show()
    
