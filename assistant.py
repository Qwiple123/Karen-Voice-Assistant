import Karen_commands
import pyttsx3
import random
import listen
ttsEngine = pyttsx3.init()
class VoiceAssistant:
    name = ''
    sex = ''
    speech_language = ''
    recognition_language = ''

def setup_assistant_voice():
    voices = ttsEngine.getProperty('voices')

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "female":
            # Microsoft Zira Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[2].id)
        else:
            # Microsoft David Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[2].id)
    else:
        assistant.recognition_language = "ru-RU"
        # Microsoft Irina Desktop - Russian
        ttsEngine.setProperty("voice", voices[3].id)


def execute_command(command_name: str, *args:list):
    print(command_name)
    commands = {
        ("hello", "hi", "morning", "привет"): Karen_commands.play_greetings,
        ("bye", "goodbye", "quit", "exit", "stop", "пока"): Karen_commands.play_farewell_and_quit,
        ("реши", "решить"): Karen_commands.solve,
        ("search", "google", "find", "найди"): Karen_commands.search_for_term_on_google,
        ("video", "youtube", "watch", "видео"): Karen_commands.search_for_video_on_youtube,
        ("wikipedia", "definition", "about", "определение", "википедия"): Karen_commands.search_for_definition_on_wikipedia,
        ("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): Karen_commands.get_translation,
        ("language", "язык"): 'change_language',
        ("weather", "forecast", "погода", "прогноз"): Karen_commands.get_weather_forecast,
        }

    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass



assistant = VoiceAssistant()
assistant.name = 'Karen'
assistant.sex = 'female'
assistant.speech_language = 'ru'
setup_assistant_voice()