
import subprocess

def get_connected_devices():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
        devices = []
        for line in result.stdout.strip().split('\n')[1:]:
            if '\t' in line:
                devices.append(line.split('\t')[0])
        return devices
    except FileNotFoundError:
        print("ADB is not installed or not in your PATH.")
        return []
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running ADB: {e}")
        return []

import os
import datetime

def take_screenshot(device_id):
    try:
        # Create the directory if it doesn't exist
        folder_name = "newest update"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Set the filename
        filename = "screenshot.png"
        device_path = f"/sdcard/{filename}"
        local_path = os.path.join(folder_name, filename)

        # Take screenshot on the device
        subprocess.run(['adb', '-s', device_id, 'shell', 'screencap', device_path], check=True)
        print(f"Screenshot taken on {device_id}")

        # Pull the screenshot from the device
        subprocess.run(['adb', '-s', device_id, 'pull', device_path, local_path], check=True)
        print(f"Screenshot saved to {local_path}")

        # Remove the screenshot from the device
        subprocess.run(['adb', '-s', device_id, 'shell', 'rm', device_path], check=True)
        print(f"Screenshot removed from {device_id}")

    except FileNotFoundError:
        print("ADB is not installed or not in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running ADB: {e}")

if __name__ == "__main__":
    connected_devices = get_connected_devices()
    if connected_devices:
        print("Connected devices:")
        for device in connected_devices:
            print(device)
        
        # Take a screenshot on the first connected device
        take_screenshot(connected_devices[0])
    else:
        print("No devices found.")
