from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import Karen_commands
import listen
import pyttsx3
import random
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой
import assistant


if __name__ == '__main__':
    while True:
        voice_input = listen.record()
        print(voice_input)
        
        if voice_input and voice_input != ' ':
            voice_input = voice_input.split()
            if voice_input[0] in ['карен', 'карин', 'карина', 'коран', 'karen', 'карэн', 'картун', 'каран', 'карен']:
                Karen_commands.play_voice_assistant_speech('Я вас слушаю')
                command = listen.record().split()
                print(command)
                if len(command)<=1:
                    assistant.execute_command(command[0])
                elif len(command)>1:
                    assistant.execute_command(command[0], command[1:])