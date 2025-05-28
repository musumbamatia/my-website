from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon(size, output_path):
    # Create a new image with a transparent background
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw a circle
    circle_color = (212, 175, 55)  # Gold color
    circle_radius = size * 0.4
    circle_center = size / 2
    draw.ellipse(
        [
            circle_center - circle_radius,
            circle_center - circle_radius,
            circle_center + circle_radius,
            circle_center + circle_radius
        ],
        fill=circle_color
    )
    
    # Draw the letter "G"
    try:
        font_size = int(size * 0.5)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "G"
    text_color = (255, 255, 255)  # White color
    
    # Get text size and position it in the center
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_position = (
        (size - text_width) / 2,
        (size - text_height) / 2
    )
    
    draw.text(text_position, text, font=font, fill=text_color)
    
    # Save the image
    image.save(output_path, 'PNG')

def create_favicon_set():
    # Create favicon directory if it doesn't exist
    if not os.path.exists('favicon'):
        os.makedirs('favicon')
    
    # Generate different sizes
    sizes = {
        'favicon-16x16.png': 16,
        'favicon-32x32.png': 32,
        'apple-touch-icon.png': 180
    }
    
    for filename, size in sizes.items():
        create_favicon(size, os.path.join('favicon', filename))
    
    # Create site.webmanifest
    manifest_content = '''{
    "name": "Gourmet Haven",
    "short_name": "Gourmet Haven",
    "icons": [
        {
            "src": "/favicon/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/favicon/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "theme_color": "#d4af37",
    "background_color": "#ffffff",
    "display": "standalone"
}'''
    
    with open(os.path.join('favicon', 'site.webmanifest'), 'w') as f:
        f.write(manifest_content)
    
    print("Favicon set generated successfully!")

if __name__ == '__main__':
    create_favicon_set() 