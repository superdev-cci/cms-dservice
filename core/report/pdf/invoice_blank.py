from reportlab.graphics.barcode import code128
from reportlab.lib.units import cm, inch, mm
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import Frame, PageTemplate, PageBreak

from branch.models import Branch
from core.report.pdf.flowable.item_blank import ProductDescription
from core.report.pdf.flowable.promotion_item_blank import PromotionDescription
from core.report.pdf.page_template import InvoiceDocTemplate
from core.utility import num_to_text
from ecommerce.models import Promotion, Product


class InvoicePdfBlankTemplate(InvoiceDocTemplate):
    page_size = (9 * inch, 11 * inch)
    margin_buttom = (1 * cm)
    margin_top = (11 * inch) - (1.2 * cm)
    margin_left = (1.5 * cm)
    margin_right = (9 * inch) - (3 * cm)

    table_head = [
        {'name': 'ลำดับ', 'cursor': (3 * cm, 0)},
        {'name': 'รายการ', 'cursor': (5.8 * cm, 0)},
        {'name': 'จำนวน', 'cursor': (1.5 * cm, 0)},
        {'name': 'หน่วยละ', 'cursor': (2 * cm, 0)},
        {'name': 'PV', 'cursor': (2 * cm, 0)},
        {'name': 'รวม', 'cursor': (2 * cm, 0)}

    ]

    def __init__(self, file_name, data=None, *args, **kwargs):
        self.branch_obj = None
        super(InvoicePdfBlankTemplate, self).__init__(file_name, data=data, **kwargs)

        return

    def get_invoice_type(self):
        return {
            'font': ('Helvetica', 20),
            'name': (0.5 * cm, 3.15 * cm, 'ใบเสร็จรับเงิน/ใบกำกับภาษี')
        }

    def get_head_info(self):
        self.customer = self.invoice.member
        # self.bill_address = self.invoice.member.bill_address
        self.branch = self.invoice.inv_code
        self.branch_obj = Branch.objects.get(inv_code=self.branch)

    def get_branch_data(self):
        branch = self.branch_obj
        branch_data = {
            'name': '(สำนักงาน ใหญ่)',
            # 'address_first': 'เลขที่ 9 อาคารพุทธวิชชาลัย โซนบี และ โซนซี',
            'address_first': '{}'.format(branch.address),
            'address_mid': 'แขวง{} เขต{} {} {}'.format(
                branch.sub_district,
                branch.district,
                branch.province,
                branch.post_code,
            ),
            'tax_info': 'เลขประจำตัวผู้เสียภาษี 0-1055-59080-08-9',
        }
        if branch.province != 'กรุงเทพมหานคร':
            branch_data['address_mid'] = 'ตำบล{} อำเภอ{} {} {}'.format(
                branch.sub_district,
                branch.district,
                branch.province,
                branch.post_code,
            )
        if branch.code != 'BKK01':
            branch_data['name'] = '(สาขา {})'.format(self.branch_obj.inv_desc)
        return branch_data

    def get_invoice_address(self):
        return self.invoice.full_address_upper, self.invoice.full_address_last

    def latest_page(self, *args, **kwargs):
        super(InvoicePdfBlankTemplate, self).latest_page(*args, **kwargs)
        self.canv.saveState()
        self.canv.translate(inch, self.bottomMargin)
        self.canv.drawString(10, 6.2 * cm, 'การชำระเงิน')
        start = 6.2
        # for x in self.invoice.get_payments():
        #     message = '- {} {:,}'.format(x['method'], x['amount'])
        #     if 'comment' in x:
        #         message = '{} {}'.format(message, x['comment'])
        #     self.canv.drawString(2 * cm, start * cm, message)
        #     start -= 0.4

        # if self.invoice.remark is not None and self.invoice.remark != '':
        #     self.canv.setFont('ANGSAI', 11)
        #     self.canv.drawString(10, -0.5 * cm, '* หมายเหตุ {}'.format(self.invoice.remark))
        self.canv.restoreState()

    def render_head(self):
        # self.canv.drawString((1.5 * cm), (11 * inch) - (1.2 * cm), 'x')
        # self.canv.drawString((1.5 * cm), (1 * cm), 'x')
        # self.canv.drawString((9 * inch) - (1.7 * cm), (1 * cm), 'x')
        # self.canv.drawString((9 * inch) - (1.7 * cm), (11 * inch) - (1.2 * cm), 'x')

        # self.canv.roundRect((1.5 * cm), (1 * cm), (9 * inch) - (3 * cm), (11 * inch) - (2 * cm), 0)
        self.canv.saveState()
        self.canv.setFont('ANGSA', 14)
        self.canv.translate(0, 11 * inch)
        branch_info = self.get_branch_data()
        # self.canv.drawString(8 * inch, -(1.5 * cm), branch_info['name'])

        text = self.canv.beginText()
        text.setTextOrigin(6 * cm, -(2.0 * cm))
        text.setFont('ANGSA', 12)
        # text.setHorizScale(90)
        text.textLine(text=branch_info['address_first'])
        text.textLine(text=branch_info['address_mid'])
        if self.branch_obj.branch_number != '0000':
            text.textLine(text='สาขาที่ออกใบกำกับภาษี {} ({})'.format(self.branch_obj.branch_number, self.branch_obj.province))
        else:
            text.textLine(text='สาขาที่ออกใบกำกับภาษี {} (สนญ.)'.format(self.branch_obj.branch_number))

        self.canv.drawText(text)
        self.canv.restoreState()
        return

    def render_customer(self):
        self.canv.saveState()
        self.canv.setFont('ANGSA', 14)
        self.canv.translate(0.5 * inch, 11 * inch)
        start_y = -3.6 * cm
        if self.invoice.sa_type == 'WI':
            self.canv.drawString(3 * cm, start_y, self.invoice.mcode)
        else:
            self.canv.drawString(3 * cm, start_y, self.invoice.member.mcode)
        start_y -= 0.6 * cm
        if self.invoice.sa_type == 'WI':
            full_name = self.invoice.name_t
            upper_address = self.invoice.full_address_upper
            lower_address = self.invoice.full_address_last
        else:
            full_name = self.invoice.name_t
            upper_address = self.invoice.member.full_address_upper
            lower_address = self.invoice.member.full_address_last

        if len(full_name) > 60:
            self.canv.setFont('ANGSA', 12)
            name = full_name.split(' ')
            if len(name) > 3:
                self.canv.drawString(3 * cm, start_y, '{} {}'.format(name[0], name[1]))
                start_y -= 10
                name = name[2:]
                name_text = ''
                for x in name:
                    name_text = '{} {}'.format(name_text, x)

                self.canv.drawString(3 * cm, start_y, name_text)
                self.canv.setFont('ANGSA', 14)
            else:
                self.canv.setFont('ANGSA', 14)
                self.canv.drawString(3 * cm, start_y, full_name)
        else:
            self.canv.drawString(3 * cm, start_y, full_name)
        start_y -= 0.8 * cm
        self.canv.drawString(3 * cm, start_y, upper_address)
        start_y -= 0.6 * cm
        self.canv.drawString(3 * cm, start_y, lower_address)
        start_y -= 0.8 * cm
        if self.invoice.sa_type != 'WI':
            if self.invoice.member.mtype == 1:
                if self.invoice.member.id_tax != '':
                    self.canv.drawString(4 * cm, start_y, self.invoice.member.id_tax)
                else:
                    self.canv.drawString(4 * cm, start_y, self.invoice.member.id_card)
            else:
                self.canv.drawString(4 * cm, start_y, self.invoice.member.id_card)

        start_y -= 1 * cm
        self.canv.drawString(3 * cm, start_y, self.invoice.txtoption)
        self.canv.restoreState()
        return

    def render_bill_header(self):
        self.canv.saveState()
        self.canv.setFont('ANGSA', 14)
        self.canv.translate(0.5 * inch, 11 * inch)
        bill_name = 'ปกติ'
        if self.invoice.sa_type == 'H':
            bill_name = "HOLD"
        elif self.invoice.sa_type == 'L':
            bill_name = "แลกของ"
        elif self.invoice.sa_type == 'B':
            bill_name = "สมาชิก"
        elif self.invoice.sa_type == 'CF':
            bill_name = "บิลพนักงาน"
        elif self.invoice.sa_type == 'WI':
            bill_name = "บิล Walk in"
        payment = self.invoice.get_payments()
        start_y = -3.6 * cm
        start_x = 16 * cm
        self.canv.drawString(start_x, start_y, self.invoice.inv_code)
        start_y -= 0.7 * cm
        self.canv.drawString(start_x, start_y, self.invoice.bill_number)
        start_y -= 0.6 * cm
        self.canv.drawString(start_x, start_y, self.invoice.sadate.strftime('%d-%m-%Y'))
        start_y -= 0.7 * cm
        self.canv.drawString(start_x, start_y, bill_name)
        start_y -= 0.7 * cm
        self.canv.drawString(start_x, start_y, payment['type'])
        start_y -= 0.7 * cm
        if self.invoice.sa_type == 'WI':
            self.canv.drawString(start_x, start_y, 'WALK IN')
        else:
            self.canv.drawString(start_x, start_y, self.invoice.member.get_group())
        self.canv.restoreState()
        return

    def render_footer(self, show_barcode=True):
        if show_barcode:
            self.render_barcode()
        return

    def render_barcode(self):
        barc = code128.Code128(self.invoice.bill_number, barWidth=0.4 * mm, barHeight=1 * cm)
        self.canv.drawString(3 * cm, 4 * cm, self.invoice.bill_number)
        barc.drawOn(self.canv, 1.2 * cm, 4.4 * cm)
        self.canv.setFont('ANGSA', 14)
        self.canv.drawString(10 * cm, 5 * cm, 'ผู้ทำรายการ {}'.format(self.invoice.create_by))
        self.canv.drawString(10 * cm, 4.5 * cm, self.invoice.create_time.strftime('%Y-%m-%d %H:%M:%S'))
        self.canv.drawString(10 * cm, 4 * cm, 'Box size : {}'.format(self.invoice.box_size))
        if self.invoice.dl == 'E':
            self.canv.setFont('ANGSA', 18)
            self.canv.drawString(10 * cm, 3.5 * cm, 'CCI Express')
        self.canv.setFont('ANGSA', 12)

    def render_total(self):
        self.canv.saveState()
        self.canv.setFont('ANGSA', 14)
        self.canv.translate(0.5 * inch, 11 * inch)

        start_y = -21 * cm
        start_x = 18 * cm
        self.canv.drawString(start_x, start_y, '{:,.02f}'.format(self.invoice.total))
        start_y -= 0.9 * cm
        self.canv.drawString(start_x - (1.5 * cm), start_y, '7')
        self.canv.drawString(start_x, start_y, '{:,.02f}'.format(self.invoice.total_vat))
        start_y -= 1 * cm
        self.canv.drawString(start_x, start_y, '{:,.02f}'.format(self.invoice.total_invat))

        payment = self.invoice.get_payments()
        start_x = 3 * cm
        start_y = -21 * cm
        self.canv.setFont('ANGSA', 12)
        for k, v in payment.items():
            if k != 'type':
                self.canv.drawString(start_x, start_y, '- {} {:,.02f} {}'.format(v['name'], float(v['value']), v['option']))
                start_y -= 0.5 * cm

        self.canv.restoreState()
        return

    def render_table(self, last=False, show_num_text=True):
        line = self.margin_buttom + (7.3 * cm)
        if last:
            text = self.canv.beginText()
            if show_num_text:
                text.setTextOrigin(self.margin_left + (5 * cm), line)
                text.setFont('ANGSA', 14)
                text.textLine(text=num_to_text.thai_num2text(self.invoice.total))
                self.canv.drawText(text)

            self.canv.setFont('ANGSA', 12)

            self.canv.drawRightString(self.margin_left + (16.7 * cm), line,
                                      '{:,d}'.format(int(self.invoice.tot_pv)))
            text.setTextOrigin(self.margin_left + (17.4 * cm), line)
            text.textLine(text='{:,.2f}'.format(self.invoice.total))
            self.canv.drawText(text)
            # self.canv.drawRightString(self.margin_left + (19.7 * cm), line,
            #                           '{:,.2f}'.format(self.invoice.total))
        return

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
        # self.canv.saveState()
        self.render_head()
        self.render_customer()
        self.render_bill_header()
        # self.canv.restoreState()

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

    def render_page_count(self):
        self.canv.setFont('ANGSA', 12)
        self.canv.drawString(inch * 7.5, 1.3 * inch, "หน้า {}/{}".format(self.page, self.total_page))
        return

    def create_pdf(self, response=None):
        item_list = []
        goods = self.invoice.items.all()
        item_count = 1
        row_count = 1
        credit = None

        code = []

        for x in goods:
            code.append(x.pcode)

        promotions = {x.pcode: x for x in Promotion.objects.prefetch_related('items').filter(pcode__in=code)}

        for x in goods:
            if x.pcode == 'SVC0001':
                credit = x
                continue
            item_name = '{} {}'.format(x.pcode, x.pdesc)
            total_item_count = 1

            total_item = [ProductDescription(no=row_count,
                                             code=x.pcode,
                                             item=x.pdesc,
                                             qty=x.qty,
                                             pv=(int(x.pv) * int(x.qty)),
                                             price=x.price,
                                             total=x.amt)]

            if x.pcode in promotions:
                for child in promotions[x.pcode].items.all():
                    total_item_count += 1
                    child_name = '{} {} ({})'.format(child.pcode, child.pdesc, int(child.qty * x.qty))
                    total_item.append(PromotionDescription(item=child_name))

            # item_count += total_item_count
            row_count += 1

            item_count = self._determind_page_break(item_count, total_item_count, item_list)
            for item in total_item:
                item_list.append(item)

        if credit:
            item_name = '{} {}'.format(credit.pcode, credit.pdesc)
            item_list.append(ProductDescription(no=row_count,
                                                code=credit.pcode,
                                                item=credit.pdesc,
                                                qty=1,
                                                pv=0,
                                                price=credit.price,
                                                total=credit.amt))
        row_count += 1
        self._determind_page_break(item_count, 1, item_list)

        # if self.invoice.shipment_fee:
        #     item_list.append(ProductDescription(no=row_count,
        #                                         item='ค่าจัดส่ง',
        #                                         qty=1,
        #                                         pv=0,
        #                                         price=self.invoice.shipment_fee,
        #                                         total=self.invoice.shipment_fee))

        self.build(item_list, filename=response)
        return self.canv

    def create_page_template(self):
        frame_template = Frame(self.leftMargin, self.bottomMargin + (6.5 * cm),
                               self.width, self.height - (12.6 * cm),
                               id='normal', showBoundary=0)
        frame_last = Frame(self.leftMargin, self.bottomMargin + (6.5 * cm),
                           self.width, self.height - (12.6 * cm),
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
        if current > 25:
            items.append(PageBreak())
            current = 1
        return current