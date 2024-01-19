from reportlab.lib.units import cm, inch
from reportlab.platypus import Flowable


class ProductDescription(Flowable):

    def __init__(self, **kwargs):
        super(ProductDescription, self).__init__()
        self.width = 9 * inch
        self.height = 0.5 * cm
        self.no = kwargs.get('no', 0)
        self.item = kwargs.get('item', '-')
        self.qty = kwargs.get('qty', 0)
        self.pv = kwargs.get('pv', 0)
        self.price = kwargs.get('price', 0)
        self.total = kwargs.get('total', 0)
        self.code = kwargs.get('code', '')

        return

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setFont('ANGSA', 16)
        self.canv.drawRightString(-0.2 * cm, 0, '{}'.format(self.no))
        self.canv.drawString(0.5 * cm, 0, self.code)

        text = self.canv.beginText()
        text.setTextOrigin(3.3 * cm, 0)
        text.setFont('ANGSA', 16)
        text.textLine(text=self.item)
        self.canv.drawText(text)

        # self.canv.drawString(3.3 * cm, 0, self.item)
        self.canv.drawRightString(11 * cm, 0, '{:,}'.format(int(self.qty)))
        self.canv.drawRightString(13.5 * cm, 0, '{:,.2f}'.format(self.price))
        self.canv.drawRightString(15.5 * cm, 0, '{:,d}'.format(int(self.pv)))
        text.setTextOrigin(16.2 * cm, 0)
        text.textLine(text='{:,.2f}'.format(self.total))
        self.canv.drawText(text)
        canvas.restoreState()
        return
