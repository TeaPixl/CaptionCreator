# .mp4 to .wav file converter for the main script
import os
import subprocess
import time
from time import sleep
from tqdm import tqdm

# makes function to be used and finds path of file
def mp4_check(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

filepath = mp4_check("audio.mp4", "/")
if filepath == None: # if the file is not found, skip this
    print("No conversion files found...")
    pass
else:
    command = "ffmpeg -i Audio\\audio.mp4 -ab 160k -ac 2 -ar 44100 -vn Audio\\audio.wav" # if it is found, convert it into .wav format
    subprocess.call(command, shell=True)
    for i in tqdm(range(10)):
        sleep(0.1)
    print("File has been successfully converted...")
    os.remove("Audio\\audio.mp4") # removes the old original file
    print("Removing audio.mp4...")
    time.sleep(0.5)