from reportlab.lib.units import cm
from reportlab.platypus import Frame, PageTemplate

from cci.report.pdf.page_template import InvoiceDocTemplate
from cci.report.pdf.flowable.ship_item import ShipItem
from ecommerce.serializers import ShipmentProcessSerializer


class ShipmentOrderPdf(InvoiceDocTemplate):
    table_head = [
        {'name': 'ลำดับ', 'cursor': (3 * cm, 0)},
        {'name': 'รายการ', 'cursor': (11.3 * cm, 0)},
        {'name': 'จำนวน', 'cursor': (0, 0)},

    ]

    def __init__(self, file_name, data=None, *args, **kwargs):
        super(ShipmentOrderPdf, self).__init__(file_name, data=data, **kwargs)

        self.letter_grid = [
            [1 * cm, self.height - (12 * cm), 1 * cm, 0.7 * cm],
            [14 * cm, self.height - (12 * cm), 14 * cm, 0]
        ]

        self.last_grid = [
            [1 * cm, self.height - (12 * cm), 1 * cm, 0],
            [14 * cm, self.height - (12 * cm), 14 * cm, 0]
        ]
        self.goods = ShipmentProcessSerializer(self.invoice).data
        return

    def get_invoice_type(self):
        return {
            'font': ('THSarabunNew Bold', 20),
            'name': (2 * cm, 3.15 * cm, 'ใบส่งของ')
        }

    def get_total_item(self):
        total = 0
        for item in self.goods['items']:
            total += int(item['qty'])
        return total

    def get_invoice_address(self):
        if self.invoice.use_manual_ship_address:
            return self.invoice.ship_address_upper, self.invoice.ship_address_last
        return self.bill_address.full_address_upper, self.bill_address.full_address_last

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
        text.textLines(self.branch.code)
        text.textLines(self.invoice.bill_number)
        text.textLines(self.invoice.date_issue.strftime('%Y-%m-%d'))
        text.textLines('1')

        self.canv.drawText(text)

        inv_type = self.get_invoice_type()
        text.setFont(*inv_type['font'])
        self.canv.drawString(*inv_type['name'])

        return

    def render_table(self, last=False, *args):
        self.canv.translate(self.leftMargin, self.bottomMargin + (6.5 * cm))
        self.canv.roundRect(0, 0, self.width, self.height - (12 * cm), 5)
        self.canv.line(0, self.height - (12.7 * cm),
                       self.width, self.height - (12.7 * cm))

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
        text.setTextOrigin(5, self.height - (12.5 * cm))
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

        for item in self.goods['items']:
            item_name = '{} {}'.format(item['code'], item['item'])
            item_count = self._determind_page_break(item_count, 1, item_list)
            item_list.append(ShipItem(no=row_count, item=item_name, qty=item['qty']))
            row_count += 1

        self.build(item_list, filename=response)
        return self.canv
