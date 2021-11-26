from documents.work_certificate.base import SpanishWorkCertificate
from documents.work_certificate.components import compose_body, compose_closure


def get_work_certificate(info_dict):
    margin = 10
    font = "Times"

    work_certificate = SpanishWorkCertificate(format="Letter")

    work_certificate.add_page()
    work_certificate.set_font(font, "B", 12)
    work_certificate.image(
        "images/RGB Factored Logo.png", work_certificate.w - 5 - 80, 10, h=25
    )
    # Header
    work_certificate.set_xy(0, 60)
    work_certificate.multi_cell(
        w=work_certificate.w, h=15, txt=work_certificate.header_text, align="C"
    )

    # Body
    work_certificate.set_font("", "", 12)
    work_certificate.set_xy(margin, 100)
    body = compose_body(
        work_certificate,
        info_dict["name"],
        info_dict["id_number"],
        info_dict["id_city"],
        info_dict["start_date"],
        info_dict["position"],
        info_dict["salary"],
        info_dict["bonus"],
    )
    work_certificate.multi_cell(w=work_certificate.w - 2 * margin, h=5, txt=body)

    work_certificate.set_xy(margin, work_certificate.get_y() + 20)

    closure = compose_closure(work_certificate, info_dict["addressee"])
    work_certificate.multi_cell(w=work_certificate.w - 2 * margin, h=5, txt=closure)

    jump_length = (work_certificate.h - work_certificate.get_y() - 60 - 5) / 2
    work_certificate.set_xy(margin, work_certificate.get_y() + jump_length)
    work_certificate.write(margin, work_certificate.salute)
    work_certificate.set_xy(margin, work_certificate.get_y() + jump_length - 15)
    work_certificate.image("images/signature.png", h=15)
    work_certificate.set_font("", "B", 12)
    work_certificate.multi_cell(
        work_certificate.w - 2 * margin, h=5, txt=work_certificate.signature
    )
    work_certificate.set_font("", "", 10)
    work_certificate.set_xy(margin, work_certificate.h - 30)
    work_certificate.cell(
        w=work_certificate.w - 2 * margin, txt="FACTORED S.A.S.", align="R"
    )
    work_certificate.set_xy(margin, work_certificate.h - 25)
    work_certificate.cell(
        w=work_certificate.w - 2 * margin, txt=work_certificate.footer_text, align="R"
    )

    work_certificate.output(
        dest="F", name="documents/work_certificate/results/example.pdf"
    )
