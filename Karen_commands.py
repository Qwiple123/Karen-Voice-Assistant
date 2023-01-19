import pyttsx3
import random
import listen
import weather
import Translator
import webbrowser
ttsEngine = pyttsx3.init()


def play_voice_assistant_speech(text_to_speech):
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()



def play_greetings():
    play_voice_assistant_speech(random.choice(['Приветствую', 'Здравствуй', 'Здравствуйте', 'Доброго времени суток']))

def play_farewell_and_quit():
    play_voice_assistant_speech('Досвидания')
    exit()

def solve(args):
    print(args)
    digits = {'один': '1',
        'два': '2',
        'три': '3',
        'четыре': '4',
        'пять': '5',
        'шесть': '6',
        'семь': '7',
        'восемь': '8',
        'девять': '9',
        'десять': '10',
        'умножить': '*',
        'разделить': '/',
        'плюс': '+',
        'минус': '-',
        'на': '',
    }
    play_voice_assistant_speech(eval(''.join([digits[i] for i in args])))
def search_for_video_on_youtube(*args:tuple):
    print(args)
    if not args[0]: return
    search_term = ' '.join(args[0])
    url = "https://www.youtube.com/results?search_query=" + search_term
    play_voice_assistant_speech(f'Открываю ваше видео на YouTube. Запрос {search_term}')
    webbrowser.get().open(url)

def search_for_definition_on_wikipedia(*args:tuple):
    if not args[0]: return
    search_term = ' '.join(args[0])
    url = 'https://ru.wikipedia.org/wiki/' + search_term
    play_voice_assistant_speech(f'Открываю статью на Wikipedia. Запрос {search_term}')
    webbrowser.get().open(url)

def search_for_term_on_google(*args:tuple):
    if not args[0]: return
    search_term = ' '.join(args[0])
    url = 'https://www.google.ru/search?q=' + search_term
    play_voice_assistant_speech(f'Вбиваю запрос в гугл. Запрос {search_term}')
    webbrowser.get().open(url)



def get_translation(*args:tuple):
    if not args[0]: return
    play_voice_assistant_speech(Translator.translate(' '.join(args[0])))

def get_weather_forecast():
    data = weather.get_weather()
    play_voice_assistant_speech(f'На улице {data[0]} градусов. {data[1]}')