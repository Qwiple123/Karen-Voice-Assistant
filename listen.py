import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import json
import wave
import os
import time

recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

def record(*args:tuple):
    with microphone:
        recognize_data = ''
        recognizer.adjust_for_ambient_noise(microphone)
        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)
            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())
        except speech_recognition.WaitTimeoutError:
            print('Check Microphone')
            return
    return(check_voice())
def check_voice():
    model = Model(r"models/vosk-model-small-ru-0.22")

    wf = wave.open(r'microphone-results.wav', "rb")
    rec = KaldiRecognizer(model, 44100)

    result = ''
    last_n = False

    while True:
        data = wf.readframes(44100)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())

            if res['text'] != '':
                result += f" {res['text']}"
                last_n = False
            elif not last_n:
                result += '\n'
                last_n = True

    res = json.loads(rec.FinalResult())
    result += f" {res['text']}"
    
    return result