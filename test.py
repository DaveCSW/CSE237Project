import wave
import sys
from vosk import KaldiRecognizer, Model, SetLogLevel

SetLogLevel(level=-1)

wf: wave.Wave_read = wave.open("/home/dalx/Desktop/vosktest/test.wav", "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)

model = Model(model_path="/home/dalx/Desktop/vosktest/vosk-model-small-en-us-0.15")

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
