/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var AOI = 
    /* color: #d63000 */
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
        [[[[3.106980421385961, 23.022987400889438],
           [3.106980421385961, -51.76520991741075],
           [81.15385542138596, -51.76520991741075],
           [81.15385542138596, 23.022987400889438]]],
         [[[18.57573042138596, 36.97133334830778],
           [18.57573042138596, 36.97133334830778],
           [18.57573042138596, 36.97133334830778],
           [18.57573042138596, 36.97133334830778]]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var imgVV = ee.ImageCollection('COPERNICUS/S1_GRD')
        .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
        .filter(ee.Filter.eq('instrumentMode', 'IW'))
        .select('VV')
        .map(function(image) {
          var edge = image.lt(-30.0);
          var maskedImage = image.mask().and(edge.not());
          return image.updateMask(maskedImage);
        });

var desc = imgVV.filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'));
var asc = imgVV.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'));

var spring = ee.Filter.date('2015-03-01', '2020-04-20');
var lateSpring = ee.Filter.date('2015-04-21', '2020-06-10');
var summer = ee.Filter.date('2015-06-11', '2020-08-31');

var descChange = ee.Image.cat(
        desc.filter(spring).mean(),
        desc.filter(lateSpring).mean(),
        desc.filter(summer).mean());

var ascChange = ee.Image.cat(
        asc.filter(spring).mean(),
        asc.filter(lateSpring).mean(),
        asc.filter(summer).mean());


Map.addLayer(ascChange, {min: -25, max: 5}, 'Multi-T Mean ASC', true);
Map.addLayer(descChange, {min: -25, max: 5}, 'Multi-T Mean DESC', true);
