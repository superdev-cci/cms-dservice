from reportlab.lib.units import cm, inch
from reportlab.platypus import Frame, PageTemplate, PageBreak

from core.report.pdf.page_template import InvoiceDocTemplate
from core.report.pdf.flowable.ship_item import ShipItem
from branch.models import StockAdjustStatement, StockAdjustItem, Branch
from branch.serializers import StockAdjustStatementSerializer


class StockAdjustPdf(InvoiceDocTemplate):
    table_head = [
        {'name': 'ลำดับ', 'cursor': (3 * cm, 0)},
        {'name': 'รายการ', 'cursor': (11.3 * cm, 0)},
        {'name': 'จำนวน', 'cursor': (0, 0)},

    ]

    def __init__(self, file_name, data=None, *args, **kwargs):
        super(StockAdjustPdf, self).__init__(file_name, data=data, **kwargs)

        self.letter_grid = [
            [1 * cm, self.height - (10 * cm), 1 * cm, 0.7 * cm],
            [14 * cm, self.height - (10 * cm), 14 * cm, 0]
        ]

        self.last_grid = [
            [1 * cm, self.height - (10 * cm), 1 * cm, 0],
            [14 * cm, self.height - (10 * cm), 14 * cm, 0]
        ]
        self.items = StockAdjustStatementSerializer(self.invoice).data['items']
        return

    def get_branch_data(self):
        branch = Branch.objects.filter(inv_code=self.branch).first()
        branch_data = {
            'name': 'บริษัท ซีซีไอ อินเตอร์เนชั่นแนล จำกัด (สำนักงานใหญ่)',
            'address_first': 'เลขที่ 9 อาคารพุทธวิชชาลัย โซนบี และ โซนซี',
            'address_mid': 'ถนนแจ้งวัฒนะ แขวงอนุสาวรีย์ เขตบางเขน กรุงเทพฯ 10220',
            'tax_info': 'เลขประจำตัวผู้เสียภาษี 0-1055-59080-08-9',
        }

        if branch:
            if branch.code != 'BKK01':
                branch_data['name'] = 'บริษัทแชมป์ ออฟ แชมห์ อินโนเวชั่น จำกัด ({})'.format(branch.name)

            if branch.code == 'KL01':
                branch_data['address_first'] = '517/119 ถนนมิตรภาพ-หนองคาย'
                branch_data['address_mid'] = 'ตำบลในเมือง อำเภอเมืองนครราชสีมา จังหวัดนครราชสีมา 30000'
            elif branch.code == 'HY01':
                branch_data['address_first'] = 'เลขที่ 403 ถนนนิพัทธ์สงเคราะห์ 4'
                branch_data['address_mid'] = 'ตำบลหาดใหญ่ อำเภอหาดใหญ่ จังหวัดสงขลา 90110'

            elif branch.code == 'CRI01':
                branch_data['address_first'] = 'เลขที่ 111/1 หมู่ 13'
                branch_data['address_mid'] = 'ตำบลสันทราย อำเภอเมืองเชียงราย จังหวัดเชียงราย 57000'

        return branch_data

    def get_head_info(self):
        self.customer = 'Company'
        self.bill_address = ''
        self.branch = self.invoice.inv_code
        return

    def get_invoice_type(self):
        return {
            'font': ('THSarabunNew Bold', 20),
            'name': (2 * cm, 3.15 * cm, 'ใบปรับสินค้า')
        }

    def get_total_item(self):
        total = 0
        for item in self.items:
            total += int(item['qty'])
        return total

    def get_invoice_address(self):
        return ''

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
        text.textLines('ใบที่')
        self.canv.drawText(text)

        text = self.canv.beginText()
        text.setTextOrigin(1.5 * cm, start_y)
        text.setFont('THSarabunNew Bold', 13)
        text.textLines(self.branch)
        text.textLines(self.invoice.bill_number)
        text.textLines(self.invoice.date_issue.strftime('%Y-%m-%d'))
        text.textLines('1')

        self.canv.drawText(text)

        inv_type = self.get_invoice_type()
        text.setFont(*inv_type['font'])
        self.canv.drawString(*inv_type['name'])

        return

    def render_customer(self):
        start_y = 3 * cm
        self.canv.translate(0, (-4 * cm))
        self.canv.roundRect(0, 0, (10 * cm), (3.8 * cm), 5)
        #
        text = self.canv.beginText()
        text.setTextOrigin(2.5 * cm, start_y)
        text.setFont('THSarabunNew Bold', 14)
        # text.textLines('{}'.format('หมายเหตุ'))
        if self.invoice.remark:
            text.textLines('{}'.format(self.invoice.remark))
        else:
            text.textLines('-')
        # # text.textLines('{}'.format(self.customer.person.id_card))
        #
        # # if self.customer.person.mobile != '0':
        # #     text.textLines('{}'.format(self.customer.person.mobile))
        # # else:
        # #     text.textLines('-')
        # # if self.bill_address is not None:
        # #     upper_line, last_line = self.get_invoice_address()
        # #     text.textLines(upper_line)
        # #     text.textLines(last_line)
        #
        self.canv.drawText(text)
        #
        text = self.canv.beginText()
        text.setTextOrigin(10, start_y)
        text.setFont('THSarabunNew Bold', 14)
        text.textLines('หมายเหตุ : ')
        # text.textLines('ชื่อ-สกุล')
        # text.textLines('เลขประจำตัวผู้เสียภาษี')
        # text.textLines('เบอร์โทรศัพท์')
        # text.textLines('ที่อยู่')
        #
        self.canv.drawText(text)
        return

    def render_footer(self, show_barcode=False):
        sign_detail = 1.8 * cm
        date_detail = 0.3 * cm
        self.canv.setFont('THSarabunNew', 12)
        self.canv.translate(inch, self.bottomMargin)
        self.canv.roundRect(0, 0, self.width, (2.3 * cm), 5)

        # self.canv.rect(3 * cm, 0, 3 * cm, 2 * cm)
        # self.canv.drawString(1.5 * cm, date_detail, 'วันที่ ......../......./........')
        # self.canv.drawString(6.5 * cm, date_detail, 'วันที่ ......../......./........')
        self.canv.drawString(11.5 * cm, date_detail, 'วันที่ ......../......./........')
        # self.canv.drawString(2.3 * cm, sign_detail, 'ผู้รับเงิน')
        self.canv.drawString(12.3 * cm, sign_detail, 'ผู้จัดทำ')
        # self.canv.drawString(12.3 * cm, sign_detail, 'ลูกค้า')

        if show_barcode:
            self.render_barcode()

        # self.canv.setFont('THSarabunNew Italic', 11)
        # self.canv.drawString(10, 4.5 * cm,
        #                      'ข้าพเจ้าได้รับสินค้าตามรายการที่ระบุไว้ข้างต้นครบถ้วนและสมบูรณ์เรียบร้อยแล้ว')
        # self.canv.drawString(10, 4.1 * cm,
        #                      'สินค้าโปรโมชั่น ไม่สามารถเปลี่ยนหรือคืนได้')
        return

    def render_table(self, last=False, *args):
        self.canv.translate(self.leftMargin, self.bottomMargin + (4.5 * cm))
        self.canv.roundRect(0, 0, self.width, self.height - (10 * cm), 5)
        self.canv.line(0, self.height - (10.7 * cm),
                       self.width, self.height - (10.7 * cm))

        if last:
            line_list = self.letter_grid
            self.canv.line(0, 0.7 * cm, self.width, 0.7 * cm)

            self.canv.setFont('THSarabunNew Bold', 14)
            self.canv.drawRightString(13.2 * cm, 0.15 * cm, 'รวม')

            self.canv.drawRightString(15.5 * cm, 0.15 * cm, '{:,d}'.format(self.get_total_item()))

        else:
            line_list = self.last_grid

        self.canv.lines(line_list)

        text = self.canv.beginText()
        text.setTextOrigin(5, self.height - (10.5 * cm))
        text.setFont(*self.table_head_font_style)
        for x in self.table_head:
            text.textOut(x['name'])
            text.moveCursor(*x['cursor'])

        self.canv.drawText(text)

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
        self.canv.restoreState()
        self.render_page_count()
        return

    def create_pdf(self, response=None):
        item_list = []
        item_count = 1
        row_count = 1

        for item in self.items:
            item_name = '{} {}'.format(item['product'], item['product_name'])
            item_count = self._determind_page_break(item_count, 1, item_list)
            item_list.append(ShipItem(no=row_count, item=item_name, qty=item['qty']))
            row_count += 1

        self.build(item_list, filename=response)
        return self.canv

    def create_page_template(self):
        frame_template = Frame(self.leftMargin, self.bottomMargin + (4.5 * cm),
                               self.width, self.height - (10.8 * cm),
                               id='normal', showBoundary=0)
        frame_last = Frame(self.leftMargin, self.bottomMargin + (4.5 * cm),
                           self.width, self.height - (10.8 * cm),
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

    def _determind_page_break(self, current, count, items):
        current += count
        if current > 26:
            items.append(PageBreak())
            current = 1
        return current
