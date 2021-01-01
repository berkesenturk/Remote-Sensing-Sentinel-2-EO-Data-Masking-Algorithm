# Description

## Index Creator

Index Creator is a pilot Python repository for solving common Remote Sensing problems. In this assignment, the creation of NDVI and NDWI indices and their masking from water bodies were studied.

Main aim was creating the NDVI, NDWI indexes and masking the water bodies after. To do so, the theoretical knowledge about Near Infrared bands does not reflect from the water bodies, in order to benefit from it a condition has been defined.

However in practical, it does not work everytime because of the effects of another factors such as atmosphere, pixel values of the NIR values are not zero always. Hence, NIR band of Landsat 8 examined and a threshold value is used rather than zero.

# Installation

```git clone git@github.com:berkesenturk/index_creator.git```

## Usage 

To use the repository it needs to be installed and worked within the same directory.

```python
import utils

utils.create_ndvi(red_band=red,nir_band=nir)
utils.water_mask_ndvi(ndvi_band=ndvi,nir_band=nir)

```

## How to contribute?

Please create an issue to resolve the problem in order to quick response.