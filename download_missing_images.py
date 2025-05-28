import os
import requests
from PIL import Image
from io import BytesIO

def download_and_optimize_image(url, filename, size=(800, 600)):
    try:
        # Download image
        response = requests.get(url)
        response.raise_for_status()
        
        # Open and optimize image
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        img = img.resize(size, Image.Resampling.LANCZOS)
        
        # Save optimized image
        img.save(f'images/{filename}', 'JPEG', quality=85, optimize=True)
        print(f'Successfully downloaded and optimized {filename}')
    except Exception as e:
        print(f'Error downloading {filename}: {str(e)}')

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Download missing images
images_to_download = {
    'award.jpg': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
    'ingredients.jpg': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80',
    'dining.jpg': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80'
}

for filename, url in images_to_download.items():
    download_and_optimize_image(url, filename) 