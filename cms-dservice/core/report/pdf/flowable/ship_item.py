from reportlab.lib.units import cm
from reportlab.platypus import Flowable


class ShipItem(Flowable):

    def __init__(self, **kwargs):
        super(ShipItem, self).__init__()
        self.width = 10 * cm
        self.height = 0.5 * cm
        self.no = kwargs.get('no', 0)
        self.item = kwargs.get('item', '-')
        self.qty = kwargs.get('qty', 0)

        return

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setFont('THSarabunNew', 13)
        self.canv.drawRightString(15, 0, '{}'.format(self.no))
        self.canv.drawString(1 * cm, 0, self.item)
        # self.canv.drawRightString(9.7 * cm, 0, '{:,}'.format(int(self.qty)))
        # self.canv.drawRightString(11.55 * cm, 0, '{:,.2f}'.format(self.price))
        # self.canv.drawRightString(12.9 * cm, 0, '{:,d}'.format(int(int(self.pv) * int(self.qty))))
        self.canv.drawRightString(15.3 * cm, 0, '{:,d}'.format(int(self.qty)))
        canvas.restoreState()
        return
