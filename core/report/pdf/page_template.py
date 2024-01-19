from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageBreak, Frame, PageTemplate
from reportlab.graphics.barcode import code128


class InvoiceDocTemplate(BaseDocTemplate):
    logo_path = './templates/report/logo_cci.jpg'
    page_size = A4
    unit = cm

    letter_grid = []
    last_grid = []

    table_head_font_style = ('THSarabunNew Bold', 13)
    table_head = []

    def __init__(self, file_name, data=None, *args, **kwargs):
        self.file_name = '{}.pdf'.format(file_name)
        super(InvoiceDocTemplate, self).__init__(self.file_name, pagesize=self.page_size, **kwargs)

        pdfmetrics.registerFont(TTFont('THSarabunNew', './templates/THSarabunNew.ttf'))
        pdfmetrics.registerFont(TTFont('THSarabunNew Bold', './templates/THSarabunNew Bold.ttf'))
        pdfmetrics.registerFont(TTFont('THSarabunNew Italic', './templates/THSarabunNew Italic.ttf'))
        pdfmetrics.registerFont(TTFont('ANGSA', './templates/ANGSA.ttf'))
        pdfmetrics.registerFont(TTFont('angsab', './templates/angsab.ttf'))
        pdfmetrics.registerFont(TTFont('ANGSAI', './templates/ANGSAI.ttf'))

        self.invoice = data
        self.customer = ''
        self.bill_address = ''
        self.branch = ''
        self.get_head_info()
        self.total_page = 0

        self.letter_grid = [
            [1 * cm, self.height - (12 * cm), 1 * cm, 0.7 * cm],
            [8.7 * cm, self.height - (12 * cm), 8.7 * cm, 0.7 * cm],
            [10.2 * cm, self.height - (12 * cm), 10.2 * cm, 0.7 * cm],
            [11.9 * cm, self.height - (12 * cm), 11.9 * cm, 0],
            [13.5 * cm, self.height - (12 * cm), 13.5 * cm, 0]
        ]

        self.last_grid = [
            [1 * cm, self.height - (12 * cm), 1 * cm, 0],
            [8.7 * cm, self.height - (12 * cm), 8.7 * cm, 0],
            [10.2 * cm, self.height - (12 * cm), 10.2 * cm, 0],
            [11.9 * cm, self.height - (12 * cm), 11.9 * cm, 0],
            [13.5 * cm, self.height - (12 * cm), 13.5 * cm, 0]
        ]

        return

    def get_head_info(self):
        self.customer = self.invoice.member
        self.bill_address = self.invoice.bill_address
        self.branch = self.invoice.branch

    def get_letter_table(self):
        return

    def get_branch_data(self):
        branch_data = {
            'name': 'บริษัทแชมป์ ออฟ แชมห์ อินโนเวชั่น จำกัด (สำนักงาน ใหญ่)',
            # 'address_first': 'เลขที่ 9 อาคารพุทธวิชชาลัย โซนบี และ โซนซี',
            'address_first': '{} {}'.format(self.branch.location.address, self.branch.location.street),
            'address_mid': 'แขวง{} เขต{} {} {}'.format(
                self.branch.location.sub_district,
                self.branch.location.district,
                self.branch.location.province,
                self.branch.location.post_code,
            ),
            'tax_info': 'เลขประจำตัวผู้เสียภาษี 0-1055-59080-08-9',
        }
        if self.branch.location.province != 'กรุงเทพมหานคร':
            branch_data['address_mid'] = 'ตำบล{} อำเภอ{} {} {}'.format(
                self.branch.location.sub_district,
                self.branch.location.district,
                self.branch.location.province,
                self.branch.location.post_code,
            )
        if self.branch.code != 'BKK01':
            branch_data['name'] = 'บริษัทแชมป์ ออฟ แชมห์ อินโนเวชั่น จำกัด (สาขา {})'.format(self.branch.name)

        return branch_data

    def get_invoice_type(self):

        return {
            'font': ('THSarabunNew Bold', 20),
            'name': (0.5 * cm, 3.15 * cm, 'Not implement')
        }

    def get_invoice_address(self):
        return self.bill_address.full_address_upper, self.bill_address.full_address_last

    def render_page_count(self):
        self.canv.setFont('THSarabunNew Bold', 12)
        self.canv.drawString(inch * 6.8, 0.75 * inch, "หน้า {}/{}".format(self.page, self.total_page))

        return

    def render_barcode(self):
        barc = code128.Code128(self.invoice.bill_number, barWidth=0.4 * mm, barHeight=1.2 * cm)
        self.canv.drawString(2.8 * cm, 2.4 * cm, self.invoice.bill_number)
        barc.drawOn(self.canv, 0, 2.7 * cm)

    def render_head(self):
        self.canv.setFont('THSarabunNew Bold', 18)
        self.canv.translate(inch, 26 * cm)
        self.canv.drawImage(self.logo_path, 0, 0, width=75, height=70)
        branch_info = self.get_branch_data()
        self.canv.drawString(100, 2.2 * cm, branch_info['name'])

        text = self.canv.beginText()
        text.setTextOrigin(100, 1.5 * cm)
        text.setFont('THSarabunNew Bold', 14)
        text.textLine(text=branch_info['address_first'])
        text.textLine(text=branch_info['address_mid'])
        text.textLine(text=branch_info['tax_info'])
        self.canv.drawText(text)
        return

    def render_customer(self):
        start_y = 3.3 * cm
        self.canv.translate(0, (-4 * cm))
        self.canv.roundRect(0, 0, (10 * cm), (3.8 * cm), 5)

        text = self.canv.beginText()
        text.setTextOrigin(3.8 * cm, start_y)
        text.setFont('THSarabunNew Bold', 14)
        text.textLines('{}'.format(self.customer.code))
        text.textLines('{}'.format(self.customer.full_name))
        text.textLines('{}'.format(self.customer.person.id_card))

        if self.customer.person.mobile != '0':
            text.textLines('{}'.format(self.customer.person.mobile))
        else:
            text.textLines('-')
        if self.bill_address is not None:
            upper_line, last_line = self.get_invoice_address()
            text.textLines(upper_line)
            text.textLines(last_line)

        self.canv.drawText(text)

        text = self.canv.beginText()
        text.setTextOrigin(10, start_y)
        text.setFont('THSarabunNew Bold', 14)
        text.textLines('รหัสสมาชิก')
        text.textLines('ชื่อ-สกุล')
        text.textLines('เลขประจำตัวผู้เสียภาษี')
        text.textLines('เบอร์โทรศัพท์')
        text.textLines('ที่อยู่')

        self.canv.drawText(text)
        return

    def render_bill_header(self):
        start_y = 2 * cm
        self.canv.translate((10.3 * cm), 0)
        self.canv.roundRect(0, 0, (5.6 * cm), (2.55 * cm), 5)

        text = self.canv.beginText()
        text.setTextOrigin(10, start_y)
        text.setFont('THSarabunNew Bold', 13)
        text.textLines('สาขา')
        text.textLines('เลขบิล')
        text.textLines('วันที่')
        text.textLines('ประเภท')
        self.canv.drawText(text)

        text = self.canv.beginText()
        text.setTextOrigin(1.5 * cm, start_y)
        text.setFont('THSarabunNew Bold', 13)
        text.textLines(self.branch.code)
        text.textLines(self.invoice.bill_number)
        text.textLines(self.invoice.date_issue.strftime('%Y-%m-%d'))
        text.textLines(self.invoice.bill_type.name)

        self.canv.drawText(text)

        inv_type = self.get_invoice_type()
        text.setFont(*inv_type['font'])
        self.canv.drawString(*inv_type['name'])

        return

    def render_footer(self, show_barcode=True):
        sign_detail = 1.8 * cm
        date_detail = 0.3 * cm
        self.canv.setFont('THSarabunNew', 12)
        self.canv.translate(inch, self.bottomMargin)
        self.canv.roundRect(0, 0, self.width, (2.3 * cm), 5)

        # self.canv.rect(3 * cm, 0, 3 * cm, 2 * cm)
        self.canv.drawString(1.5 * cm, date_detail, 'วันที่ ......../......./........')
        self.canv.drawString(6.5 * cm, date_detail, 'วันที่ ......../......./........')
        self.canv.drawString(11.5 * cm, date_detail, 'วันที่ ......../......./........')
        self.canv.drawString(2.3 * cm, sign_detail, 'ผู้รับเงิน')
        self.canv.drawString(7.3 * cm, sign_detail, 'ผู้จัดทำ')
        self.canv.drawString(12.3 * cm, sign_detail, 'ลูกค้า')

        if show_barcode:
            self.render_barcode()

        self.canv.setFont('THSarabunNew Italic', 11)
        self.canv.drawString(10, 4.5 * cm,
                             'ข้าพเจ้าได้รับสินค้าตามรายการที่ระบุไว้ข้างต้นครบถ้วนและสมบูรณ์เรียบร้อยแล้ว')
        self.canv.drawString(10, 4.1 * cm,
                             'สินค้าโปรโมชั่น ไม่สามารถเปลี่ยนหรือคืนได้')
        return

    def render_total(self):
        self.canv.translate(9 * cm, 3.5 * cm)
        self.canv.roundRect(0, 0, 6.9 * cm, 3 * cm, 5)

        text = self.canv.beginText()
        text.setTextOrigin(10, 2.3 * cm)
        text.setFont('THSarabunNew Bold', 14)
        text.textLine('ส่วนลด')
        text.textLine('ราคารวม')
        text.textLine('ภาษีมูลค่าเพิ่ม 7%')
        text.textLine('ราคารวมทั้งหมด')

        self.canv.drawText(text)

        text = self.canv.beginText()
        text.setTextOrigin(4 * cm, 2.3 * cm)
        text.setFont('THSarabunNew Bold', 14)
        if self.invoice.discount:
            text.textLine('{:,.02f}'.format(self.invoice.discount))
        else:
            text.textLine('-')

        text.textLine('{:,.02f}'.format(self.invoice.price_without_vat))
        text.textLine('{:,.02f}'.format(self.invoice.vat))
        text.textLine('{:,.02f}'.format(self.invoice.price))

        self.canv.drawText(text)

        return

    def render_table(self, last=False, show_num_text=True):
        t_height = self.height - (12 * cm)
        self.canv.translate(inch, self.bottomMargin + (6.5 * cm))
        self.canv.roundRect(0, 0, self.width, self.height - (12 * cm), 5)
        self.canv.line(0, self.height - (12.7 * cm),
                       self.width, self.height - (12.7 * cm))

        if last:
            line_list = self.letter_grid
            self.canv.line(0, 0.7 * cm, self.width, 0.7 * cm)

            # if show_num_text:
            #     self.canv.setFont('THSarabunNew Bold', 14)
            #     self.canv.drawRightString(11.5 * cm, 0.15 * cm, num_to_text.thai_num2text(self.invoice.total_price))
            self.canv.setFont('THSarabunNew Bold', 12)

            self.canv.drawRightString(13.2 * cm, 0.15 * cm, '{:,d}'.format(int(self.invoice.pv)))
            self.canv.drawRightString(15.5 * cm, 0.15 * cm, '{:,.2f}'.format(self.invoice.price))

        else:
            line_list = self.last_grid

        self.canv.lines(line_list)

        text = self.canv.beginText()
        text.setTextOrigin(5, self.height - (12.5 * cm))
        text.setFont(*self.table_head_font_style)
        for x in self.table_head:
            text.textOut(x['name'])
            text.moveCursor(*x['cursor'])

        self.canv.drawText(text)

    def later_page(self, *args, **kwargs):
        # Header section
        self.canv.saveState()
        self.render_head()
        self.render_customer()
        self.render_bill_header()
        self.canv.restoreState()

        # Body
        self.canv.saveState()
        self.render_table()
        self.canv.restoreState()

        # Footer section
        self.canv.saveState()
        self.render_footer()
        # self.render_total()
        self.canv.restoreState()
        self.render_page_count()
        return

    def latest_page(self, *args, **kwargs):
        # Header section
        self.canv.saveState()
        self.render_head()
        self.render_customer()
        self.render_bill_header()
        self.canv.restoreState()

        # Body
        self.canv.saveState()
        self.render_table(True, True)
        self.canv.restoreState()

        # Footer section
        self.canv.saveState()
        self.render_footer()
        self.render_total()
        self.canv.restoreState()
        self.render_page_count()
        return

    def handle_pageBegin(self):
        self._handle_pageBegin()
        next_page = self.page + 1
        if next_page >= self.total_page:
            self._handle_nextPageTemplate('final')
        # self._handle_nextPageTemplate('Later')'

    def create_page_template(self):
        frame_template = Frame(self.leftMargin, self.bottomMargin + (6.5 * cm),
                               self.width, self.height - (12.8 * cm),
                               id='normal', showBoundary=0)
        frame_last = Frame(self.leftMargin, self.bottomMargin + (6.5 * cm),
                           self.width, self.height - (12.8 * cm),
                           id='last', showBoundary=0)
        if self.total_page != 1:
            template_pool = [
                PageTemplate(id='defaut', frames=frame_template, onPage=self.later_page, pagesize=self.page_size),
                PageTemplate(id='final', frames=frame_last, onPage=self.latest_page, pagesize=self.page_size),
            ]
        else:
            template_pool = [
                PageTemplate(id='final', frames=frame_last, onPage=self.latest_page, pagesize=self.page_size), ]
        self.addPageTemplates(template_pool)
        return

    def build(self, flowables, filename=None, canvasmaker=canvas.Canvas):
        self.total_page = 1
        for x in flowables:
            if isinstance(x, PageBreak):
                self.total_page += 1

        self._calc()  # in case we changed margins sizes etc

        self.create_page_template()

        super(InvoiceDocTemplate, self).build(flowables, filename, canvasmaker)
        return

    def create_pdf(self, response=None):
        return NotImplemented('Not imprement')

    def _determind_page_break(self, current, count, items):
        current += count
        if current > 22:
            items.append(PageBreak())
            current = 1
        return current
