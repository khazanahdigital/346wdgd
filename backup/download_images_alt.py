import os
import urllib.request

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# List of image URLs and their target filenames
images = [
    # Hero image - auto repair shop
    ('https://images.pexels.com/photos/3807319/pexels-photo-3807319.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'hero-bg.jpg'),
    
    # Gallery images
    ('https://images.pexels.com/photos/3806249/pexels-photo-3806249.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'gallery-1.jpg'),
    # gallery-2.jpg already downloaded
    # gallery-3.jpg already downloaded
    ('https://images.pexels.com/photos/2244746/pexels-photo-2244746.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'gallery-4.jpg'),
    # gallery-5.jpg already downloaded
    ('https://images.pexels.com/photos/1119796/pexels-photo-1119796.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'gallery-6.jpg'),
    
    # Additional images
    ('https://images.pexels.com/photos/3822843/pexels-photo-3822843.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'service-bg.jpg'),
    ('https://images.pexels.com/photos/3807171/pexels-photo-3807171.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'testimonial-bg.jpg'),
]

# Download each image
for url, filename in images:
    try:
        # Skip if file already exists
        if os.path.exists(os.path.join('images', filename)):
            print(f"{filename} already exists, skipping...")
            continue
            
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, os.path.join('images', filename))
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("Image download process completed!")
