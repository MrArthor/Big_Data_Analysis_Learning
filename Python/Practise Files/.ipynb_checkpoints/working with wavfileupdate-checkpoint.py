from scipy.io import wavfile
from pydub import AudioSegment 
from pydub.playback import play 
import matplotlib.pyplot as plt

# load the wav file
sample_rate, data =wavfile.read("E:/data/sunil.wav")
# find the sample rate
print("The sample rate is" +str(sample_rate) + "per seconds")
# find the total length of the file
print("There is the length of file is", str(len(data)) + "seconds")
# find the end point of the wav file
print("Audio end point", str(len(data)/sample_rate))
print(data) 
#Find Maximum amplitude 
print(data.max())
# plot the frequency for the data
plt.plot(data)
plt.show()
# play the wave file
import simpleaudio as sa
wav_obj = sa.WaveObject.from_wave_file("E:/data/sunil.wav")
ply_obj = wav_obj.play()
print("Music is start")
ply_obj.wait_done()

# merge two wave files

wav_file_1 = AudioSegment.from_file("E:/data/sunil.wav") 
play(wav_file_1)
wav_file_2 = AudioSegment.from_file("E:/data/sunil1.wav")
play(wav_file_2)

# Merging the two audio files 
wav_file_3 = wav_file_1 + wav_file_2
# play the sound 
play(wav_file_3)


# increasing the volume of the audio file in decibles
louder_wav_file = wav_file_1 + 30
play(louder_wav_file)
 
# Export louder audio file 
louder_wav_file.export(out_f = "louder_wav_file.wav",format = "wav")

# Decreasing the volume of the audio file in decibles
louder_wav_file = wav_file_1 - 15
play(louder_wav_file)
 
# Export louder audio file 
louder_wav_file.export(out_f = "louder_wav_file.wav",format = "wav")

#spiliting the file
b = wav_file_1.split_to_mono() 
print(b) 
print(b[0].channels )
b[0].export(out_f="new.wav",format="wav")
