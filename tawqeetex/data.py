import sys
import json
import requests
from .utils import *
from .latex import gen_pdf

class Tawqeetex:

    fajr, sunrise, dhuhr, asr, maghrib, isha = [], [], [], [], [], []
    prayers = [fajr, sunrise, dhuhr, asr, maghrib, isha]
    date_gr, months = {}, {}
    hi_day, hi_weekday = [], []

    def __init__(self, city, country, month, year, method, lang, adj):

        self.city = city # city.title()
        self.country = country
        self.month = month
        self.year = year
        self.method = method
        self.lang = lang
        self.adj = adj

        url = 'http://api.aladhan.com/v1/calendarByCity?city=' + self.city + \
            '&country=' + self.country + \
            '&method=' + self.method + \
            '&month=' + self.month + \
            '&year=' + self.year + \
            '&adjustment=' + self.adj

        response = requests.get(url)

        if response.status_code != 200:
            print(url)
            sys.exit("Error: Couldn't get from url")

        data = response.json()

        str_pr = ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
        self.months['gr'] = data['data'][0]['date']['gregorian']['month']['en']
        self.months['hi'] = data['data'][0]['date']['hijri']['month']['ar']

        for i in data['data']:
            self.date_gr[i['date']['gregorian']['day']] = i['date']['gregorian']['weekday']['en']
            self.hi_day.append(i['date']['hijri']['day'])
            self.hi_weekday.append(i['date']['hijri']['weekday']['ar'])

            for j in range(0, len(self.prayers)):
                self.prayers[j].append(i['timings'][str_pr[j]].split(' ')[0])

    def create_schedule(self):

        gen_pdf(self)
