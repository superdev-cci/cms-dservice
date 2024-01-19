from reportlab.lib.units import cm, inch, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageBreak, Frame, PageTemplate
from reportlab.graphics.barcode import code128
from io import BytesIO


class TaxTawi50Template(object):
    page_size = (864.0, 1056.0) # 9 inch x 11 inch dpi96
    text_position = {
        'doc_number': (page_size[0]-(6.1*cm), page_size[1]-(1.7*cm)),
        'company_tax_number': (page_size[0]-(10.1*cm), page_size[1]-(2.7*cm)),
        'company_name': (3.4*cm, page_size[1]-(3.65*cm)),
        'company_address': (3.4*cm, page_size[1]-(4.75*cm)),
        'customer_tax_number': (page_size[0]-(10.1*cm), page_size[1]-(6.2*cm)),
        'customer_name': (3.4*cm, page_size[1]-(7.15*cm)),
        'customer_address': (3.4*cm, page_size[1]-(8.25*cm)),
        'run_number_tax': (3.85*cm, page_size[1]-(9.85*cm)),
        'sum_text': (8.35*cm, 9.48*cm),
        'saving_money_name': (7*cm, 8.26*cm),
        'employer_id': (2.5*cm, 5.8*cm),
        'item_6_topic': (4.5*cm, 12.9*cm),

        # Position from RIGHT
        'item_1': (page_size[0]-(2.6*cm), page_size[1]-(12.4*cm)),
        'item_2': (page_size[0]-(2.6*cm), page_size[1]-(13.2*cm)),
        'item_3': (page_size[0]-(2.6*cm), page_size[1]-(14*cm)),
        'item_4_a': (page_size[0]-(2.6*cm), page_size[1]-(14.8*cm)),
        'item_4_b': (page_size[0]-(2.6*cm), page_size[1]-(15.6*cm)),
        'item_4_1_1.1': (page_size[0]-(2.6*cm), page_size[1]-(17*cm)),
        'item_4_1_1.2': (page_size[0]-(2.6*cm), page_size[1]-(17.6*cm)),
        'item_4_1_1.3': (page_size[0]-(2.6*cm), page_size[1]-(18.2*cm)),
        'item_4_1_1.4': (page_size[0]-(2.6*cm), page_size[1]-(18.8*cm)),
        'item_4_2': (page_size[0]-(2.6*cm), page_size[1]-(19.6*cm)),
        'item_4_3': (page_size[0]-(2.6*cm), page_size[1]-(20.4*cm)),
        'item_5': (page_size[0]-(2.6*cm), page_size[1]-(21.8*cm)),
        'item_6': (page_size[0]-(2.6*cm), page_size[1]-(24.4*cm)),
        'sum_paid': (page_size[0]-(7.8*cm), 10.6*cm),
        'sum_vat': (page_size[0]-(2.6*cm), 10.6*cm),
        'employee_tax_id': (page_size[0]-(3.4*cm), 5.8*cm),
        'insurance': (page_size[0]-(7.55*cm), 7.36*cm),
        'saving_money_amount': (page_size[0]-(3.5*cm), 8.26*cm)
    }

    def __init__(self, file_name, data=None, *args, **kwargs):
        self.file_name = '{}.pdf'.format(file_name)
        pdfmetrics.registerFont(TTFont('THSarabunNew', './templates/THSarabunNew.ttf'))
        pdfmetrics.registerFont(TTFont('THSarabunNew Bold', './templates/THSarabunNew Bold.ttf'))
        pdfmetrics.registerFont(TTFont('THSarabunNew Italic', './templates/THSarabunNew Italic.ttf'))
        self.pdf_file = canvas.Canvas(self.file_name, pagesize=self.page_size)

    def render_template(self):
        self.pdf_file.setFillColor("#000000")
        self.pdf_file.setLineWidth(1.5)
        self.pdf_file.roundRect(2*cm, 2*cm, self.page_size[0]-(4.4*cm), self.page_size[1]-(4.1*cm), 0)

        self.pdf_file.setLineWidth(0.5)
        self.pdf_file.rect(20.15*cm, self.page_size[1]-(2.9*cm), 7.2*cm, 0.8*cm)
        self.pdf_file.rect(20.15*cm, self.page_size[1]-(6.4*cm), 7.2*cm, 0.8*cm)
        self.pdf_file.line(2*cm, self.page_size[1]-(9*cm), self.page_size[0]-(2.4*cm), self.page_size[1]-(9*cm)) #full line
        self.pdf_file.rect(3.7*cm, self.page_size[1]-(10.1*cm), 3*cm, 0.8*cm)
        self.pdf_file.rect(8.2*cm, self.page_size[1]-(9.6*cm), 0.7*cm, 0.4*cm)
        self.pdf_file.rect(8.2*cm, self.page_size[1]-(10.4*cm), 0.7*cm, 0.4*cm)
        self.pdf_file.rect(13.2*cm, self.page_size[1]-(9.6*cm), 0.7*cm, 0.4*cm)
        self.pdf_file.rect(13.2*cm, self.page_size[1]-(10.4*cm), 0.7*cm, 0.4*cm)
        self.pdf_file.rect(18.2*cm, self.page_size[1]-(9.6*cm), 0.7*cm, 0.4*cm)
        self.pdf_file.rect(18.2*cm, self.page_size[1]-(10.4*cm), 0.7*cm, 0.4*cm)
        self.pdf_file.rect(23.2*cm, self.page_size[1]-(9.6*cm), 0.7*cm, 0.4*cm)
        self.pdf_file.line(2*cm, self.page_size[1]-(10.55*cm), self.page_size[0]-(2.4*cm), self.page_size[1]-(10.55*cm))
        self.pdf_file.line(2*cm, self.page_size[1]-(11.8*cm), self.page_size[0]-(2.4*cm), self.page_size[1]-(11.8*cm))
        self.pdf_file.line(14.2*cm, self.page_size[1]-(10.55*cm), 14.2*cm, self.page_size[1]-(26*cm))
        self.pdf_file.line(17.75*cm, self.page_size[1]-(10.55*cm), 17.75*cm, self.page_size[1]-(26.9*cm))
        self.pdf_file.line(22.05*cm, self.page_size[1]-(11.8*cm), 22.05*cm, self.page_size[1]-(26.8*cm))
        self.pdf_file.line(22.95*cm, self.page_size[1]-(10.55*cm), 22.95*cm, self.page_size[1]-(26.8*cm))
        self.pdf_file.line(27.25*cm, self.page_size[1]-(11.8*cm), 27.25*cm, self.page_size[1]-(26.8*cm))
        self.pdf_file.rect(3.3*cm, self.page_size[1]-(17.03*cm), 0.3*cm, 0.3*cm)
        self.pdf_file.rect(3.3*cm, self.page_size[1]-(17.63*cm), 0.3*cm, 0.3*cm)
        self.pdf_file.rect(3.3*cm, self.page_size[1]-(18.23*cm), 0.3*cm, 0.3*cm)
        self.pdf_file.rect(3.3*cm, self.page_size[1]-(18.83*cm), 0.3*cm, 0.3*cm)
        self.pdf_file.line(14.2*cm, self.page_size[1]-(26*cm), self.page_size[0]-(2.4*cm), self.page_size[1]-(26*cm))
        self.pdf_file.line(17.75*cm, self.page_size[1]-(26.8*cm), self.page_size[0]-(2.4*cm), self.page_size[1]-(26.8*cm))
        self.pdf_file.line(17.75*cm, self.page_size[1]-(26.9*cm), self.page_size[0]-(2.4*cm), self.page_size[1]-(26.9*cm))
        self.pdf_file.line(2*cm, 9*cm, self.page_size[0]-(2.4*cm), 9*cm)
        self.pdf_file.line(2*cm, 8*cm, self.page_size[0]-(2.4*cm), 8*cm)
        self.pdf_file.rect(2.3*cm, 5.6*cm, 0.75*cm, 0.85*cm)
        self.pdf_file.rect(3.05*cm, 5.6*cm, 0.75*cm, 0.85*cm)
        self.pdf_file.line(3.8*cm, 6.05*cm, 4*cm, 6.05*cm)
        self.pdf_file.line(9.25*cm, 6.05*cm, 9.45*cm, 6.05*cm)
        self.pdf_file.rect(9.45*cm, 5.6*cm, 0.75*cm, 0.85*cm)
        self.pdf_file.rect(17.3*cm, 5.6*cm, 0.75*cm, 0.85*cm)
        self.pdf_file.rect(18.05*cm, 5.6*cm, 0.75*cm, 0.85*cm)
        self.pdf_file.line(18.8*cm, 6.05*cm, 19*cm, 6.05*cm)
        self.pdf_file.line(26.5*cm, 6.05*cm, 26.7*cm, 6.05*cm)
        self.pdf_file.rect(26.7*cm, 5.6*cm, 0.75*cm, 0.85*cm)
        self.pdf_file.line(2*cm, 5.45*cm, self.page_size[0]-(2.4*cm), 5.45*cm)
        self.pdf_file.line(6.65*cm, 5.45*cm, 6.65*cm, 2*cm)
        self.pdf_file.circle(self.page_size[0]-(4.25*cm), 3.75*cm, 1.15*cm)
        for i in range(0, 7):
            self.pdf_file.rect((4+0.75*i)*cm, 5.6*cm, 0.75*cm, 0.85*cm)

        for i in range(0, 10):
            self.pdf_file.rect((19+0.75*i)*cm, 5.6*cm, 0.75*cm, 0.85*cm)

        for i in range(0, 4):
            self.pdf_file.rect(2.3*cm, (2.3+0.65*i)*cm, 0.6*cm, 0.35*cm)

        self.pdf_file.setFont('THSarabunNew Italic', 14)
        self.pdf_file.drawString(9.2*cm, self.page_size[1]-(1*cm), u"ฉบับที่  1  ( สำหรับผู้ถูกหักภาษี  ณ  ที่จ่าย  ใช้แนบพร้อมกับแบบแสดงรายการภาษี )")
        self.pdf_file.drawString(3.3*cm, self.page_size[1]-(4.1*cm), u"( ให้ระบุว่าเป็น บุคคล นิติบุคคล บริษัท สมาคม หรือคณะบุคคล )")
        self.pdf_file.drawString(3.3*cm, self.page_size[1]-(5.25*cm), u"( ให้ระบุชื่ออาคาร/หมู่บ้าน ห้องเลขที่ ชั้นที่ เลขที่ ตรอก/ซอย หมู่ที่ ถนน ตำบล/แขวง อำเภอ/เขต จังหวัด )")
        self.pdf_file.drawString(3.3*cm, self.page_size[1]-(7.6*cm), u"( ให้ระบุว่าเป็น บุคคล นิติบุคคล บริษัท สมาคม หรือคณะบุคคล )")
        self.pdf_file.drawString(3.3*cm, self.page_size[1]-(8.75*cm), u"( ให้ระบุชื่ออาคาร/หมู่บ้าน ห้องเลขที่ ชั้นที่ เลขที่ ตรอก/ซอย หมู่ที่ ถนน ตำบล/แขวง อำเภอ/เขต จังหวัด )")

        self.pdf_file.setFont('THSarabunNew Bold', 25)
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(1.8*cm), u"หนังสือรับรองการหักภาษี  ณ  ที่จ่าย")

        self.pdf_file.setFont('THSarabunNew Bold', 18)
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(2.7*cm), u"ผู้มีหน้าที่หักภาษี ณ ที่จ่าย : ")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(6.2*cm), u"ผู้ถูกหักภาษี ณ ที่จ่าย : ")

        self.pdf_file.setFont('THSarabunNew Bold', 16)
        self.pdf_file.drawString(5.9*cm, self.page_size[1]-(11.4*cm), u"ประเภทเงินได้พึงประเมินที่จ่าย")
        self.pdf_file.drawString(14.95*cm, self.page_size[1]-(11.1*cm), u"วัน เดือน หรือ")
        self.pdf_file.drawString(15.1*cm, self.page_size[1]-(11.65*cm), u"ปีภาษีที่จ่าย")
        self.pdf_file.drawString(19.15*cm, self.page_size[1]-(11.4*cm), u"จำนวนเงินที่จ่าย")
        self.pdf_file.drawString(23.9*cm, self.page_size[1]-(11.4*cm), u"ภาษีที่หักและนำส่งไว้")
        self.pdf_file.drawString(12.5*cm, 10.6*cm, u"รวมเงินที่จ่ายและภาษีที่หักนำส่ง")
        self.pdf_file.drawString(2.75*cm, 9.5*cm, u"รวมเงินภาษีที่หักนำส่ง (ตัวอักษร)")

        self.pdf_file.setFont('THSarabunNew', 18)
        self.pdf_file.drawString(11.4*cm, self.page_size[1]-(1.8*cm), u"ตามมาตรา  ๕๐  ทวิ  แห่งประมวลรัษฎากร")
        self.pdf_file.drawString(self.page_size[0]-(7.1*cm), self.page_size[1]-(1.8*cm), u"เลขที่...................................")
        self.pdf_file.drawString(9.15*cm, 4.8*cm, u"ขอรับรองว่า ข้อความและตัวเลขดังกล่าวข้างต้นถูกต้องตรงกับความจริงทุกประการ")

        self.pdf_file.setFont('THSarabunNew', 15)
        self.pdf_file.drawString(15.9*cm, self.page_size[1]-(2.7*cm), u"เลขประจำตัวผู้เสียภาษีอากร")
        self.pdf_file.drawString(15.9*cm, self.page_size[1]-(6.2*cm), u"เลขประจำตัวผู้เสียภาษีอากร")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(3.7*cm), u"ชื่อ  ..............................................................................................................................................................................................................................................................................................")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(4.8*cm), u"ที่อยู่  ...........................................................................................................................................................................................................................................................................................")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(7.2*cm), u"ชื่อ  ..............................................................................................................................................................................................................................................................................................")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(8.3*cm), u"ที่อยู่  ...........................................................................................................................................................................................................................................................................................")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(9.9*cm), u"ลำดับที่")
        self.pdf_file.drawString(6.9*cm, self.page_size[1]-(9.9*cm), u"ในแบบ")
        self.pdf_file.drawString(9.1*cm, self.page_size[1]-(9.55*cm), u"(1) ภ.ง.ด.1ก.")
        self.pdf_file.drawString(9.1*cm, self.page_size[1]-(10.35*cm), u"(5) ภ.ง.ด.2ก.")
        self.pdf_file.drawString(14.1*cm, self.page_size[1]-(9.55*cm), u"(2) ภ.ง.ด.1ก. พิเศษ")
        self.pdf_file.drawString(14.1*cm, self.page_size[1]-(10.35*cm), u"(6) ภ.ง.ด.3ก.")
        self.pdf_file.drawString(19.1*cm, self.page_size[1]-(9.55*cm), u"(3) ภ.ง.ด.2")
        self.pdf_file.drawString(19.1*cm, self.page_size[1]-(10.35*cm), u"(7) ภ.ง.ด.53")
        self.pdf_file.drawString(24.1*cm, self.page_size[1]-(9.55*cm), u"(4) ภ.ง.ด.3")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(12.4*cm), u"1.  เงินเดือน ค่าจ้าง เบี้ยเลี้ยง โบนัส ฯลฯ ตามมาตรา 40 (1)")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(13.2*cm), u"2.  ค่าธรรมเนียม ค่านายหน้า ฯลฯ ตามมาตรา 40 (2)")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(14*cm), u"3.  ค่าแห่งลิขสิทธิ์ ฯลฯ ตามมาตรา 40 (3)")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(14.8*cm), u"4.  (ก) ค่าดอกเบี้ย ฯลฯ ตามมาตรา 40 (4) (ก)")
        self.pdf_file.drawString(2.32*cm, self.page_size[1]-(15.6*cm), u"    (ข) เงินปันผล เงินส่วนแบ่งกำไร ฯลฯ ตามมาตรา 40 (4) (ข) ที่จ่ายจาก")
        self.pdf_file.drawString(2.32*cm, self.page_size[1]-(16.4*cm), u"    (1) กิจการที่ต้องเสียภาษีเงินได้นิติบุคคลในอัตราดังนี้")
        self.pdf_file.drawString(3.75*cm, self.page_size[1]-(17*cm), u"(1.1) อัตราร้อยละ 30 ของกำไรสุทธิ")
        self.pdf_file.drawString(3.75*cm, self.page_size[1]-(17.6*cm), u"(1.2) อัตราร้อยละ 25 ของกำไรสุทธิ")
        self.pdf_file.drawString(3.75*cm, self.page_size[1]-(18.2*cm), u"(1.3) อัตราร้อยละ 20 ของกำไรสุทธิ")
        self.pdf_file.drawString(3.75*cm, self.page_size[1]-(18.8*cm), u"(1.4) อัตราอื่นๆ (ระบุ)....................ของกำไรสุทธิ")
        self.pdf_file.drawString(2.32*cm, self.page_size[1]-(19.6*cm), u"    (2) กิจการที่ได้รับยกเว้นภาษีเงินได้นิติบุคคล ซึ่งผู้รับเงินปันผลไม่ได้รับเครดิตภาษี")
        self.pdf_file.drawString(2.32*cm, self.page_size[1]-(20.4*cm), u"    (3) กำไรเฉพาะส่วนที่ได้รับยกเว้นไม่ต้องนำมารวมคำนวณภาษีเงินได้นิติบุคคล")
        self.pdf_file.drawString(3.3*cm, self.page_size[1]-(21*cm), u"ซึ่งผู้ได้รับเงินปันผลไม่ได้รับเครดิตภาษี")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(21.8*cm), u"5.  การจ่ายเงินได้ที่ต้องหักภาษี ณ ที่จ่าย ตามคำสั่งกรมสรรพากรที่ออกตามมาตรา")
        self.pdf_file.drawString(2.33*cm, self.page_size[1]-(22.4*cm), u"    3 เตรส เช่น รางวัล ส่วนลด หรือประโยชน์ใดๆ เนื่องจากการส่งเสริมการขาย")
        self.pdf_file.drawString(2.33*cm, self.page_size[1]-(23*cm), u"    รางวัลในการประกวด การแข่งขัน การชิงโชค ค่าแสดงของนักแสดงสาธารณะ")
        self.pdf_file.drawString(2.33*cm, self.page_size[1]-(23.6*cm), u"    ค่าจ้างทำของ ค่าจ้างโฆษณา ค่าเช่า ค่าขนส่ง ค่าบริการ ค่าเบี้ยประกันวินาศภัยฯลฯ")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(24.4*cm), u"6.  อื่นๆ (ระบุ)................................................................................................................")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(25.2*cm), u"........................................................................................................................................")
        self.pdf_file.drawString(2.3*cm, self.page_size[1]-(26*cm), u"........................................................................................................................................")
        self.pdf_file.drawString(2.3*cm, 8.2*cm, u"เงินสะสมจ่ายเข้ากองทุนสำรอง..............................................................................................................................................จำนวน.......................................................................................บาท")
        self.pdf_file.drawString(6.45*cm, 7.3*cm, u"เงินสมทบจ่ายเข้ากองทุนประกันสังคม  จำนวนเงิน...................................................................................................................บาท")
        self.pdf_file.drawString(5.1*cm, 6.6*cm, u"เลขที่บัญชีนายจ้าง")
        self.pdf_file.drawString(19.1*cm, 6.6*cm, u"เลขที่บัตรประกันสังคม ของผู้ถูกหักภาษี ณ ที่จ่าย")
        self.pdf_file.drawString(2.3*cm, 4.9*cm, u"ผู้จ่ายเงิน")
        self.pdf_file.drawString(9.15*cm, 3.6*cm, u"(ลงชื่อ)........................................................................................................ผู้มีหน้าที่หีกภาษี ณ ที่จ่าย")
        self.pdf_file.drawString(9.15*cm, 2.4*cm, u".......................................................................................................วัน เดือน ปี ที่ออกหนังสือรับรองฯ")
        self.pdf_file.drawString(self.page_size[0]-(5*cm), 4.15*cm, u"ตราประทับ")
        self.pdf_file.drawString(self.page_size[0]-(4.85*cm), 3.55*cm, u"นิติบุคคล")
        self.pdf_file.drawString(self.page_size[0]-(4.5*cm), 2.95*cm, u"ถ้ามี")
        self.pdf_file.drawString(2.3*cm, 1.4*cm, u"หมายเหตุ")
        self.pdf_file.drawString(4.2*cm, 1.4*cm, u"ให้สามารถอ้างอิงหรือสอบยันกันได้ระหว่างลำดับที่ตามหนังสือรับรองฯ กับแบบยื่นรายการหักภาษี ณ ที่จ่าย")
        self.pdf_file.drawString(2.3*cm, 0.8*cm, u"คำเตือน")
        self.pdf_file.drawString(4.2*cm, 0.8*cm, u"ผู้มีหน้าที่ออกหนังสือรับรองการหักภาษี ณ ที่จ่าย ฝ่าฝืนไม่ปฏิบัติตามมาตรา 50 ทวิ แห่งประมวลรัษฎากร ต้องรับโทษทางอาญาจามมาตรา 35 แห่งประมวลรัษฎากร")
        textlist = ["อื่นๆ (ให้ระบุ)..........", "ออกภาษีให้ครั้งเดียว", "ออกภาษีให้ตลอดไป", "หักภาษี ณ ที่จ่าย"]
        for i in range(0, 4):
            self.pdf_file.drawString(3.2*cm, (2.3+0.65*i)*cm, textlist[i])

        self.pdf_file.setFillColor("#EEEEEE")
        self.pdf_file.setLineWidth(0.5)
        self.pdf_file.rect(8.15*cm, 9.2*cm, 19.65*cm, 1*cm, fill=True)


    def render_data(self):
        pass
        # #Fill Sample Data
        # self.pdf_file.setFillColor("#000000")
        # self.pdf_file.setFont('THSarabunNew Italic', 16)
        # self.pdf_file.drawString(*(*self.text_position['doc_number'], u"test0001"))
        # self.pdf_file.drawString(*(*self.text_position['company_tax_number'], u"0-1055-59080-08-9"))
        # self.pdf_file.drawString(*(*self.text_position['company_name'], u"บริษัท แชมป์ ออฟ แชมป์ อินโนเวชั่น จำกัด"))
        # self.pdf_file.drawString(*(*self.text_position['company_address'], u"เลขที่ 9 อาคารพุทธวิชชาลัย โซนบี และ โซนซี ถนนแจ้งวัฒนะ แขวงอนุสาวรีย์ เขตบางเขน กรุงเทพฯ 10220"))
        # self.pdf_file.drawString(*(*self.text_position['customer_tax_number'], u"1-2345-67890-12-3"))
        # self.pdf_file.drawString(*(*self.text_position['customer_name'], u"สมชาย ใจดี"))
        # self.pdf_file.drawString(*(*self.text_position['customer_address'], u"123 ซ.รัชดาภิเษก99 ถ.รัชดาภิเษก แขวงดินแดง เขตดินแดง กรุงเทพฯ 99999"))
        # self.pdf_file.drawString(*(*self.text_position['run_number_tax'], u"1234"))
        # self.pdf_file.drawString(*(*self.text_position['sum_text'], u"เจ็ดแสนสองหมื่นเก้าพันหกร้อยสิบเอ็ดบาท"))
        # self.pdf_file.drawString(*(*self.text_position['saving_money_name'], u"เพื่อการเกษียนก่อนอายุ 50 ปี"))
        # self.pdf_file.drawString(*(*self.text_position['employer_id'], u"1234567890"))
        # self.pdf_file.drawString(*(*self.text_position['item_6_topic'], u"ค่าสนับสนุนเล่าเรียน"))

        # self.pdf_file.drawRightString(*(*self.text_position['saving_money_amount'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['insurance'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['employee_tax_id'], u"1234567890123"))

        # self.pdf_file.setFont('THSarabunNew Italic', 18)
        # self.pdf_file.drawRightString(*(*self.text_position['item_1'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_2'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_3'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_4_a'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_4_b'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_4_1_1.1'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_4_1_1.2'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_4_1_1.3'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_4_1_1.4'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_4_2'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_4_3'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_5'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['item_6'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['sum_vat'], u"9,999.99"))
        # self.pdf_file.drawRightString(*(*self.text_position['sum_paid'], u"9,999.99"))


    def save_pdf(self):
        self.render_template()
        # self.pdf_file.showPage()
        # self.render_template()
        self.render_data()
        # self.pdf_file.setFillColor("#000000")
        # self.pdf_file.drawRightString(6.1*1.3*cm, 6.3*1.3*cm, 'Hello World')
        # self.pdf_file.setFillColor("red")
        # self.pdf_file.drawString(6.1*1.3*cm, 6.3*1.3*cm, 'Hello World')
        self.pdf_file.save()