import ee 
from ee_plugin import Map

mean_0_20 =
'<RasterSymbolizer>' + \
 '<ColorMap type="ramp">' + \
  '<ColorMapEntry color="#0D0887" label="0-32.1" opacity="1" quantity="35"/>' + \
  '<ColorMapEntry color="#350498" label="32.1-43.7" opacity="1" quantity="38"/>' + \
  '<ColorMapEntry color="#5402A3" label="43.7-48.4" opacity="1" quantity="39"/>' + \
  '<ColorMapEntry color="#7000A8" label="48.4-53.6" opacity="1" quantity="40"/>' + \
  '<ColorMapEntry color="#8B0AA5" label="53.6-59.3" opacity="1" quantity="41"/>' + \
  '<ColorMapEntry color="#A31E9A" label="59.3-65.7" opacity="1" quantity="42"/>' + \
  '<ColorMapEntry color="#B93289" label="65.7-72.7" opacity="1" quantity="43"/>' + \
  '<ColorMapEntry color="#CC4678" label="72.7-89" opacity="1" quantity="45"/>' + \
  '<ColorMapEntry color="#DB5C68" label="89-98.5" opacity="1" quantity="46"/>' + \
  '<ColorMapEntry color="#E97158" label="98.5-108.9" opacity="1" quantity="47"/>' + \
  '<ColorMapEntry color="#F48849" label="108.9-120.5" opacity="1" quantity="48"/>' + \
  '<ColorMapEntry color="#FBA139" label="120.5-133.3" opacity="1" quantity="49"/>' + \
  '<ColorMapEntry color="#FEBC2A" label="133.3-163" opacity="1" quantity="51"/>' + \
  '<ColorMapEntry color="#FADA24" label="163-199.3" opacity="1" quantity="53"/>' + \
  '<ColorMapEntry color="#F0F921" label="163-1200" opacity="1" quantity="55"/>' + \
 '</ColorMap>' + \
 '<ContrastEnhancement/>' + \
'</RasterSymbolizer>'

mean_20_50 =
'<RasterSymbolizer>' + \
 '<ColorMap type="ramp">' + \
  '<ColorMapEntry color="#0D0887" label="0-32.1" opacity="1" quantity="35"/>' + \
  '<ColorMapEntry color="#350498" label="32.1-43.7" opacity="1" quantity="38"/>' + \
  '<ColorMapEntry color="#5402A3" label="43.7-48.4" opacity="1" quantity="39"/>' + \
  '<ColorMapEntry color="#7000A8" label="48.4-53.6" opacity="1" quantity="40"/>' + \
  '<ColorMapEntry color="#8B0AA5" label="53.6-59.3" opacity="1" quantity="41"/>' + \
  '<ColorMapEntry color="#A31E9A" label="59.3-65.7" opacity="1" quantity="42"/>' + \
  '<ColorMapEntry color="#B93289" label="65.7-72.7" opacity="1" quantity="43"/>' + \
  '<ColorMapEntry color="#CC4678" label="72.7-89" opacity="1" quantity="45"/>' + \
  '<ColorMapEntry color="#DB5C68" label="89-98.5" opacity="1" quantity="46"/>' + \
  '<ColorMapEntry color="#E97158" label="98.5-108.9" opacity="1" quantity="47"/>' + \
  '<ColorMapEntry color="#F48849" label="108.9-120.5" opacity="1" quantity="48"/>' + \
  '<ColorMapEntry color="#FBA139" label="120.5-133.3" opacity="1" quantity="49"/>' + \
  '<ColorMapEntry color="#FEBC2A" label="133.3-163" opacity="1" quantity="51"/>' + \
  '<ColorMapEntry color="#FADA24" label="163-199.3" opacity="1" quantity="53"/>' + \
  '<ColorMapEntry color="#F0F921" label="163-1200" opacity="1" quantity="55"/>' + \
 '</ColorMap>' + \
 '<ContrastEnhancement/>' + \
'</RasterSymbolizer>'

stdev_0_20 =
'<RasterSymbolizer>' + \
 '<ColorMap type="ramp">' + \
  '<ColorMapEntry color="#fde725" label="low" opacity="1" quantity="1"/>' + \
  '<ColorMapEntry color="#5dc962" label=" " opacity="1" quantity="2"/>' + \
  '<ColorMapEntry color="#20908d" label=" " opacity="1" quantity="3"/>' + \
  '<ColorMapEntry color="#3a528b" label=" " opacity="1" quantity="4"/>' + \
  '<ColorMapEntry color="#440154" label="high" opacity="1" quantity="5"/>' + \
 '</ColorMap>' + \
 '<ContrastEnhancement/>' + \
'</RasterSymbolizer>'

stdev_20_50 =
'<RasterSymbolizer>' + \
 '<ColorMap type="ramp">' + \
  '<ColorMapEntry color="#fde725" label="low" opacity="1" quantity="1"/>' + \
  '<ColorMapEntry color="#5dc962" label=" " opacity="1" quantity="2"/>' + \
  '<ColorMapEntry color="#20908d" label=" " opacity="1" quantity="3"/>' + \
  '<ColorMapEntry color="#3a528b" label=" " opacity="1" quantity="4"/>' + \
  '<ColorMapEntry color="#440154" label="high" opacity="1" quantity="5"/>' + \
 '</ColorMap>' + \
 '<ContrastEnhancement/>' + \
'</RasterSymbolizer>'

raw = ee.Image("ISDASOIL/Africa/v1/potassium_extractable")
Map.addLayer(
    raw.select(0).sldStyle(mean_0_20), {},
    "Potassium extractable, mean visualization, 0-20 cm")
Map.addLayer(
    raw.select(1).sldStyle(mean_20_50), {},
    "Potassium extractable, mean visualization, 20-50 cm")
Map.addLayer(
    raw.select(2).sldStyle(stdev_0_20), {},
    "Potassium extractable, stdev visualization, 0-20 cm")
Map.addLayer(
    raw.select(3).sldStyle(stdev_20_50), {},
    "Potassium extractable, stdev visualization, 20-50 cm")

converted = raw.divide(10).exp().subtract(1)

visualization = {'min': 0, 'max': 250}

Map.setCenter(25, -3, 2)

Map.addLayer(converted.select(0), visualization, "Potassium extractable, mean, 0-20 cm")


Export.image.toDrive({
  'image' : raw.select(2),
  'description': 'mean_postassium',
  'maxPixels': 3784216672400
})
Map