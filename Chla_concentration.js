/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var wio = ee.Image("users/PichayaMelody123/wiosymmarin"),
    roi = 
    /* color: #98ff00 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      },
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.MultiPolygon(
        [[[[10.711103613726104, 68.50216451884634],
           [10.711103613726104, 53.34085060429263],
           [32.5958692387261, 53.34085060429263],
           [32.5958692387261, 68.50216451884634]]],
         [[[7.561812400817871, 16.2923477813746],
           [7.561812400817871, -49.1575371409465],
           [78.48954677581787, -49.1575371409465],
           [78.48954677581787, 16.2923477813746]]]], null, false),
    geometry = 
    /* color: #d63000 */
    /* shown: false */
    ee.Geometry.MultiPoint();
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var wiosym = ee.Image('users/PichayaMelody123/wiosymmarin');
Map.addLayer(wiosym);

var dataset = ee.ImageCollection("JAXA/GCOM-C/L3/OCEAN/CHLA/V1")
                .filterDate('2017-01-01', '2021-12-01')
                // filter to daytime data only
                .filter(ee.Filter.eq("SATELLITE_DIRECTION", "D"));

// Multiply with slope coefficient
var image = dataset.mean().multiply(0.0016).log10();
print(image);
var vis = {
  bands: ['CHLA_AVE'],
  min: -2,
  max: 2,
  palette: [
    '3500a8','0800ba','003fd6',
    '00aca9','77f800','ff8800',
    'b30000','920000','880000'
  ]
};

Map.addLayer(image.clip(roi), vis, "Chlorophyll-a concentration");

