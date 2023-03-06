''' Програма призначена для пошуку помилок у звіті змагань по радіоспорту. Програма за допомогою регулярних виразів
вибирає із звіту спрацьовані позивні і порівнює їх із позивними, звіти яких вже завантежені на сайті організатора змагань.
Для цього використовується технологія парсінгу. У випадку, якщо спрацьованого позивного програма не знаходить у вже
поданих звітах, такі позивні будуть позначені жовтим і надається посилання для перевірки чи такий кличний взагалі існує.
Якщо такий позивний не існує, слід перевірити його на прсутність помилки.'''

import re
from bs4 import BeautifulSoup
from django.db import models
import requests

class Parser(models.Model):
    url = models.CharField(max_length=100, null=True, blank=True, verbose_name="Посилання на надіслані логи")
    log_file = models.FileField(upload_to='core/files/%Y/%m/%d/', blank=True)

    def parsing(self):
        self.f = open(r"core/files/2022/11/01/US5WBJ.log", "r")
        self.call_sign_list = []
        for self.x in self.f:
            pattern = r'\d?[A-Z]?[A-Z]+\d\d?[A-Z][A-Z]?[A-Z]?[A-Z]?'
            self.call_sign = re.findall(pattern, self.x)
            self.c = [self.c for self.c in self.call_sign if self.c != 'US5WBJ']
            self.call_sign_list.append(self.c)
            self.filtered_list = [self.n for self.n in self.call_sign_list if self.n != [] and self.n != ['N1MM']]
            self.k = [self.k[0] for self.k in self.filtered_list]
        self.p = requests.get(self.url)
        self.soup = BeautifulSoup(self.p.text, 'html.parser')
        self.tbody = self.soup.tbody
        self.trs = self.tbody.contents
        self.ww_list = []
        for self.tr in self.trs:
            if self.tr.find('td') != -1:
                self.ww_list.append(self.tr.find('td').string)
        self.result = {}
        k = 0
        for self.h in self.filtered_list:
            k += 1
            n = 200
            if self.h[0] not in self.ww_list:
                # self.url_call = 'https://www.qrz.com/db/'+ self.h[0]
                # self.url_pars = requests.get(self.url_call)
                # self.soup = BeautifulSoup(self.url_pars.text, 'html.parser')
                # self.soup = self.soup.find_all(string=' produced no results.')
                if k > n:
                    break
                if self.soup != []:
                    self.result[self.h[0]] = '1'
                    if k > n:
                        break
                else:
                    self.result[self.h[0]] = '0'
                    if k > n:
                        break
            else:
                self.result[self.h[0]] = '2'
                if k > n:
                    break
        return self.result
