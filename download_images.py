import os
import requests
from PIL import Image
from io import BytesIO

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Image URLs (using high-quality, royalty-free images)
image_urls = {
    'hero-bg.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1920&q=80',
    'food1.jpg': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800&q=80',
    'food2.jpg': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800&q=80',
    'food3.jpg': 'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=800&q=80',
    'food4.jpg': 'https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=800&q=80',
    'interior1.jpg': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=80',
    'interior2.jpg': 'https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800&q=80',
    'event1.jpg': 'https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=800&q=80',
    'event2.jpg': 'https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?w=800&q=80',
    'tasting1.jpg': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80',
    'map.jpg': 'https://images.unsplash.com/photo-1524661135-423995f22d0b?w=800&q=80',
    'featured-menu.jpg': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&q=80',
    'featured-about.jpg': 'https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800&q=80',
    'featured-gallery.jpg': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=80',
    'restaurant-interior.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
    'chef1.jpg': 'https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=400&q=80',
    'chef2.jpg': 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400&q=80',
    'chef3.jpg': 'https://images.unsplash.com/photo-1581299894007-aaa50297cf16?w=400&q=80',
    'page-hero-bg.jpg': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1920&q=80',
    'offers-bg.jpg': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1920&q=80'
}

def download_and_optimize_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Open the image
            img = Image.open(BytesIO(response.content))
            
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Save the optimized image
            img.save(f'images/{filename}', 'JPEG', quality=85, optimize=True)
            print(f'Successfully downloaded and optimized {filename}')
        else:
            print(f'Failed to download {filename}')
    except Exception as e:
        print(f'Error processing {filename}: {str(e)}')

# Download and optimize all images
for filename, url in image_urls.items():
    download_and_optimize_image(url, filename)

print('All images have been downloaded and optimized!') 