# Description

## Index Creator

Index Creator is a pilot Python repository for solving common Remote Sensing problems. In this assignment, the creation of NDVI and NDWI indices and their masking from water bodies were studied.

Main aim was creating the NDVI, NDWI indexes and masking the water bodies after. To do so, the theoretical knowledge about Near Infrared bands does not reflect from the water bodies, in order to benefit from it a condition has been defined.

However in practical, it does not work everytime because of the effects of another factors such as atmosphere, pixel values of the NIR values are not zero always. Hence, NIR band of Landsat 8 examined and a threshold value is used rather than zero.

# Installation

In this repository following libraries are used and needs to be installed,

- matplotlib 
- skimage
- tifffile

To install the repository,

```git clone git@github.com:berkesenturk/index_creator.git```

## Usage 

To use the repository it needs to be installed and worked within the same directory.

To create an index, corresponding bands needs to be introduced. After that the create_ndvi function can be called as follows,

```python
import utils
utils.create_ndvi(red_band=red,nir_band=nir)
```

However, the output will not satisfy the user because water bodies are needed to be masked.

To mask water bodies,

```python
import utils
utils.water_mask_ndvi(ndvi_band=ndvi,nir_band=nir)
```

## How to contribute?

Please create an issue to resolve the problem in order to quick response.