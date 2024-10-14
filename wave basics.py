#Speecg recognition learning from FreeCodeCamp.com youtube video
#print("Heelo World")
#it is working

#Lets Start with Wave as input audio format

import wave

#Audio Signal Paramters
#1  Number of Channels  2 channels Mono from one channel Stereo from 2 channels
#2  Sample Width No of bytes for each sample
#3  frame-rate / sample_rate Frequency of sample this means that the number of samples for each sec 44,100 Hz the standard sample rate for CD quality
#4  Number of frames    
#5  Values of a frame

Obj = wave.open("voice.wav", "rb")
print("No of channels", Obj.getnchannels())
print("Sample Widht", Obj.getsampwidth())
print("Frame Rates", Obj.getframerate())
print("No of Frame", Obj.getnframes())
print("Parameter", Obj.getparams())

#to claculate audio time
#as frame rate is number of sample per second so if we devide it by framerate we will get time in second
t_audio = Obj.getnframes() / Obj.getframerate()
print("The time of audio is ", t_audio)

frames = Obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))
#the lenght is double bcz we have sample width of 2
print(print(len(frames)/2))
#print(frames)

Obj.close()
obj_new = wave.open("voice_new.wav", "wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(24414)

obj_new.writeframes(frames)
obj_new.close()