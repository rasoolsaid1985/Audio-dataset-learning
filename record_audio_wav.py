import pyaudio
import wave

frames_per_buffer = 3200
format = pyaudio.paInt16
channels = 1
frame_rate = 16000
obj = pyaudio.PyAudio()
straem = obj.open(
    format=format,
    channels = channels,
    rate=frame_rate,
    input=True,
    frames_per_buffer=frames_per_buffer
)

print("Start Recording")

seconds = 5
frame = []
for i in range(0,int(frame_rate/frames_per_buffer*seconds)):
    data = straem.read(frames_per_buffer)
    frame.append(data)

straem.stop_stream()
straem.close()

obj.terminate()


obj1 = wave.open("ouput.wav", "wb")
obj1.setnchannels(channels)
obj1.setsampwidth(obj.get_sample_size(format))
obj1.setframerate(frame_rate)
obj1.writeframes(b"".join(frame))
obj1.close()