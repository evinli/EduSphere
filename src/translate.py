import googletrans
import json
from googletrans import Translator

translator = Translator()

def get_translation(word, src, dest):
    if (word is None or src is None or dest is None):
        return "Invalid input"
    return translator.translate(word, src=googletrans.LANGCODES[src], dest=googletrans.LANGCODES[dest]).text

def get_all_languages():
    return json.dumps(list(googletrans.LANGCODES.keys()))
