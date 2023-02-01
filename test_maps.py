import folium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
m = folium.Map(location = [36.9741, -122.0308],zoom_start=11,tiles = 'OpenStreetMap')
m.save('/Users/sasankgamini/Desktop/GDSCProject/newTest.html')

mapurl = "file:///Users/sasankgamini/Desktop/GDSCProject/newTest.html" #You have to give full path to your HTML file
driver = webdriver.Chrome(options=Options())
driver.get(mapurl)
time.sleep(3)
driver.save_screenshot("output.png")
driver.quit()






