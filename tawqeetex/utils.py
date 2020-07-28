from pylatex.utils import NoEscape, bold

NAME = 'tawqeetex'
VERSION = '1.0'

dict_month = {
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'it': ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'],
    'fr': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aôut', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
}

dict_weekday = {
    'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'it': ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica'],
    'fr': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
}

dict_lang = {
    'English': 'en',
    'Italian': 'it',
    'French': 'fr'
}

dict_title = {
    'en': 'Prayer time schedule for the month of ',
    'it': 'Orario di preghiera per il mese di ',
    'fr': 'Horaire de prière pour le mois de '
}

list_prayers = ['العشاء‎', 'المغرب‎', 'العصر‎', 'الظهر‎', 'الشروق‎', 'الفجر']

list_method = [
    "1  - Muslim World League",
    "2  - Islamic Society of North America",
    "3  - Egyptian General Authority of Survey",
    "4  - Umm Al-Qura University, Makkah",
    "5  - University of Islamic Sciences, Karachi",
    "6  - Institute of Geophysics, University of Tehran",
    "7  - Shia Ithna-Ashari, Leva Institute, Qum",
    "8  - Gulf Region",
    "9  - Kuwait",
    "10 - Qatar",
    "11 - Majlis Ugama Islam Singapura, Singapore",
    "12 - Union Organization Islamique de France",
    "13 - Diyanet İşleri Başkanlığı, Turkey",
    "14 - Spiritual Administration of Muslims of Russia",
]

list_lang = [
    "English",
    "Italian",
    "French",
]

def get_weekday_str(weekday, lang):
    index = dict_weekday['en'].index(weekday)

    if index == dict_weekday['en'].index('Friday'):
        return bold(dict_weekday[lang][index])
    else:
        return dict_weekday[lang][index]

def get_month_str(lang, month):
    return dict_month[lang][int(month) - 1]

def get_title_str(lang, month, year):
    return dict_title[lang] + get_month_str(lang, month) + ' ' + year

def get_prayers_str():
    res = []

    for p in list_prayers:
        res.append(NoEscape(r'\AR{' + p + '}'))

    return res
