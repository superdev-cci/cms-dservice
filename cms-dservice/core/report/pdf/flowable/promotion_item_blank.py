from reportlab.lib.units import cm
from reportlab.platypus import Flowable


class PromotionDescription(Flowable):

    def __init__(self, **kwargs):
        super(PromotionDescription, self).__init__()
        self.width = 10 * cm
        self.height = 0.35 * cm
        self.item = kwargs.get('item', '-')
        return

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setFont('ANGSAI', 14)
        self.canv.drawString(3.3 * cm, 0, ' - {}'.format(self.item))
        canvas.restoreState()
        return
