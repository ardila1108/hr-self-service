from fpdf import FPDF
from pydantic import BaseModel


class WorkCertificate(FPDF):
    def __init__(self, language="spanish"):
        super().__init__()
        self.language = language


class SpanishWorkCertificate(BaseModel):
    header_text = "EL DEPARTAMENTO DE RECURSOS HUMANOS\n" "CERTIFICA"
    body = (
        "Que el señor %(name)s identificado con C.C. No %(id_number)s de "
        "%(id_city)s, labora en nuestra empresa con un contrato a término indefinido, desde el día %(start_date)s, "
        "desempeñando el cargo de %(position)s"
    )
    salary_body = ", devengando un salario básico mensual de %(salary)s"
    bonus_body = (
        ", más un auxilio mensual no constitutivo de factor salarial, de %(bonus)s"
    )
    closure = "La presente se expide en Medellín, Colombia con destino a %(addressee)s el día %(current_date)s."
    salute = "Cordialmente,"
    signature = (
        "Vivana Taborda\n" "Operations Manager\n" "Factored SAS\n" "NIT: 901.317.478-7"
    )
    footer_text = "Calle 10B Nº 36 - 32 Oficina 402, Medellín, Antioquia | Tlf: +57 (301)7383404 | www.factored.ai"
