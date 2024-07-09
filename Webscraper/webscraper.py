# TODO 
# Create the Web Scraper (using requests and beautifulsoup4)
    # Scrape a webpage for images using requests and beautifulsoup4
# Create the GUI using Tkinter, and handle image processing using PIL
    # Use Tkinter to create a GUI for displaying thumbnails
    # Use PIL to handle image processing.
# Integrate the Scraper and GUI
    # Display the scraped images in a grid layout.
    # Implement click functionality for the images (to view or save)

### Imports ###

import tkinter as tk # Tkinter
from tkinter import tkk, filedialog 
from PIL import Image, ImageTk # Python Image Library
import requests # HTTP
from bs4 import BeautifulSoup
import io

### Functions ###

# Function to Scrape Images from a Website
def scrape(url):
    response = requests.get(url) # Uses the passed URL to obtain an HTTP request.
    soup = BeautifulSoup(response.content, 'html.parser') # Parses the content of the response as HTML.
    images = [] # List to contain the image source URLs.
    for img in soup.find_all('img'): # Search for all img tags in the document.
        src = img.get('src') # get the Source URL for the image
        if src: # If a source is returned...
            if not src.startswith('http'): # And If the source doesn't start with http
                src = url + src 
            images.append(src)
    return images

 

# Function to Create a Thumbnail from an Image URL

# Function to handle a Thumbnail Click 

# Function to view the Image

# Function to save the Image

### Core Program ###

# Get URL to scrape images from.

# Scrape Images

# Create the Main (root) Window using Tkinter

# Create a Frame to hold the Thumbnails

# Display Thumbnails in a grid

# Run the Application
