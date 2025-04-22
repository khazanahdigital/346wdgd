#!/bin/bash

# Create images directory if it doesn't exist
mkdir -p images

# Download hero image
curl -o images/hero-bg.jpg "https://images.unsplash.com/photo-1597007030739-6d2e7172ee0e?q=80&w=2070&auto=format&fit=crop"

# Download gallery images
curl -o images/gallery-1.jpg "https://images.unsplash.com/photo-1562141961-b5d1dfb57290?q=80&w=1974&auto=format&fit=crop"
curl -o images/gallery-2.jpg "https://images.unsplash.com/photo-1580273916550-e323be2ae537?q=80&w=1934&auto=format&fit=crop"
curl -o images/gallery-3.jpg "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?q=80&w=2070&auto=format&fit=crop"
curl -o images/gallery-4.jpg "https://images.unsplash.com/photo-1617886322168-72b886573c5a?q=80&w=1974&auto=format&fit=crop"
curl -o images/gallery-5.jpg "https://images.unsplash.com/photo-1596541223130-5d31a73fb6c6?q=80&w=2070&auto=format&fit=crop"
curl -o images/gallery-6.jpg "https://images.unsplash.com/photo-1602254872596-aa3fccc45d2e?q=80&w=2070&auto=format&fit=crop"

# Download about section image
curl -o images/shop-interior.jpg "https://images.unsplash.com/photo-1625047509248-ec889cbff17f?q=80&w=2070&auto=format&fit=crop"

echo "All images downloaded successfully!"
