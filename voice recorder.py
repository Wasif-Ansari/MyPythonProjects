import sounddevice
from scipy.io.wavfile import write

fs = 44100

second = int(input("Enter recording time in seconds: "))
print("Recording....")
record_voice = sounddevice.rec(int(second*fs), samplerate=fs, channels=2)
sounddevice.wait()
write("MyRec.mp3",fs,record_voice)
print("Recording done please check your folder to listen")
