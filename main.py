import wave
import array
import itertools
from canvas import Canvas
from pyglet.app import run

audio = wave.open("start.wav", "rb")
print("Channels:", audio.getnchannels())
print("Sample width:", audio.getsampwidth(), "Bytes")
print("Frequency:", audio.getframerate(), "kHz")
print("Number of frames:", audio.getnframes())
print("Audio length", audio.getnframes() / audio.getframerate(), "seconds")

samples = audio.readframes(audio.getnframes())
array_of_ints = array.array("h", samples)
normalized = [x / 65536 for x in array_of_ints]
batched_samples = list(itertools.batched(normalized, 2))

renderer = Canvas(batched_samples)
run()
