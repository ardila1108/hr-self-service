import locale
from num2words import num2words
from datetime import datetime


def format_id_number(id_number):
    if isinstance(id_number, str):
        id_number = int(id_number)
    return "{:,}".format(id_number).replace(",", ".")


def get_date_in_spanish_text_format(date, date_format="(%d) del mes de %B de %Y"):
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    day = date.day
    if day == 1:
        day_string = num2words(day, ordinal=True, lang="es")
    else:
        day_string = num2words(day, ordinal=False, lang="es")
    full_date_string = date.strftime(date_format)
    return day_string + " " + full_date_string


def number_to_money_str(amount):
    if isinstance(amount, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    day = date.day
    if day == 1:
        day_string = num2words(day, ordinal=True, lang="es")
    else:
        day_string = num2words(day, ordinal=False, lang="es")
    full_date_string = date.strftime("(%d) del mes de %B de %Y")
    return day_string + " " + full_date_string
