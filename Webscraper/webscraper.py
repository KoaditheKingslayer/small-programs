import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
import io

# Function to Scrape Images from a Website
def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            if not src.startswith('http'):
                src = url + src
            images.append(src)
    return images 

# Function to Create a Thumbnail from an Image URL
def makeThumb(image_url):
    try:
        response = requests.get(image_url)
        img = Image.open(io.BytesIO(response.content))
        img.thumbnail((100, 100))
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error creating thumbnail for {image_url}: {e}")
        return None

# Function to handle a Thumbnail Click 
def on_thumbnail_click(image_url):
    def open_prompt():
        prompt = tk.Toplevel(root)
        prompt.title("Image Options")
        
        view_button = ttk.Button(prompt, text="View File", command=lambda: view_image(image_url))
        view_button.pack(pady=5)
        
        save_button = ttk.Button(prompt, text="Save File", command=lambda: save_image(image_url))
        save_button.pack(pady=5)
        
    return open_prompt

# Function to view the Image
def view_image(image_url):
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))
    image.show()

# Function to save the Image
def save_image(image_url):
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
    if file_path:
        response = requests.get(image_url)
        with open(file_path, 'wb') as file:
            file.write(response.content)

# Core Program

# Get URL to scrape images from.
url = 'https://www.petsmart.com/' # Replace with target URL

# Scrape Images
image_urls = scrape(url)

# Create the Main (root) Window using Tkinter
root = tk.Tk()
root.title('Image Scraper')
root.geometry('800x600')  # Set a fixed size for the window

# Create a Frame to hold the Thumbnails
frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

# Display Thumbnails in a grid
row, col = 0, 0
for image_url in image_urls:
    thumbnail = makeThumb(image_url)
    if thumbnail:
        label = ttk.Label(frame, image=thumbnail)
        label.image = thumbnail  # Keep a reference to avoid garbage collection
        label.grid(row=row, column=col, padx=5, pady=5)
        label.bind('<Button-1>', lambda e, url=image_url: on_thumbnail_click(url)())
        
        col += 1
        if col == 5:  # Change the number of columns as needed
            col = 0
            row += 1

# Run the Application
root.mainloop()