# import required libraries
from pydub import AudioSegment 
from pydub.playback import play 
from playsound import playsound
 
# Import an audio file 
# Format parameter only
# for readability 
wav_file = AudioSegment.from_mp3(file ="E:\data\sk.mp3") 
# Play the audio file
play(wav_file)

from pydub import AudioSegment
from pydub.playback import play

