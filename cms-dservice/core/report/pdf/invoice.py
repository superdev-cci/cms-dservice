from reportlab.lib.units import cm, inch, mm

from core.report.pdf.flowable.item import ProductDescription
from core.report.pdf.flowable.promotion_item import PromotionDescription
from core.report.pdf.page_template import InvoiceDocTemplate


class InvoicePdf(InvoiceDocTemplate):

    table_head = [
        {'name': 'ลำดับ', 'cursor': (3 * cm, 0)},
        {'name': 'รายการ', 'cursor': (5.8 * cm, 0)},
        {'name': 'จำนวน', 'cursor': (1.5 * cm, 0)},
        {'name': 'หน่วยละ', 'cursor': (2 * cm, 0)},
        {'name': 'PV', 'cursor': (2 * cm, 0)},
        {'name': 'รวม', 'cursor': (2 * cm, 0)}

    ]

    def __init__(self, file_name, data=None, *args, **kwargs):
        super(InvoicePdf, self).__init__(file_name, data=data, **kwargs)
        return

    def get_invoice_type(self):
        return {
            'font': ('THSarabunNew Bold', 20),
            'name': (0.5 * cm, 3.15 * cm, 'ใบเสร็จรับเงิน/ใบกำกับภาษี')
        }

    def latest_page(self, *args, **kwargs):
        super(InvoicePdf, self).latest_page(*args, **kwargs)
        self.canv.saveState()
        self.canv.translate(inch, self.bottomMargin)
        self.canv.drawString(10, 6.2 * cm, 'การชำระเงิน')
        start = 6.2
        for x in self.invoice.get_payments():
            message = '- {} {:,}'.format(x['method'], x['amount'])
            if 'comment' in x:
                message = '{} {}'.format(message, x['comment'])
            self.canv.drawString(2 * cm, start * cm, message)
            start -= 0.4

        if self.invoice.comment is not None and self.invoice.comment != '':
            self.canv.setFont('THSarabunNew Italic', 11)
            self.canv.drawString(10, -0.5 * cm, '* หมายเหตุ {}'.format(self.invoice.comment))
        self.canv.restoreState()


    def create_pdf(self, response=None):
        item_list = []
        goods = []
        item_count = 1
        row_count = 1
        credit = None

        for x in goods:
            if x['code'] == 'SVC0001':
                credit = x
                continue
            item_name = '{} {}'.format(x['code'], x['item'])
            total_item_count = 1
            if x['type'] == 'promotion':
                total_item = [ProductDescription(no=row_count,
                                                 item=item_name,
                                                 qty=x['qty'],
                                                 pv=x['pv'],
                                                 price=int(x['prices']) / int(x['qty']),
                                                 total=x['prices'])]
            else:
                total_item = [ProductDescription(no=row_count,
                                                 item=item_name,
                                                 qty=x['qty'],
                                                 pv=x['pv'],
                                                 price=int(x['prices']) / int(x['qty']),
                                                 total=x['prices'])]
            if x['type'] == 'promotion':
                for child in x['product']:
                    total_item_count += 1
                    child_name = '{} {} ({})'.format(child['code'], child['item'], child['qty'] * x['qty'])
                    total_item.append(PromotionDescription(item=child_name))

            # item_count += total_item_count
            row_count += 1

            item_count = self._determind_page_break(item_count, total_item_count, item_list)
            for item in total_item:
                item_list.append(item)

        if credit:
            item_name = '{} {}'.format(credit['code'], credit['item'])
            item_list.append(ProductDescription(no=row_count,
                                                item=item_name,
                                                qty=1,
                                                pv=0,
                                                price=credit['prices'],
                                                total=credit['prices']))
        elif self.invoice.credit_fee:
            item_list.append(ProductDescription(no=row_count,
                                                item='SVC0001 ค่าธรรมเนียมรูดบัตร',
                                                qty=1,
                                                pv=0,
                                                price=self.invoice.credit_fee,
                                                total=self.invoice.credit_fee))
        row_count += 1
        self._determind_page_break(item_count, 1, item_list)

        if self.invoice.shipment_fee:
            item_list.append(ProductDescription(no=row_count,
                                                item='ค่าจัดส่ง',
                                                qty=1,
                                                pv=0,
                                                price=self.invoice.shipment_fee,
                                                total=self.invoice.shipment_fee))

        self.build(item_list, filename=response)
        return self.canv
