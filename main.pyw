import ctypes
import os
import platform

from GenerateImage import CurrentTime
import datetime
import time

SPI_SETDESKWALLPAPER = 20

script_dir = os.path.dirname(os.path.abspath(__file__))
WALLPAPER_PATH = os.path.join(script_dir, "output_image.png")

# Define the ctypes structure for the function parameters
class ChangeWallpaperInfo(ctypes.Structure):
    _fields_ = [("dwFlags", ctypes.c_uint),
                ("pszWallpaper", ctypes.c_char_p),
                ("pszReserved", ctypes.c_char_p),
                ("fForce", ctypes.c_bool)]

def change_wallpaper(image_path):
    # Get the full path to the image
    image_path = os.path.abspath(image_path)
    print(image_path)

    system = platform.system()

    if system == "Windows":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)
    elif system == "Linux":
        try:
            import subprocess

            subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', f'file://{image_path}'])
            # subprocess.run(['qdbus', 'org.kde.plasmashell', '/PlasmaShell', 'org.kde.PlasmaShell.evaluateScript',
            #             f'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[i];d.wallpaperPlugin = "org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "file://{image_path}")}}'])
        except Exception as e:
            print(f"Failed to set wallpaper on Linux: {e}")

    elif system == "Darwin":  # macOS
        try:
            from appscript import app, mactypes

            app('Finder').desktop_picture.set(mactypes.File(image_path))
        except ImportError:
            print("appscript is not installed. Run 'pip install appscript' to enable macOS support.")
        else:
            print(f"Unsupported operating system: {system}")

def get_12_hour_time():
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%I:%M %p")
    return formatted_time


def getDateText():
    currentDate = datetime.date.today()
    formatedDate = currentDate.strftime("%d %B %Y")

    # Calculating Remaining days
    nextMonthNum = currentDate.month + 1
    if nextMonthNum > 12:
        nextMonthNum = 1

    nextYearNum = currentDate.year
    if nextMonthNum < currentDate.month:
        nextYearNum = nextYearNum + 1


    nextMonth = datetime.date(nextYearNum, nextMonthNum, 1)
    reminingDays = (nextMonth - currentDate).days
    remingStr = f"{reminingDays} Days left to Start {nextMonth.strftime('%B')}"

    return f"{formatedDate} | {remingStr}"


if __name__ == "__main__":
    while True:
        twelve_hour_time = get_12_hour_time()
        dateInfo = getDateText()

        CurrentTime(time=twelve_hour_time, date=dateInfo)
        change_wallpaper(WALLPAPER_PATH)
        time.sleep(60)




