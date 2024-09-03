from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
import datetime
import os

from numba.core.datamodel.models import ListModel

script_dir = os.path.dirname(os.path.abspath(__file__))

def create_image_with_text(text,date, resolution=(2560, 1440), text_color=(255, 255, 255)):
    width, height = resolution

    # Create a black image
    # image = Image.new("RGB", (width, height), (0, 0, 0))
    bg_path = os.path.join(script_dir, "assets", "bg.png")
    image = Image.open(bg_path).convert('RGBA')

    draw = ImageDraw.Draw(image)

    # Load a font (you might need to adjust the font path)
    font_path = os.path.join(script_dir, "Inter-Black.otf")
    font_size = 160
    font = ImageFont.truetype(font_path, font_size)

    # Calculate text size and position
    text_width = draw.textlength(text, font=font)
    text_height = font_size
    x = 1330 #(width - text_width) // 2
    y = 132.27 # (height - text_height) // 2

    draw.text((x, y), text, font=font, fill=text_color)

    # Drawing Date
    DATE_FONT_SIZE = 45
    dateFontpath = os.path.join(script_dir, "Roboto-Medium.ttf")
    dateFont = ImageFont.truetype(dateFontpath, DATE_FONT_SIZE)
    dx = 1188.5
    dy = 325

    draw.text((dx, dy), date, font=dateFont, fill="#A8A8A8")

    # Adding Box to Active Month
    overlayImagePath = os.path.join(script_dir, "assets", "glow.png")
    overlay_image = Image.open(overlayImagePath).convert('RGBA')
    currentMonth =datetime.date.today().month

    if currentMonth == 9:
        overlayX = 1370
        overlayY = 408

    elif currentMonth == 10:
        overlayX = 2035
        overlayY = 408

    elif currentMonth == 11:
        overlayX = 704
        overlayY = 843

    elif currentMonth == 12:
        overlayX = 1370
        overlayY = 843

    elif currentMonth == 1:
        overlayX = 2036
        overlayY = 843

    else:
        overlayX = 0
        overlayY = 0

    image.paste(overlay_image, (overlayX, overlayY), overlay_image)


    return image

def CurrentTime(date, time = "100:00" ):
    image = create_image_with_text(time, resolution=(2560, 1440), date=date)
    # image.show()
    savePath = os.path.join(script_dir, "output_image.png")
    image.save(savePath)
