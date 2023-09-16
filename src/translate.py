import googletrans
import json
from googletrans import Translator

translator = Translator()

def get_translation(word, src, dest):
    return translator.translate(word, src=googletrans.LANGCODES[src], dest=googletrans.LANGCODES[dest]).text

def get_all_languages():
    return json.dumps(list(googletrans.LANGCODES.keys()))

# print(get_translation('hi', 'english', 'french'))

# print(type(get_all_languages()))
