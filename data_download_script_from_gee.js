// In order to get region of interest from a dataset
var gaul = ee.FeatureCollection('FAO/GAUL_SIMPLIFIED_500m/2015/level2');
var roi = ee.Feature(gaul.filter(ee.Filter.eq('ADM2_NAME', 'Hopa')).first());
Map.centerObject(roi, 11);
// ------------------------------------------
    /**
 * Function to mask clouds using the Sentinel-2 QA band
 * @param {ee.Image} image Sentinel-2 image
 * @return {ee.Image} cloud masked Sentinel-2 image
 */
function maskS2clouds(image) {
  var qa = image.select('QA60');

  // Bits 10 and 11 are clouds and cirrus, respectively.
  var cloudBitMask = 1 << 10;
  var cirrusBitMask = 1 << 11;

  // Both flags should be set to zero, indicating clear conditions.
  var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
      .and(qa.bitwiseAnd(cirrusBitMask).eq(0));

  return image.updateMask(mask).divide(10000);
}
// ----------------------------------------
var sentinel_2_image_collection_2016 = ee.ImageCollection("COPERNICUS/S2")
    .filterBounds(roi.geometry())
    .filterDate('2020-01-01', '2020-12-30')
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',2))
    .map(maskS2clouds);

// ---------------------
var visualization = {
  min: 0.0,
  max: 0.3,
  bands: ['B8'],
  // bands: ['B4', 'B3', 'B2'],
};

// --------------------
var sentinel2_collection_mean_clipped = sentinel_2_image_collection_2016.median().clip(roi.geometry())
var band_nir= sentinel2_collection_mean_clipped.select('B8')
var band_swir= sentinel2_collection_mean_clipped.select('B11')
var band_red= sentinel2_collection_mean_clipped.select('B5')
//clip by asset/roi
Map.addLayer(sentinel2_collection_mean_clipped, visualization, 'RGB');

// NIR
Export.image.toDrive({
image: band_nir,
description:"Landuse_LandCover_2016",
scale: 10,
region:roi,
maxPixels:3e10,
});
// RED
Export.image.toDrive({
image: band_red,
description:"Landuse_LandCover_2016",
scale: 10,
region:roi,
maxPixels:3e10,
});

// SWIR
Export.image.toDrive({
image: band_swir,
description:"Landuse_LandCover_2016",
scale: 10,
region:roi,
maxPixels:3e10,
});
