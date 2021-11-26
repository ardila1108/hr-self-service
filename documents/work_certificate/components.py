from documents.work_certificate import utils
from datetime import datetime


def compose_body(
    document, name, id_number, id_city, start_date, position, salary=None, bonus=None
):
    body = document.body % {
        "name": name,
        "id_number": utils.format_id_number(id_number),
        "id_city": id_city,
        "start_date": utils.get_date_in_spanish_text_format(start_date),
        "position": position,
    }
    if salary is not None:
        body += document.salary_body % {"salary": salary}
    if bonus is not None:
        body += document.bonus_body % {"bonus": bonus}
    return body + "."


def compose_closure(document, addressee):
    return document.closure % {
        "current_date": utils.get_date_in_spanish_text_format(datetime.today()),
        "addressee": addressee,
    }
