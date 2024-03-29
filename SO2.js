/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var image = ee.Image("users/PichayaMelody123/wiosymmarin"),
    wiosym_roi = 
    /* color: #d63000 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[7.584759468943162, 16.2784294007598],
          [7.584759468943162, -40.46329452343532],
          [78.60038446894316, -40.46329452343532],
          [78.60038446894316, 16.2784294007598]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/

var roi= ee.FeatureCollection(wiosym_roi).geometry();
var collection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_SO2')
  .select('SO2_column_number_density')
  .filterDate('2021-01-01', '2021-12-01');
 

var wiosym = ee.Image ('users/PichayaMelody123/wiosymmarin');


print(collection);

var band_viz = {
  min: 0,
  max: 0.0002,
  palette: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
};
Map.addLayer(wiosym);
Map.addLayer(collection.mean().clip(roi), band_viz, 'S5P S02');

Export.image.toDrive({
  image : collection.mean().clip(roi),
  description: 'SO2_wio21',
  maxPixels: 3784216672400,
  region : roi});