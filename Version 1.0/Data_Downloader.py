# Name:                                             Renacin Matadeen
# Student Number:                                         N/A
# Date:                                               03/29/2018
# Course:                                                 N/A
# Title                             LiDAR Data Visualization - Part 1 - Download Data
#
#
#
#
#
# ----------------------------------------------------------------------------------------------------------------------

from selenium import webdriver
import pandas as pd
import time

# ----------------------------------------------------------------------------------------------------------------------

"""

Python Version: 3.6.3

Purpose:
    Using Selenium, this program will download a list of LAZ, compressed LiDAR files to a specific location
    
"""
# ----------------------------------------------------------------------------------------------------------------------

# Import Tile Index
tile_index = pd.read_csv("PATH")
tiles = tile_index['LIDAR_Tiles'].tolist()

# Instantiate Location Of WebDriver Options
path1 = "CRX 1"
path2 = "CRX 2"

# Instantiate WebDriver With Options
chromedriver = "CHROMEDRIVER"
chrome_options = webdriver.ChromeOptions()

prefs = {"download.default_directory": "DIRECTORY"}
chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_extension(path1)
chrome_options.add_extension(path2)
chrome = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)

# Link Address To Use, Data Will Always Be Of 2015
link_add = "http://depot.ville.montreal.qc.ca/geomatique/lidar_aerien/2015/"

# Loop Through Each Observation & Download The LAZ Files
for tile in tiles:
    try:
        chrome.get(link_add + str(tile) + "_2015.laz")
        time.sleep(1)

    except:
        print("Error: " + str(tile))

time.sleep(60)



