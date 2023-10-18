import pyautogui

def get_color_under_mouse():
    while True:
        x, y = pyautogui.position()  # Get mouse pointer's current position
        screenshot = pyautogui.screenshot()  # Take a screenshot
        color = screenshot.getpixel((x, y))  # Get pixel color at mouse pointer's position
        print(f"Color at mouse pointer: {color}")
    return color
if __name__ == '__main__':
    color = get_color_under_mouse()

