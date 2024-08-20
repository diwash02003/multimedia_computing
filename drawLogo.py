from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
width, height = 600, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

try:
    # Try to use a system font if available
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    # If the system font is not available, use the default Pillow font
    font = ImageFont.load_default()

# Define colors
black = "black"
blue = (0, 122, 204)
red = (255, 0, 0)

# Draw shapes (e.g., a circle, triangle, and rectangle)
draw.ellipse((50, 50, 200, 200), outline=black, width=5)
draw.polygon([(300, 50), (450, 50), (375, 250)], outline=blue, fill=blue)
draw.rectangle((100, 250, 400, 300), outline=red, fill=red, width=5)

# Add text
text = "multimedia\nComputing"

# Calculate text size using font.getsize_multiline
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2

# Draw text in the center of the image
draw.text((text_x, text_y), text, fill=black, font=font, align="center")

# Save the image
image.save("multimedia_computing_logo.png")

# Display the image
image.show()
