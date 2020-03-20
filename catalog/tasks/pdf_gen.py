from django.conf import settings
from fpdf import FPDF
import pathlib


def create_publication_cert(uuid, name, author, journal, publication_date, created_date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(25, 15, 15)

    pdf.image(settings.STATIC_ROOT + "/pdf/logo.png", 25, 15, 50)

    pdf.add_font('Arial', '', settings.STATIC_ROOT + '/pdf/arial.ttf', uni=True)

    pdf.set_font('Arial', '', 8)
    pdf.set_draw_color(50, 50, 50)
    pdf.cell(90, 5, ln=1)
    pdf.cell(90)
    pdf.cell(0, 3, "АНС «СибАК» ИНН 5404255395 КПП 540201001", ln=1)
    pdf.cell(90)
    pdf.cell(0, 3, "Адрес: г.Новосибирск, ул. Красный проспект, 165, офис 4", ln=1)
    pdf.cell(90)
    pdf.cell(0, 3, "Телефон: 8-913-915-38-00", ln=1)
    pdf.cell(90)
    pdf.cell(0, 3, "Р/с 40703810029100000978 в ОАО АКБ \"АВАНГАРД\"", ln=1)
    pdf.cell(90)
    pdf.cell(0, 3, "к/с 3010181000000000201", ln=1)
    pdf.cell(90)
    pdf.cell(0, 3, "БИК 044525201", ln=1)

    pdf.set_font_size(16)
    pdf.cell(0, 30, "СПРАВКА", ln=1, align="C")

    pdf.set_font_size(12)
    pdf.cell(0, 6, created_date.strftime('%d.%m.%Y') + " No. 14362", ln=1, align="L")
    pdf.cell(0, 6, ln=1)

    pdf.cell(0, 6, author, ln=1, align="R")

    pdf.cell(0, 6, ln=1)
    spisok = [name, journal, publication_date.strftime('%d.%m.%Y')]
    pdf.multi_cell(0, 6, "Издательство подтверждает, что Ваша статья «{}» \
    принята для публикации в научном журнале «{}». \
    Журнал будет опубликован на сайте издательства {}.".format(*spisok))
    pdf.cell(0, 24, ln=1)

    pathlib.Path(settings.MEDIA_ROOT + '/pdf/publication_cert').mkdir(parents=True, exist_ok=True)
    pdf.output(settings.MEDIA_ROOT + "/pdf/publication_cert/publication_cert_" + str(uuid) + ".pdf", 'F')
    return "/pdf/publication_cert/publication_cert_" + str(uuid) + ".pdf"


def create_participation_cert(uuid, name, author, journal):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(10, 15, 60)

    pdf.image(settings.STATIC_ROOT + "/pdf/ref_publication_cert.jpg", 0, 0, 210)

    pdf.add_font('Arial', '', settings.STATIC_ROOT + '/pdf/arial.ttf', uni=True)

    pdf.set_font('Arial', '', 20)
    pdf.cell(0, 50, ln=1)

    pdf.set_font('Arial', '', 32)
    pdf.cell(0, 20, ln=1)
    pdf.cell(0, 6, str(journal), ln=1, align="C")

    pdf.set_font_size(16)
    pdf.cell(0, 20, ln=1)
    pdf.cell(0, 6, author, ln=1, align="C")
    pdf.cell(0, 20, ln=1)
    pdf.cell(0, 6, "Научная статья:", ln=1, align="C")
    pdf.cell(0, 6, name, ln=1, align="C")

    pathlib.Path(settings.MEDIA_ROOT + '/pdf/participation_cert').mkdir(parents=True, exist_ok=True)
    pdf.output(settings.MEDIA_ROOT + "/pdf/participation_cert/participation_cert_" + str(uuid) + ".pdf", 'F')
    return "/pdf/participation_cert/participation_cert_" + str(uuid) + ".pdf"
