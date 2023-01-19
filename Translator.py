from googletrans import Translator, constants
from pprint import pprint
import pyttsx3
translator = Translator()

def translate(words):
    translation = translator.translate(words)
    return translation.text

