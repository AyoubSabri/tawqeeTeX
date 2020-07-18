import sys
import json
import requests
from utils import *
from pylatex.utils import NoEscape, bold

fajr, sunrise, dhuhr, asr, maghrib, isha = [], [], [], [], [], []
prayers = [fajr, sunrise, dhuhr, asr, maghrib, isha]
date_gr, months = {}, {}
hi_day, hi_weekday = [], []
city, country, month, year, method, lang, adj = None, None, None, None, None, None, None


def init_data(arg_city, arg_country, arg_month, arg_year, arg_method, arg_lang, arg_adj):

    global city, country, month, year, method, lang, adj

    city = arg_city
    country = arg_country
    month = arg_month
    year = arg_year
    method = arg_method
    lang = arg_lang
    adj = arg_adj

    url = 'http://api.aladhan.com/v1/calendarByCity?city=' + city + \
                        '&country=' + country + '&method=' + method + \
                        '&month=' + month + '&year=' + year + '&adjustment=' + adj

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

    return dict_month[lang][int(month) - 1]


def get_title_str():

    return dict_title[lang] + get_month_str() + ' ' + year


def get_weekday_str(weekday):

    index = dict_weekday['en'].index(weekday)

    if index == dict_weekday['en'].index('Friday'):
        return bold(dict_weekday[lang][index])
    else:
        return dict_weekday[lang][index]


def get_prayers_str():

    res = []

    for p in prayer_list:
        res.append(NoEscape(r'\AR{' + p + '}'))

    return res
