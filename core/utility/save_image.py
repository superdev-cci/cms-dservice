import os
import uuid
from reportlab.lib.colors import white, Color
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

write_transparent = Color(60, 60, 60, alpha=0.8)

pdfmetrics.registerFont(TTFont('THSarabunNew', './templates/THSarabunNew.ttf'))
pdfmetrics.registerFont(TTFont('THSarabunNew Bold', './templates/THSarabunNew Bold.ttf'))
pdfmetrics.registerFont(TTFont('THSarabunNew Italic', './templates/THSarabunNew Italic.ttf'))


def create_image_pdf(path, file, member_code):
    file_path = '{}/{}'.format(path, file.name)
    filename, file_extension = os.path.splitext(file_path)
    temp_name = '{}{}'.format(uuid.uuid4().hex, file_extension)
    file_path = '{}/{}'.format(path, temp_name)
    # create temp image
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    page_size = A4
    c = canvas.Canvas('{}/{}.pdf'.format(path, member_code), pagesize=page_size)
    width, height = page_size
    try:
        c.drawImage(file_path, 0, 0, width=width, height=height)
        c.setFillColor(write_transparent)
        c.setStrokeColor(white)
        c.setFont("THSarabunNew Bold", 20)

        c.saveState()
        c.rotate(45)
        c.translate(0, -15 * cm)
        for i in range(1, 15):
            if i % 2 == 1:
                c.drawString(1 * cm, 3 * i * cm, 'บริษัทแชมป์ ออฟ แชมป์ อินโนเวชั่น จำกัด')
                c.drawString(16 * cm, 3 * i * cm, 'บริษัทแชมป์ ออฟ แชมป์ อินโนเวชั่น จำกัด')
                c.drawString(32 * cm, 3 * i * cm, 'บริษัทแชมป์ ออฟ แชมป์ อินโนเวชั่น จำกัด')
            else:
                c.drawString(8 * cm, 3 * i * cm, 'บริษัทแชมป์ ออฟ แชมป์ อินโนเวชั่น จำกัด')
                c.drawString(24 * cm, 3 * i * cm, 'บริษัทแชมป์ ออฟ แชมป์ อินโนเวชั่น จำกัด')
                c.drawString(40 * cm, 3 * i * cm, 'บริษัทแชมป์ ออฟ แชมป์ อินโนเวชั่น จำกัด')

        c.restoreState()
        c.showPage()
        c.save()
    finally:
        os.remove(file_path)

    return
