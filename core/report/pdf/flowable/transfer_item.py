from reportlab.lib.units import cm
from reportlab.platypus import Flowable


class TransferItem(Flowable):

    def __init__(self, **kwargs):
        super(TransferItem, self).__init__()
        self.width = 10 * cm
        self.height = 0.5 * cm
        self.no = kwargs.get('no', 0)
        self.code = kwargs.get('code', '-')
        self.item = kwargs.get('item', '-')
        self.qty = kwargs.get('qty', 0)

        return

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setFont('ANGSA', 16)
        self.canv.drawRightString(-0.08 * cm, 0, '{}'.format(self.no))
        self.canv.drawString(0.6 * cm, 0, self.code)
        self.canv.drawString(2.5 * cm, 0, self.item)
        self.canv.drawRightString(16 * cm, 0, '{:,d}'.format(int(self.qty)))
        canvas.restoreState()
        return
