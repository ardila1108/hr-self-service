from fpdf import FPDF
from datetime import datetime

from core.entities import Document
from utils import text_functions


class VerificationLetter(FPDF, Document):
    def __init__(
        self, email, addressee, include_salary=True, include_allowance=True, language="es"
    ):
        super().__init__(format="Letter")
        self.email = email
        self.addressee = addressee
        self.include_salary = include_salary
        self.include_allowance = include_allowance
        self.font = "times"
        self.margin = 14
        if language == "es":
            self.header_text = "EL DEPARTAMENTO DE RECURSOS HUMANOS\n" "CERTIFICA"
            self.body = (
                "Que el señor %(name)s identificado con %(id_type)s No %(id_number)s de "
                "%(id_city)s, labora en nuestra empresa con un contrato a término indefinido, "
                "desde el día %(start_date)s, desempeñando el cargo de %(position)s"
            )
            self.salary_body = ", devengando un salario básico mensual de %(salary)s"
            self.allowance_body = ", más un auxilio mensual no constitutivo de factor salarial, de %(allowance)s"
            self.closure = (
                "La presente se expide en Medellín, Colombia con destino a "
                "%(addressee)s el día %(current_date)s. Si desea mayor información, nos puede contactar al correo "
                "electrónico info@factored.ai."
            )
            self.salute = "Cordialmente,"
            self.signature = (
                "Vivana Taborda\n"
                "Operations Manager\n"
                "Factored SAS\n"
                "NIT: 901.317.478-7"
            )
            self.footer_text = (
                "Calle 10B Nº 36 - 32 Oficina 402, Medellín, Antioquia |"
                "Tlf: +57 (301)7383404 | www.factored.ai"
            )
        else:
            raise NotImplementedError

    def render(self):
        info_dict = self.database.fetch_user_info(
            self.email, self.include_salary, self.include_allowance
        )
        self.add_page()
        self.set_font(self.font, "B", 12)
        self._render_header()
        self._render_body(
            info_dict["name"],
            info_dict["id_type"],
            info_dict["id_number"],
            info_dict["id_city"],
            info_dict["start_date"],
            info_dict["position"],
            info_dict.get("salary", None),
            info_dict.get("allowance", None),
        )
        self._render_closure(self.addressee)
        self._render_footer()
        return self.output(dest="S")

    def _render_header(self):
        self.image("images/RGB Factored Logo.png", self.w - 5 - 80, 10, h=25)
        self.set_xy(0, 60)
        self.multi_cell(w=self.w, h=15, txt=self.header_text, align="C")

    def _compose_body(
        self, name, id_type, id_number, id_city, start_date, position, salary, allowance
    ):
        body = self.body % {
            "name": name,
            "id_type": id_type,
            "id_number": text_functions.format_id_number(id_number),
            "id_city": id_city,
            "start_date": text_functions.get_date_in_spanish_text_format(start_date),
            "position": position,
        }
        if salary is not None:
            body += self.salary_body % {
                "salary": text_functions.number_to_money_str(salary)
            }
        if allowance is not None:
            body += self.allowance_body % {
                "allowance": text_functions.number_to_money_str(allowance)
            }
        return body + "."

    def _render_body(
        self, name, id_type, id_number, id_city, start_date, position, salary, allowance
    ):
        self.set_font("", "", 12)
        self.set_xy(self.margin, 100)
        body = self._compose_body(
            name, id_type, id_number, id_city, start_date, position, salary, allowance
        )
        self.multi_cell(w=self.w - 2 * self.margin, h=5, txt=body)

    def _compose_closure(self, addressee):
        return self.closure % {
            "current_date": text_functions.get_date_in_spanish_text_format(
                datetime.today()
            ),
            "addressee": addressee,
        }

    def _render_closure(self, addressee):
        self.set_xy(self.margin, self.get_y() + 20)

        closure = self._compose_closure(addressee)
        self.multi_cell(w=self.w - 2 * self.margin, h=5, txt=closure)

    def _render_footer(self):
        jump_length = (self.h - self.get_y() - 60 - 5) / 2
        self.set_xy(self.margin, self.get_y() + jump_length)
        self.write(self.margin, self.salute)
        self.set_xy(self.margin, self.get_y() + jump_length - 15)
        self.image("images/signature.png", h=15)
        self.set_font("", "B", 12)
        self.multi_cell(self.w - 2 * self.margin, h=5, txt=self.signature)
        self.set_font("", "", 10)
        self.set_xy(self.margin, self.h - 30)
        self.cell(w=self.w - 2 * self.margin, txt="FACTORED S.A.S.", align="R")
        self.set_xy(self.margin, self.h - 25)
        self.cell(w=self.w - 2 * self.margin, txt=self.footer_text, align="R")
