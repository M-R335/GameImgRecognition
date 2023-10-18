import pyautogui
import keyboard
import random
import time

# Define the region's coordinates
top_left = (160, 153)
bottom_right = (2403, 1258)

TOO_DARK_THRESHOLD = 44
TOO_LIGHT_THRESHOLD = 35
SAMPLE_SIZE = 5000


def is_shift_pressed():
    return keyboard.is_pressed('shift')


def to_grayscale(rgb):
    return 0.2989 * rgb[0] + 0.5870 * rgb[1] + 0.1140 * rgb[2]


def is_acceptable_color(color):
    # Checking if it's too dark
    if all(value < TOO_DARK_THRESHOLD for value in color):
        return False
    # Checking if it's too light (or kinda white)
    if all(value > TOO_LIGHT_THRESHOLD for value in color):
        return False
    return True



def click_within_region(top_left, bottom_right):
    count = 0

    # Capture screenshot of the specified region
    img = pyautogui.screenshot(
        region=(top_left[0], top_left[1], bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]))

    for _ in range(SAMPLE_SIZE):
        x = random.randint(0, img.width - 1)
        y = random.randint(0, img.height - 1)
        color = img.getpixel((x, y))
        if is_acceptable_color(color):
            #pyautogui.click(x + top_left[0], y + top_left[1],clicks=2)
            pyautogui.click(x + top_left[0], y + top_left[1],clicks=3)


            count += 1
            if count == 1:
                return True
    return False


def main():
    active = False
    while True:
        if is_shift_pressed() and not active:
            active = True
            print("Activated!")
            time.sleep(0.2)  # To prevent multiple toggles in quick succession
        elif is_shift_pressed() and active:
            active = False
            print("Deactivated!")
            time.sleep(0.2)

        if active:
            clicked = click_within_region(top_left, bottom_right)
            if clicked:
                print("Clicked 3 times!")


if __name__ == '__main__':
    main()
