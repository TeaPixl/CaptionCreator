# ********************---THE PROGRAM---********************

import speech_recognition as sr
import progressbar
import time
import os

# greeting into the program
print("**********Caption Creator**********\n")
print("This only works for .wav, .mp3, .mp4, and .mkv file formats")
print("Place your file in the folder labeled Audio before you start")
answer = input("Would you like to start the Creator? (y/n): ")
if answer == "y":
    pass
else:
    print("Goodbye!")
    time.sleep(2)
    exit()

# check for caption files that are already there and if so, delete them
try:
    os.remove('Captions\\Captions.txt')
except FileNotFoundError:
    print("No captions to remove...")
    pass

# animated progressbar
def animated_progressbar():
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
        
recognise = sr.Recognizer()

# accesses the file
try:
    import mp3_converter
    import mp4_converter
    import mkv_converter
    audio_file = sr.AudioFile("Audio\\audio.wav")  # tries to access a .wav file
except Exception:
    print("Error was caught, check for unsupported file types or if there is no file") # any extra errors caught
    time.sleep(5)
finally: 
    
    # records the speech in the file
    with audio_file as source:
        recognise.adjust_for_ambient_noise(source)
        print("Adjusted recording for background noise cancellation...")
        # shows an animated progress bar
        animated_progressbar()
        # records and sends speech to API
        audio = recognise.record(source)
        # I am using the Sphinx API, feel free to change this if you would like
        finished_audio = recognise.recognize_google(audio)
        # begins to write captions to a file
        # shows an animated progress bar
        animated_progressbar()
        with open('Captions\\Captions.txt', "w") as f:
            print("Writing to a file...")
            f.write("***CAPTIONS***\n\n")
            f.write(finished_audio.capitalize())
            f.write("\n\n")
            f.write("-Credits go to Teapixl, Thx :D") # credits (of course :/)
            f.close
            
os.remove("Audio\\audio.wav") # removes the original file
print("Removing audio.wav...")
print("Done.")
print("Text file has finished processing")
print("Check the Captions folder")
time.sleep(10) # extra time to show the finished text
exit()
