import requests
import json
import sys
from pylatex.utils import NoEscape
from parser import get_args

fajr, sunrise, dhuhr, asr, maghrib, isha = [], [], [], [], [], []
prayers = [fajr, sunrise, dhuhr, asr, maghrib, isha]
date_gr, months = {}, {}
hi_day, hi_weekday = [], []
city, country, month, year, method, lang, adj = get_args()

url = 'http://api.aladhan.com/v1/calendarByCity?city=' + city +     \
                    '&country=' + country + '&method=' + method +   \
                    '&month=' + month + '&year=' + year + '&adjustment=' + adj


def init_data():

    response = requests.get(url)

    if response.status_code != 200:
        sys.exit("Error: Couldn't get from url")

    data = response.json()

    str_pr  = ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
    months['gr'] = data['data'][0]['date']['gregorian']['month']['en']
    months['hi'] = data['data'][0]['date']['hijri']['month']['ar']

    for i in data['data']:

        date_gr[i['date']['gregorian']['day']] = i['date']['gregorian']['weekday']['en']
        hi_day.append(i['date']['hijri']['day'])
        hi_weekday.append(i['date']['hijri']['weekday']['ar'])

        for j in range(0, len(prayers)):
            prayers[j].append(i['timings'][str_pr[j]].split(' ')[0])


def get_month_str():

    dict_month = {
        'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'it': ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'],
        'fr': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aôut', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    }

    return dict_month[lang][int(month) - 1]


def get_title_str():

    dict_title = {'en': 'Prayer time schedule for the month of ',
                  'it': 'Orario di preghiera per il mese di ',
                  'fr': 'Horaire de prière pour le mois de '}

    return dict_title[lang] + get_month_str() + ' ' + year


def get_weekday_str(weekday):

    dict_weekday = {'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    'it': ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica'],
                    'fr': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']}

    index = dict_weekday['en'].index(weekday)
    return dict_weekday[lang][index]


def get_prayers_str():

    prayer_list = ['العشاء‎', 'المغرب‎', 'العصر‎', 'الظهر‎', 'الشروق‎', 'الفجر']
    res = []

    for p in prayer_list:
        res.append(NoEscape(r'\AR{' + p + '}'))

    return res
