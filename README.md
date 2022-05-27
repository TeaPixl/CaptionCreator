# Caption Creator

Caption creator that uses natural language processing from a speech-to-text API to process and create accurate captions.

simply drag and drop the .wav, .mp4, .mkv, or .mp3 files into the program folder as audio and it will output your caption .txt file on the desktop
This program only supports .mkv, .wav, .mp3 and .mp4 file formats.
DO NOT STOP THE PROGRAM IF IT STOPS LOADING, this is completly normal, longer audio files will take some time

YOUR ORIGINAL AUDIO OR VIDEO FILE WILL BE LOST IN THE PROCESS SO BE SURE TO HAVE A BACKUP

I am not held liable for any loss of video or audio from misuse of this software, Thanks!
Creation and Credits go to TeaPixl :)



## Documentation

There are many files in this folder that will be used.

You simply want to paste you files into the directory labeled "Audio" to convert the file, it will automatically delete the original audio file after completion
MAKE SURE TO RENAME THE FILE TO "audio"

The "speech_process.py" file is the main file used in the program and controls all other files in the directory.
The "mp3_converter.py", "mp4_converter.py" and "mkv_converter" are used to convert a mp3 or mp4 file into a wav format that is used by the speech analysis program unless the file is already in a wav format.

The "README.md" file is what you are looking at now! and contains all of the documentation for the program.
The "Captions" directory stores all of your finished captions from your audio files,
You can take these files and store them anywhere to be used, or leave them and they will automatically be deleted the next time the program boots.

The "source.py" file is the source code for this program and the brain of it, it can be used to develop your own additions
You can change the API that is used to convert speech into text with the recognise_[] function
