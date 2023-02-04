import folium
#selium used to save image from web
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#import earth engine api and authenticate/initizlize
import ee
ee.Authenticate()
ee.Initialize()

#load data
dataset = ee.ImageCollection("JAXA/ALOS/PALSAR/YEARLY/FNF")\
.filterDate('2017-01-01', '2017-01-31')\
.median()

#select the forest non forest data layer
forestNonForest = dataset.select('fnf')

#create visualization
forestNonForestVis = {
    'min':1.0,
    'max':3.0,
    'palette': ['006400', 'FEFF99', '0000FF']
}

# Define a method for displaying Earth Engine image tiles to folium map.
def add_ee_layer(self, ee_image_object, vis_params, name):
  map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
  folium.raster_layers.TileLayer(
    tiles = map_id_dict['tile_fetcher'].url_format,
    attr = 'Map Data © <a href="https://earthengine.google.com/">Google Earth Engine</a>',
    name = name,
    overlay = True,
    control = True
  ).add_to(self)
 
# Add EE drawing method to folium.
folium.Map.add_ee_layer = add_ee_layer


#Create a folium map object
my_map = folium.Map(location = [-20,-60], zoom_start = 4) #(y,x) south America: -20,-60

#add the layer to the map object
my_map.add_ee_layer(forestNonForest, forestNonForestVis, 'Forest/Non-Forest')

#Add a layer contorl panel
my_map.add_child(folium.LayerControl())

#saving and displaying image
my_map.save('/Users/sasankgamini/Desktop/GDSCProject/GDSCProject/deforestationMap.html')
mapurl = "file:///Users/sasankgamini/Desktop/GDSCProject/GDSCProject/deforestationMap.html" #You have to give full path to your HTML file
driver = webdriver.Chrome(options=Options())
driver.get(mapurl)
time.sleep(3)
driver.save_screenshot("outputAfter.png")
driver.quit()
