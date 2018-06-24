# encoding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, NORM


_exc = {}

_abbrev_exc = [
    # Weekdays abbreviations
    {ORTH: "пн", LEMMA: "понедельник", NORM: "понедельник"},
    {ORTH: "вт", LEMMA: "вторник", NORM: "вторник"},
    {ORTH: "ср", LEMMA: "среда", NORM: "среда"},
    {ORTH: "чт", LEMMA: "четверг", NORM: "четверг"},
    {ORTH: "чтв", LEMMA: "четверг", NORM: "четверг"},
    {ORTH: "пт", LEMMA: "пятница", NORM: "пятница"},
    {ORTH: "сб", LEMMA: "суббота", NORM: "суббота"},
    {ORTH: "сбт", LEMMA: "суббота", NORM: "суббота"},
    {ORTH: "вс", LEMMA: "воскресенье", NORM: "воскресенье"},
    {ORTH: "вскр", LEMMA: "воскресенье", NORM: "воскресенье"},
    {ORTH: "воскр", LEMMA: "воскресенье", NORM: "воскресенье"},

    # Months abbreviations
    {ORTH: "янв", LEMMA: "январь", NORM: "январь"},
    {ORTH: "фев", LEMMA: "февраль", NORM: "февраль"},
    {ORTH: "февр", LEMMA: "февраль", NORM: "февраль"},
    {ORTH: "мар", LEMMA: "март", NORM: "март"},
    # {ORTH: "март", LEMMA: "март", NORM: "март"},
    {ORTH: "мрт", LEMMA: "март", NORM: "март"},
    {ORTH: "апр", LEMMA: "апрель", NORM: "апрель"},
    # {ORTH: "май", LEMMA: "май", NORM: "май"},
    {ORTH: "июн", LEMMA: "июнь", NORM: "июнь"},
    # {ORTH: "июнь", LEMMA: "июнь", NORM: "июнь"},
    {ORTH: "июл", LEMMA: "июль", NORM: "июль"},
    # {ORTH: "июль", LEMMA: "июль", NORM: "июль"},
    {ORTH: "авг", LEMMA: "август", NORM: "август"},
    {ORTH: "сен", LEMMA: "сентябрь", NORM: "сентябрь"},
    {ORTH: "сент", LEMMA: "сентябрь", NORM: "сентябрь"},
    {ORTH: "окт", LEMMA: "октябрь", NORM: "октябрь"},
    {ORTH: "октб", LEMMA: "октябрь", NORM: "октябрь"},
    {ORTH: "ноя", LEMMA: "ноябрь", NORM: "ноябрь"},
    {ORTH: "нояб", LEMMA: "ноябрь", NORM: "ноябрь"},
    {ORTH: "нбр", LEMMA: "ноябрь", NORM: "ноябрь"},
    {ORTH: "дек", LEMMA: "декабрь", NORM: "декабрь"},

    # Date abbreviations
    {ORTH: "гг", LEMMA: "годы", NORM: "годы"},

    # Address abbreviations
    {ORTH: "респ", LEMMA: "республика", NORM: "республика"},
    {ORTH: "обл", LEMMA: "область", NORM: "область"},
    {ORTH: "ур", LEMMA: "урочище", NORM: "урочище"},
    {ORTH: "дер", LEMMA: "деревня", NORM: "деревня"},
    {ORTH: "ул", LEMMA: "улица", NORM: "улица"},
    {ORTH: "пр", LEMMA: "проспект", NORM: "проспект"},
    {ORTH: "пр-д", LEMMA: "проезд", NORM: "проезд"},
    {ORTH: "р-н", LEMMA: "район", NORM: "район"},
    {ORTH: "просп", LEMMA: "проспект", NORM: "проспект"},
    {ORTH: "пос", LEMMA: "посёлок", NORM: "посёлок"},
    {ORTH: "пер", LEMMA: "переулок", NORM: "переулок"},
    {ORTH: "наб", LEMMA: "набережная", NORM: "набережная"},
    {ORTH: "вдхр", LEMMA: "водохранилище", NORM: "водохранилище"},
    {ORTH: "кан", LEMMA: "канал", NORM: "канал"},
    {ORTH: "о-в", LEMMA: "остров", NORM: "остров"},
    {ORTH: "пл", LEMMA: "площадь", NORM: "площадь"},
    {ORTH: "ш", LEMMA: "шоссе", NORM: "шоссе"},
    {ORTH: "корп", LEMMA: "корпус", NORM: "корпус"},
    {ORTH: "кв", LEMMA: "квартира", NORM: "квартира"},
    {ORTH: "вкз", LEMMA: "вокзал", NORM: "вокзал"},
    {ORTH: "свхз", LEMMA: "совхоз", NORM: "совхоз"},
    {ORTH: "тел", LEMMA: "телефон", NORM: "телефон"},
    {ORTH: "мкр", LEMMA: "микрорайон", NORM: "микрорайон"},

    # Big numbers
    {ORTH: "тыс", LEMMA: "тысяча", NORM: "тысяча"},
    {ORTH: "млн", LEMMA: "миллион", NORM: "миллион"},
    {ORTH: "млрд", LEMMA: "миллиард", NORM: "миллиард"},
    {ORTH: "трлн", LEMMA: "триллион", NORM: "триллион"},

    # Measure units
    {ORTH: "га", LEMMA: "гектар", NORM: "гектар"},
    {ORTH: "кг", LEMMA: "килограмм", NORM: "килограмм"},
    {ORTH: "см", LEMMA: "сантиметр", NORM: "сантиметр"},
    {ORTH: "дм", LEMMA: "дециметр", NORM: "дециметр"},
    {ORTH: "мин", LEMMA: "минута", NORM: "минута"},
    {ORTH: "сек", LEMMA: "секунда", NORM: "секунда"},
    {ORTH: "гц", LEMMA: "герц", NORM: "герц"},
    {ORTH: "кгц", LEMMA: "килогерц", NORM: "килогерц"},
    {ORTH: "мгц", LEMMA: "мегагерц", NORM: "мегагерц"},
    {ORTH: "кдж", LEMMA: "килоджоуль", NORM: "килоджоуль"},
    {ORTH: "мдж", LEMMA: "мегаджоуль", NORM: "мегаджоуль"},
    {ORTH: "ккал", LEMMA: "килокалорий", NORM: "килокалорий"},
    {ORTH: "мкал", LEMMA: "мегакалорий", NORM: "мегакалорий"},
    {ORTH: "мл", LEMMA: "миллилитр", NORM: "миллилитр"},

    # Other
    {ORTH: "рис", LEMMA: "рисунок", NORM: "рисунок"},
    {ORTH: "стр", LEMMA: "страница", NORM: "страница"},
    {ORTH: "книжн", LEMMA: "книжный", NORM: "книжный"},
    {ORTH: "сокр", LEMMA: "сокращение", NORM: "сокращение"},
    {ORTH: "гжа", LEMMA: "госпожа", NORM: "госпожа"},
    {ORTH: "женск", LEMMA: "женский", NORM: "женский"},
    {ORTH: "мужск", LEMMA: "мужской", NORM: "мужской"},
    {ORTH: "средн", LEMMA: "средний", NORM: "средний"},
]


for abbrev_desc in _abbrev_exc:
    abbrev = abbrev_desc[ORTH]
    for orth in (abbrev, abbrev.capitalize(), abbrev.upper()):
        _exc[orth] = [{ORTH: orth, LEMMA: abbrev_desc[LEMMA], NORM: abbrev_desc[NORM]}]
        _exc[orth + '.'] = [{ORTH: orth + '.', LEMMA: abbrev_desc[LEMMA], NORM: abbrev_desc[NORM]}]


_slang_exc = [
    {ORTH: '2к15', LEMMA: '2015', NORM: '2015'},
    {ORTH: '2к16', LEMMA: '2016', NORM: '2016'},
    {ORTH: '2к17', LEMMA: '2017', NORM: '2017'},
    {ORTH: '2к18', LEMMA: '2018', NORM: '2018'},
    {ORTH: '2к19', LEMMA: '2019', NORM: '2019'},
    {ORTH: '2к20', LEMMA: '2020', NORM: '2020'},
]

for slang_desc in _slang_exc:
    _exc[slang_desc[ORTH]] = [slang_desc]


TOKENIZER_EXCEPTIONS = _exc
