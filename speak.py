import speech_recognition as sr
from googletrans import Translator

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {text}")
        return text
    except sr.RequestError:
        print("Erro ao solicitar resultados do serviço de reconhecimento de fala.")
        return None
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return None

def translate_text(text, src_lang='pt', dest_lang='en'):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Dicionário de línguas
languages = {
        'africâner': 'af',
    'albanês': 'sq',
    'amárico': 'am',
    'árabe': 'ar',
    'armênio': 'hy',
    'azerbaijano': 'az',
    'basco': 'eu',
    'bengali': 'bn',
    'bielorrusso': 'be',
    'bósnio': 'bs',
    'búlgaro': 'bg',
    'catalão': 'ca',
    'cebuano': 'ceb',
    'chichewa': 'ny',
    'chinês': 'zh-cn',
    'córsico': 'co',
    'croata': 'hr',
    'tcheco': 'cs',
    'dinamarquês': 'da',
    'holandês': 'nl',
    'inglês': 'en',
    'esperanto': 'eo',
    'estoniano': 'et',
    'filipino': 'tl',
    'finlandês': 'fi',
    'francês': 'fr',
    'frísio': 'fy',
    'galês': 'cy',
    'galiciano': 'gl',
    'georgiano': 'ka',
    'alemão': 'de',
    'grego': 'el',
    'guarani': 'gn',
    'gujarati': 'gu',
    'hauçá': 'ha',
    'havaiano': 'haw',
    'hebraico': 'he',
    'hindi': 'hi',
    'hmong': 'hmn',
    'húngaro': 'hu',
    'islandês': 'is',
    'igbo': 'ig',
    'indonésio': 'id',
    'irlandês': 'ga',
    'italiano': 'it',
    'japonês': 'ja',
    'javanês': 'jw',
    'canará': 'kn',
    'cazaque': 'kk',
    'khmer': 'km',
    'coreano': 'ko',
    'curdo': 'ku',
    'quirguiz': 'ky',
    'laosiano': 'lo',
    'latim': 'la',
    'letão': 'lv',
    'lituano': 'lt',
    'luxemburguês': 'lb',
    'macedônio': 'mk',
    'malgaxe': 'mg',
    'malaio': 'ms',
    'malaiala': 'ml',
    'maltês': 'mt',
    'maori': 'mi',
    'marati': 'mr',
    'mongol': 'mn',
    'myanmar': 'my',
    'nepali': 'ne',
    'norueguês': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persa': 'fa',
    'polonês': 'pl',
    'português': 'pt',
    'punjabi': 'pa',
    'romeno': 'ro',
    'russo': 'ru',
    'samoano': 'sm',
    'gaélico escocês': 'gd',
    'sérvio': 'sr',
    'sessoto': 'st',
    'shona': 'sn',
    'sindhi': 'sd',
    'cingalês': 'si',
    'eslovaco': 'sk',
    'esloveno': 'sl',
    'somali': 'so',
    'espanhol': 'es',
    'sundanês': 'su',
    'suaíli': 'sw',
    'sueco': 'sv',
    'tájico': 'tg',
    'tâmil': 'ta',
    'telugu': 'te',
    'tailandês': 'th',
    'turco': 'tr',
    'ucraniano': 'uk',
    'urdu': 'ur',
    'uzbeque': 'uz',
    'vietnamita': 'vi',
    'xhosa': 'xh',
    'iídiche': 'yi',
    'iorubá': 'yo',
    'zulu': 'zu'
}

# Capturar e traduzir áudio
recognized_text = recognize_speech_from_mic()
if recognized_text:
    dest_lang_name = input("Digite a língua de destino (ex: 'inglês', 'espanhol', 'francês'): ").strip().lower()
    
    if dest_lang_name in languages:
        dest_lang = languages[dest_lang_name]
        translated_text = translate_text(recognized_text, dest_lang=dest_lang)
        print(f"Texto traduzido: {translated_text}")
    else:
        print("Língua de destino não suportada. Tente novamente com uma língua válida.")