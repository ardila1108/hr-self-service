import locale
from num2words import num2words
from datetime import datetime


def format_id_number(id_number):
    if isinstance(id_number, str):
        id_number = int(id_number)
    return "{:,}".format(id_number).replace(",", ".")


def get_date_in_spanish_text_format(
    date, date_format="(%d) del mes de %B de %Y", language="es"
):
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    if language == "es":
        locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    day = date.day
    if day == 1:
        day_string = num2words(day, ordinal=True, lang=language)
    else:
        day_string = num2words(day, ordinal=False, lang=language)
    full_date_string = date.strftime(date_format)
    return day_string + " " + full_date_string


def number_to_money_str(amount, language="es"):
    money_str = num2words(amount, lang=language).upper()
    if language == "es":
        money_str += " DE PESOS M/CTE"
    money_str += " ($" + "{:,}".format(amount).replace(",", ".") + ")"
    return money_str
