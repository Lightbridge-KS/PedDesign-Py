# Run This Script from Project Root (Dev Only)
import os
import subprocess
from sys import platform
from pathlib import Path

app_name = "PedDesignCT"

print(os.getcwd()) # Project root

os.chdir("app") 

print(os.getcwd())

home_dir = str(Path.home()) # User Home Directory
print(f"Home dir: {home_dir}")

if platform == "darwin":
    print("On Mac")
    # Run on Mac
    cmd_mac_str = f"""
# ls
pyinstaller --noconfirm PedDesignCT_macos.spec
tar -czf dist/PedDesignCT_macos.tar.gz dist/PedDesignCT_macos.app
"""
    subprocess.run(cmd_mac_str, shell=True)
    # print(cmd_mac_str)
else:
    print("On Windows")
    # Run on Win
    cmd_win_str = fr"""""" 
    os.system(cmd_win_str)
    # Zip File
    os.chdir("dist") 
    os.system(f"powershell -Command Compress-Archive -Path {app_name}.exe -DestinationPath {app_name}-win.zip")
    #print(cmd_win_str)
    #subprocess.run(cmd_win_str, shell=True) # Not work
